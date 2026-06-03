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
            for item in shopping_list:
                print(item)
            break
            
    if not status:
        print("Can't find the item!")
        continue

for item in shopping_list:
    total += item["price"]

for final_item in shopping_list:
    print(final_item)

print(f"total: {total}")