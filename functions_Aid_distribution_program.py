import json
FILENAME = "aid_inventory.txt"

#دالة تحويل نص ملف ابجسون الى قواميس بداخل قائمة
def load_data():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data_list = json.load(f)
        return data_list

    except FileNotFoundError:
        print("Inventory file not found.")
        return []

    except json.JSONDecodeError:
        print("Inventory file contains invalid data.")
        return []

def menu():
    print("1. Inventory Review")
    print("2. Add New Aid Shipment")
    print("3. Distribute Aid")
    print("4. Search Item")
    print("5. Inventory Report")
    print("6. Exit")

    try:
        num = int(input("---What process do you need?---\n"))
        return num
    except ValueError:
        print("Please enter a number.")
        return 0

def display_aids(data_list):
    count = 1
    for i in data_list:
        print(count, "- ", i)
        count +=1

def add_shipment(data_list):
    item = input("Item Name: ")
    try:
        quantity = int(input("Quantity Number: "))
    except ValueError:
        print("Quantity must be a number.")
        return
    donor = input("Donor: ")

    found = False
    for i in data_list:
        if i['item'].lower() == item.lower():
           i['quantity'] += quantity
           print(f"Quantity updated: {item}.")
           found = True
           break

    if not found:
        new_item = {"item" : item, "quantity" : quantity, "donor" : donor}
        data_list.append(new_item)
        print("The item has been added successfully!")

    return data_list

def distribute_aid(data_list):
    item_name = input("Name of the item to be distributed: ").strip()
    found_item = None

    for i in data_list:
        if i['item'].lower() == item_name.lower():
            found_item = i
            break

    if found_item:
        print(f"Item '{found_item['item']}' found. Available quantity: {found_item['quantity']}")

        if found_item['quantity'] > 0:
            # طلب الكمية بعد التأكد من وجودها
            try:
                item_num = int(input("Specify the required quantity to distribute: "))

                # التحقق من كفاية الكمية
                if item_num <= found_item['quantity']:
                    found_item['quantity'] -= item_num
                    print(f"Distributed successfully! Remaining quantity: {found_item['quantity']}.")
                else:
                    print(f"Error: Not enough stock! Only {found_item['quantity']} available.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        else:
            print("Sorry! The item is currently out of stock (0 quantity).")

    else:
        print("Item not found in the inventory.")

    return data_list

def search_item(data_list):
    name = input("Enter the item name to search for: ").strip()
    found = False  # متغير تتبع

    for i in data_list:
        if i['item'].lower() == name.lower():
            print(f"\nItem details:")
            print(f"Name: {i['item']}")
            print(f"Available Quantity: {i['quantity']}")
            print(f"Donor: {i['donor']}")
            found = True
            break  # نخرج من الحلقة بمجرد العثور على المادة

    # هذا الجزء ينفذ فقط إذا انتهت الحلقة ولم نجد المادة
    if not found:
        print("Sorry, this item was not found in the inventory.")

def report(data_list: list):
    print("WAREHOUSE INVENTORY REPORT")
    if not data_list:
        print("The inventory is currently empty. No items to display.")
        return

    print(f"{'Item':<25} {'Quantity':<15} {'Donor':<30}")
    print("-" * 75)
    for i in data_list:
        print(f"{i['item']:<25} {i['quantity']:<15} {i['donor']:<30}")
    print("-" * 75)
    print(f"Total unique item groups tracked: {len(data_list)}")

def save_inventory(inventory: list) -> bool:
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=4)
        return True

    except IOError as e:
        print(f"[Error] Failed to write data to storage: {e}")
        return False