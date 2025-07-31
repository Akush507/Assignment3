records = [
    {'name': "rice", 'price': 120, 'category': "grocery"},
    {'name': "sugar", 'price': 220, 'category': "grocery"},
    {'name': "wheat", 'price': 320, 'category': "grocery"},
    {'name': "cereal", 'price': 420, 'category': "grocery"},
]
with open("grocery.txt", "w") as file:
    file.write("ID\tNAME\tPRICE\tCATEGORY\n")  # Write header
    idx = 1
    for record in records:
        file.write(f"{idx}\t{record['name']}\t{record['price']}\t{record['category']}\n")
        idx += 1

print("Reading from grocery.txt:")
with open("grocery.txt", "r") as file:
    contents = file.read()
    print(contents)
