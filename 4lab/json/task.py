import json

file_path = "C:/Users/uzakb/PP2_all_labs/4lab/json/sample-data.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print(json.dumps(data, indent=4, ensure_ascii=False))

{
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        }
    ]
}

interfaces = data["imdata"]  # "imdata" ішінде интерфейстер бар





# Бастапқы тақырыптарды шығару
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

# Интерфейстерді шығару
for item in interfaces:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""  # Егер бос болса, көрсетпейміз
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")
