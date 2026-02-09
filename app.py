item = [{
    "name": "ASUS TUF Gaming Radeon RX 9070 XT OC Edition 16GB GDDR6",
    "price": 849.99,
    "department": "Electronics",
    "description": "A GPU"
},
{
    "name": "AMD Ryzen 7 9850X3D Desktop Processor",
    "price": 499.99,
    "department": "Electronics",
    "description": "A cpu",
},
{
    "name": "ASUS X870E-E ROG Strix Gaming R2 USBC WiFi",
    "price": 349.99,
    "department": "Electronics",
    "decription": "A Motherboard",
},
{
    "name": "CORSAIR - DOMINATOR TITANIUM 64GB (2 x 32GB) DDR5 6000",
    "price": 1182.99,
    "department": "Electronics",
    "decription": "Some Expensive Ram",
},
{
    "name": "Be Quiet! Dark Power 13 1000W ATX 3.0 80 Plus Titanium Efficiency Modular Power Supply",
    "price": 259.99,
    "department": "Electronics",
    "decription": "A PSU",
},



]
for index, part in enumerate(item):
    print(index, ":", part["name"])