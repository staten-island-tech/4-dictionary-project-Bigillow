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
{
    "name": "Hyte Y70 Infinite Touch Case",
    "price": 299.99,
    "department": "Electronics",
    "description": "A PC case with touch features"
},
{
    "name": "Lian Li HydroShift 360",
    "price": 229.99,
    "department": "Electronics",
    "description": "A 360mm liquid cooling radiator"
},
{
    "name": "Lian Li Uni FAN SL-Infinity Case Fan",
    "price": 39.99,
    "department": "Electronics",
    "description": "A customizable case fan"
},
{
    "name": "1TB SSD 990 PRO",
    "price": 99.99,
    "department": "Electronics",
    "description": "High-performance NVMe SSD"
},
{
    "name": "2TB SSD 990 PRO",
    "price": 189.99,
    "department": "Electronics",
    "description": "High-capacity NVMe SSD"
},
{
    "name": "3TB SSD 990 PRO",
    "price": 289.99,
    "department": "Electronics",
    "description": "Large capacity NVMe SSD"
},
{
    "name": "4TB SSD 990 PRO",
    "price": 399.99,
    "department": "Electronics",
    "description": "Extra large NVMe SSD"
},
{
    "name": "Corsair Vengeance LPX 32GB (2 x 16GB) DDR4 3200",
    "price": 149.99,
    "department": "Electronics",
    "description": "High-performance DDR4 RAM"
},
{
    "name": "Samsung 980 PRO 2TB NVMe SSD",
    "price": 229.99,
    "department": "Electronics",
    "description": "Fast NVMe SSD for gaming and editing"
},
{
    "name": "ASUS ROG Strix B550-F Gaming (Wi-Fi 6)",
    "price": 179.99,
    "department": "Electronics",
    "description": "Motherboard with Wi-Fi 6 and PCIe 4.0"
},
{
    "name": "Noctua NH-U12S chromax. black CPU Cooler",
    "price": 79.99,
    "department": "Electronics",
    "description": "High-performance air CPU cooler"
},
{
    "name": "WD Black 6TB External Hard Drive",
    "price": 159.99,
    "department": "Electronics",
    "description": "Large external storage"
},
{
    "name": "SteelSeries Apex Pro Mechanical Gaming Keyboard",
    "price": 199.99,
    "department": "Electronics",
    "description": "Mechanical keyboard with adjustable actuation"
},
{
    "name": "Logitech G502 Lightspeed Wireless Mouse",
    "price": 129.99,
    "department": "Electronics",
    "description": "Wireless gaming mouse"
},
{
    "name": "AOC CQ32G1 Curved Gaming Monitor 32\"",
    "price": 349.99,
    "department": "Electronics",
    "description": "QHD curved gaming display"
},


]

# for index, part in enumerate(item):
#     print(index, ":", part["name"])
# item_number = int(input("What item do you want?"))
# print("You purchased " + str(item[item_number]["name"]) + " for $" + str(item[item_number]["price"]) + " in the " + str(item[item_number]["department"]) + " department ")
# print("Product discription: " + str(item[item_number]["description"]))

cart = []
bill = 0
while True:
    for index, part in enumerate(item):
        print(index, ":", part["name"])
    item_number = int(input("What item do you want?"))
