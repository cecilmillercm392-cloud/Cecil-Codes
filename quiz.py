products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}


for product,  item  in products.items():
    products[product]  = round(item * 0.8)

print(products)

for product in enumerate(products):
    print(product)

for index, product in enumerate(products.items(), 1):
    print(index, product)

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}
print(my_set & your_set)


print(my_set.issubset(your_set))
print(your_set.issubset(my_set))