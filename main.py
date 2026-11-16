import os
import json

products = {}

FILE_NAME = "products.json"


def load_products():
    global products

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            products = {
                int(product_ID): details
                for product_ID, details in data.items()
            }
    else:
        products = {}


def save_products():
    with open(FILE_NAME, "w") as file:
        json.dump(products, file, indent=4)


def display_menu():
    print("\n" + "=" * 50)
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Sell Product")
    print("7. Restock Product")
    print("8. Low Stock Alert")
    print("9. Calculate Inventory Value")
    print("10. Display Statistics")
    print("0. Exit")

    print("=" * 50)


def add_products():
    print("=" * 50)
    print("              ADD PRODUCTS")
    print("=" * 50)

    num = int(input("Enter the number of products: "))

    for i in range(num):
        print(f"\nEnter Details of Product {i + 1}")

        product_ID = int(input("Enter Product ID: "))

        if product_ID in products:
            print("Product ID Already Exists!")
            continue

        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))

        products[product_ID] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        print("Product Added Successfully!")


def view_All_Products():
    print("=" * 50)
    print("             VIEW ALL PRODUCTS")
    print("=" * 50)

    if not products:
        print("No Products Available!")
    else:
        for product_ID, details in products.items():
            print("-" * 50)
            print("Product ID :", product_ID)
            print("Name       :", details["name"])
            print("Price      :", details["price"])
            print("Quantity   :", details["quantity"])

    print("=" * 50)


def search_product():
    print("=" * 50)
    print("              SEARCH PRODUCT")
    print("=" * 50)

    product_ID = int(input("Enter Product ID: "))

    if product_ID in products:
        print("\nProduct Found!")
        print("-" * 50)
        print("Product ID :", product_ID)
        print("Name       :", products[product_ID]["name"])
        print("Price      :", products[product_ID]["price"])
        print("Quantity   :", products[product_ID]["quantity"])
    else:
        print("Product ID Not Found!")


def update_product():
    print("=" * 50)
    print("              UPDATE PRODUCT")
    print("=" * 50)

    product_ID = int(input("Enter Product ID: "))

    if product_ID in products:
        print("\n1. Update Product Price")
        print("2. Update Product Quantity")
        print("3. Update Both")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            price = float(input("Enter New Price: "))
            products[product_ID]["price"] = price
            print("Price Updated Successfully!")

        elif choice == 2:
            quantity = int(input("Enter New Quantity: "))
            products[product_ID]["quantity"] = quantity
            print("Quantity Updated Successfully!")

        elif choice == 3:
            price = float(input("Enter New Price: "))
            quantity = int(input("Enter New Quantity: "))

            products[product_ID]["price"] = price
            products[product_ID]["quantity"] = quantity

            print("Product Updated Successfully!")

        else:
            print("Invalid Choice!")
    else:
        print("Product ID Not Found!")


def delete_Product():
    print("=" * 50)
    print("              DELETE PRODUCT")
    print("=" * 50)

    product_ID = int(input("Enter Product ID: "))

    if product_ID in products:
        del products[product_ID]
        print("Product Deleted Successfully!")
    else:
        print("Product ID Not Found!")


def sell_product():
    print("=" * 50)
    print("              SELL PRODUCT")
    print("=" * 50)

    product_ID = int(input("Enter Product ID: "))

    if product_ID in products:
        print("Product Name:", products[product_ID]["name"])
        print("Available Stock:", products[product_ID]["quantity"])

        sell_quantity = int(input("Enter Selling Quantity: "))

        if sell_quantity > 0 and sell_quantity <= products[product_ID]["quantity"]:
            products[product_ID]["quantity"] -= sell_quantity

            total_price = sell_quantity * products[product_ID]["price"]

            print("\nProduct Sold Successfully!")
            print("Quantity Sold:", sell_quantity)
            print("Total Bill:", total_price)
            print("Remaining Stock:", products[product_ID]["quantity"])
        else:
            print("Invalid Quantity or Insufficient Stock!")
    else:
        print("Product ID Not Found!")


def restock_product():
    print("=" * 50)
    print("              RESTOCK PRODUCT")
    print("=" * 50)

    product_ID = int(input("Enter Product ID: "))

    if product_ID in products:
        print("Product Name:", products[product_ID]["name"])
        print("Available Stock:", products[product_ID]["quantity"])

        quantity = int(input("Enter Quantity to Add: "))

        if quantity > 0:
            products[product_ID]["quantity"] += quantity

            print("Stock Updated Successfully!")
            print("New Stock:", products[product_ID]["quantity"])
        else:
            print("Invalid Quantity!")
    else:
        print("Product ID Not Found!")


def low_stock_alert():
    print("=" * 50)
    print("              LOW STOCK ALERT")
    print("=" * 50)

    if not products:
        print("No Products Available!")
        return

    found = False

    for product_ID, details in products.items():
        if details["quantity"] <= 5:
            print("Product ID:", product_ID)
            print("Name:", details["name"])
            print("Quantity:", details["quantity"])
            print("-" * 30)
            found = True

    if not found:
        print("All Products Have Sufficient Stock!")


def calculate_inventory_value():
    print("=" * 50)
    print("              INVENTORY VALUE")
    print("=" * 50)

    total_value = 0

    for product_ID, details in products.items():
        value = details["price"] * details["quantity"]
        total_value += value

    print("Total Inventory Value:", total_value)


def display_statistics():
    print("=" * 50)
    print("              INVENTORY STATISTICS")
    print("=" * 50)

    total_products = len(products)
    total_quantity = 0
    total_value = 0

    for product_ID, details in products.items():
        total_quantity += details["quantity"]
        total_value += details["price"] * details["quantity"]

    print("Total Products:", total_products)
    print("Total Stock Quantity:", total_quantity)
    print("Total Inventory Value:", total_value)


def main():
    load_products()

    print("Previous Inventory Data Loaded Successfully!")

    while True:
        os.system("cls")

        display_menu()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_products()

        elif choice == 2:
            view_All_Products()

        elif choice == 3:
            search_product()

        elif choice == 4:
            update_product()

        elif choice == 5:
            delete_Product()

        elif choice == 6:
            sell_product()

        elif choice == 7:
            restock_product()

        elif choice == 8:
            low_stock_alert()

        elif choice == 9:
            calculate_inventory_value()

        elif choice == 10:
            display_statistics()

        elif choice == 0:
            print("\nThank You for Using Inventory Management System!")
            break

        else:
            print("Invalid Choice! Please Try Again.")

        if choice in [1, 4, 5, 6, 7]:
            save_products()
            print("\nInventory Data Saved Successfully!")

        input("\nPress Enter to Continue...")


main()