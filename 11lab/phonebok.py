import psycopg2
import csv

conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password",
    port="your_port",
    options="-c client_encoding=UTF8"  # UTF-8 кодтауын пайдалану


)
conn.autocommit = True  # Add this to handle transactions automatically
cur = conn.cursor()

def create_tables_and_procedures():
    """Create required tables and stored procedures if they don't exist"""
    try:
        # Create phonebook table if not exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebok (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(20) NOT NULL
            );
        """)
        
        # Create pagination function if not exists
        cur.execute("""
            CREATE OR REPLACE FUNCTION get_phonebok_paginated(
                limit_num INTEGER, 
                offset_num INTEGER
            ) 
            RETURNS TABLE(id INTEGER, name VARCHAR, phone VARCHAR) AS $$
            BEGIN
                RETURN QUERY 
                SELECT * FROM phonebok
                ORDER BY name
                LIMIT limit_num OFFSET offset_num;
            END;
            $$ LANGUAGE plpgsql;
        """)
        
        # Create insert/update procedure if not exists
        cur.execute("""
            CREATE OR REPLACE PROCEDURE insert_or_update_user(
                user_name VARCHAR, 
                user_phone VARCHAR
            ) AS $$
            BEGIN
                IF EXISTS (SELECT 1 FROM phonebok WHERE name = user_name) THEN
                    UPDATE phonebok SET phone = user_phone WHERE name = user_name;
                ELSE
                    INSERT INTO phonebok (name, phone) VALUES (user_name, user_phone);
                END IF;
            END;
            $$ LANGUAGE plpgsql;
        """)
        
        # Create multiple users procedure if not exists
        cur.execute("""
            CREATE OR REPLACE PROCEDURE insert_multiple_users(
                users_data VARCHAR[]
            ) AS $$
            DECLARE
                user_pair VARCHAR;
                user_name VARCHAR;
                user_phone VARCHAR;
            BEGIN
                FOREACH user_pair IN ARRAY users_data
                LOOP
                    BEGIN
                        user_name := SPLIT_PART(user_pair, ':', 1);
                        user_phone := SPLIT_PART(user_pair, ':', 2);
                        
                        IF user_name != '' AND user_phone != '' THEN
                            CALL insert_or_update_user(user_name, user_phone);
                        END IF;
                    EXCEPTION WHEN OTHERS THEN
                        -- Skip invalid entries
                        CONTINUE;
                    END;
                END LOOP;
            END;
            $$ LANGUAGE plpgsql;
        """)
        
        # Create delete procedure if not exists
        cur.execute("""
            CREATE OR REPLACE PROCEDURE delete_user_data(
                identifier VARCHAR
            ) AS $$
            BEGIN
                DELETE FROM phonebok WHERE name = identifier OR phone = identifier;
            END;
            $$ LANGUAGE plpgsql;
        """)
        
        print("Database setup completed successfully.")
    except Exception as e:
        print(f"Error setting up database: {e}")
        conn.rollback()

def insert_from_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 2:
                    continue 
                cur.execute(
                    "INSERT INTO phonebok (name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
        print("Data inserted from CSV successfully.")
    except Exception as e:
        print(f"Error inserting from CSV: {e}")

def update_contact():
    try:
        choice = input("What would you like to update? (1 - name, 2 - phone): ")
        if choice == '1':
            old_name = input("Enter the current name: ")
            new_name = input("Enter the new name: ")
            cur.execute(
                "UPDATE phonebok SET name = %s WHERE name = %s",
                (new_name, old_name)
            )
        elif choice == '2':
            name = input("Enter the name: ")
            new_phone = input("Enter the new phone number: ")
            cur.execute(
                "UPDATE phonebok SET phone = %s WHERE name = %s",
                (new_phone, name)
            )
        print("Contact updated successfully.")
    except Exception as e:
        print(f"Error updating contact: {e}")

def search_contacts():
    try:
        keyword = input("Enter a name or phone number to search: ")
        cur.execute(
            "SELECT * FROM phonebok WHERE name ILIKE %s OR phone LIKE %s",
            ('%' + keyword + '%', '%' + keyword + '%')
        )
        results = cur.fetchall()
        if results:
            print("\nSearch Results:")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        else:
            print("No contacts found.")
    except Exception as e:
        print(f"Error searching contacts: {e}")

def delete_contact():
    try:
        keyword = input("Enter the name or phone number to delete: ")
        cur.execute(
            "DELETE FROM phonebok WHERE name = %s OR phone = %s",
            (keyword, keyword)
        )
        print(f"Deleted {cur.rowcount} contact(s).")
    except Exception as e:
        print(f"Error deleting contact: {e}")

def insert_or_update_user():
    try:
        name = input("Enter name: ")
        phone = input("Enter phone number (12 digits): ")
        cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
        print("User inserted or updated successfully.")
    except Exception as e:
        print(f"Error inserting/updating user: {e}")

def insert_multiple_users():
    try:
        users_input = input("Enter users in format 'name:phone,name:phone,...': ").strip()
        
        # Clean and validate input
        user_entries = []
        for entry in users_input.split(','):
            entry = entry.strip()
            if ':' in entry:
                name, phone = entry.split(':', 1)
                if name.strip() and phone.strip():
                    user_entries.append(f"{name.strip()}:{phone.strip()}")
        
        if not user_entries:
            print("No valid entries found.")
            return
            
        # Call the procedure using CALL syntax
        with conn.cursor() as cur:
            # Convert Python list to PostgreSQL array format
            array_literal = "ARRAY['" + "','".join(user_entries) + "']"
            cur.execute(f"CALL insert_multiple_users({array_literal})")
            conn.commit()
            print(f"Successfully processed {len(user_entries)} users.")
            
    except Exception as e:
        print(f"Error inserting multiple users: {e}")
        conn.rollback()
        
def get_phonebook_paginated():
    try:
        limit = int(input("Enter number of records per page: "))
        page = int(input("Enter page number (starting from 0): "))
        offset = page * limit
        cur.execute("SELECT * FROM get_phonebok_paginated(%s, %s)", (limit, offset))
        results = cur.fetchall()
        if results:
            print(f"\nPage {page + 1} Results:")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        else:
            print("No more contacts to display.")
    except Exception as e:
        print(f"Error while fetching paginated contact list: {e}")

def delete_user_data():
    try:
        identifier = input("Enter name or phone to delete: ")
        cur.execute("CALL delete_user_data(%s)", (identifier,))
        print(f"Deleted {cur.rowcount} user(s).")
    except Exception as e:
        print(f"Error deleting user: {e}")

def main():
    create_tables_and_procedures()  # Ensure database is properly set up
    
    while True:
        print("\nPhoneBok Menu:")
        print("1. Insert data from CSV")
        print("2. Update contact")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Insert or update single user")
        print("6. Insert multiple users")
        print("7. Paginated contact list")
        print("8. Delete by stored procedure")
        print("9. Exit")

        try:
            choice = input("Choose an option: ").strip()
            
            if choice == '1':
                file_path = input("Enter the path to the CSV file: ")
                insert_from_csv(file_path)
            elif choice == '2':
                update_contact()
            elif choice == '3':
                search_contacts()
            elif choice == '4':
                delete_contact()
            elif choice == '5':
                insert_or_update_user()
            elif choice == '6':
                insert_multiple_users()
            elif choice == '7':
                get_phonebook_paginated()
            elif choice == '8':
                delete_user_data()
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid option, please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    finally:
        cur.close()
        conn.close()