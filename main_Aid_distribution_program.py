import functions_Aid_distribution_program as funs
import os

#تحويل الداتا في ملف الجسون المشكلة على شكل قواميس الى قائمة بدخلها
data_list_success = funs.load_data()
print(" ")

while True:
    num = funs.menu()
    if num == 1:
        funs.display_aids(data_list_success)
    elif num == 2:
        funs.add_shipment(data_list_success)
    elif num == 3:
        funs.distribute_aid(data_list_success)
    elif num == 4:
        funs.search_item(data_list_success)
    elif num == 5:
        funs.report(data_list_success)
    elif num == 6:
        print("\nSaving updated data to local storage...")
        if funs.save_inventory(data_list_success):
            print("Inventory saved successfully.")
        break
    else:
        print("[Error] Invalid menu option selected. Please choose a value between 1 and 5.")

#الداتا الاصلية:
# [
#     {
#         "item": "Flour", "quantity": 1500, "donor": "World Food Programme"
#     },
#     {
#         "item": "Rice",
#         "quantity": 2000,
#         "donor": "UNRWA"
#     },
#     {
#         "item": "Blankets",
#         "quantity": 500,
#         "donor": "Red Crescent"
#     },
#     {
#         "item": "Insulin",
#         "quantity": 350,
#         "donor": "WHO"
#     },
#     {
#         "item": "Baby Formula",
#         "quantity": 800,
#         "donor": "UNICEF"
#     },
#     {
#         "item": "Solar Panels",
#         "quantity": 120,
#         "donor": "Qatar Charity"
#     },
#     {
#         "item": "Painkillers",
#         "quantity": 1000,
#         "donor": "WHO"
#     },
#     {
#         "item": "Drinking Water",
#         "quantity": 3000,
#         "donor": "UNICEF"
#     },
#     {
#         "item": "Winter Jackets",
#         "quantity": 400,
#         "donor": "Red Crescent"
#     },
#     {
#         "item": "Soap",
#         "quantity": 1200,
#         "donor": "Qatar Charity"
#     }
# ]
