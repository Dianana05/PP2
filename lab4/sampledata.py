import json

with open(r"C:\Users\user\Desktop\PP2\lab4\sample_data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("DN".ljust(50), "Description".ljust(20), "Speed".ljust(8), "MTU".ljust(8))
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    DN = attributes["dn"]
    Description = attributes.get("descr", "")
    Speed = attributes.get("speed", "inherit")
    MTU = attributes["mtu"]

    print(DN.ljust(50), Description.ljust(20), Speed.ljust(8), MTU.ljust(8))
