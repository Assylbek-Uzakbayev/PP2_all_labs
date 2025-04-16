import psycopg2
import csv
from tabulate import tabulate

# Дерекқормен қосылу
conn = psycopg2.connect(
    dbname='mydb',
    user='postgres',
    password='uzakbaev2006',
    host='localhost',
    port='5432',
    options="-c client_encoding=UTF8"
)


cur = conn.cursor()
cur.execute("SET client_encoding TO 'UTF8'")  # Кодировканы кейін орнату


# Бұдан әрі код қалыпты жұмыс істеуі керек

# Создание таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
""")
conn.commit()

def insert_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропуск заголовка
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("Данные загружены из CSV!")

def insert_from_console():
    name = input("Имя: ")
    phone = input("Телефон: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Добавлено!")

def update_entry():
    user_id = input("Введите ID записи для обновления: ")
    column = input("Какое поле хотите изменить? (name/phone): ")
    new_value = input(f"Введите новое значение для {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE user_id = %s", (new_value, user_id))
    conn.commit()
    print("Обновлено!")

def query_data():
    column = input("По какому полю выполнить поиск? (name/phone/user_id): ")
    value = input(f"Введите значение для {column}: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {column} = %s", (value,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Имя", "Телефон"], tablefmt="grid"))

def delete_data():
    column = input("По какому полю удалить? (name/phone/user_id): ")
    value = input(f"Введите значение для {column}: ")
    cur.execute(f"DELETE FROM phonebook WHERE {column} = %s", (value,))
    conn.commit()
    print("Удалено!")

def display_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Имя", "Телефон"], tablefmt="fancy_grid"))

def main():
    while True:
        print("""
ТЕЛЕФОННАЯ КНИГА — МЕНЮ
1. Загрузить из CSV
2. Добавить вручную
3. Обновить запись
4. Найти запись
5. Удалить запись
6. Показать все записи
7. Выход
        """)
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            path = input("Введите путь к CSV файлу: ")
            insert_from_csv(path)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_entry()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            display_all()
        elif choice == "7":
            break
        else:
            print("Неверный выбор!")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
