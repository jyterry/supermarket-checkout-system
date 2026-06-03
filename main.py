import csv


products = []
shopping_list = []
total = 0


with open("products.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        products.append({"id": row["id"], "name": row["name"], "price": float(row["price"])})


while True:
    code = input("Please enter item's code: ")

    if code == "checkout":
        break

    status = False

    for item in products:
        if item["id"] == code:
            shopping_list.append({"name": item["name"], "price": item["price"]})
            status = True
            for cart_item in shopping_list:
                print(cart_item)
            break
            
    if not status:
        print("Can't find the item!")
        continue

for final_item in shopping_list:
    print(final_item)
    total += final_item["price"]

print(f"total: {total}")