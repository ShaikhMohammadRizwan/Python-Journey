# CAFE MANAGEMENT SYSTEM

# Define the Menu of Cafe

menu = {
    'Pizza': 130,
    'Pasta': 140,
    'Burger': 150,
    'Noodles': 160,
    'Boil Egg': 20,
    'Egg Fry': 100,
    'Shake': 50,
    'Water Bottel': 20,
    'Coffee': 30,
    'Tea': 25,
    'Black Tea': 50,
    'Milkshake': 70,
    'Smoothie': 90,
    'Cookies': 10,
    'Chocolate Cake': 150,
    'Ice Cream': 50,
    'Greek Salad': 100,
    'Fruit Salad': 80,
    'Papaya Salad': 70,
    'Mixed Salad': 120,
    'Hot Milk': 30,
    'Lassi': 30,
    'Tea Latte': 60,
    'Cappuccino': 80,
    'Hot Chocolate': 70,
    'Mojito': 80,
    'Iced Tea': 40,
    'Brownie': 100,
    'Muffin': 80,
    'Donut': 50,
    'Pancake': 70,
    'French Fries': 100,
    'Fried Chicken': 120,
    'Grilled Beef': 150,
    'Sushi': 180,
    'Tacos': 150,
}

# Greet 

print('Welcome to the Cafe Restaurant')

# Show the Menu
print("Pizza: 130\nPasta: 140\nBurger: 150\nNoodles: 160\nBoil Egg: 20\nEgg Fry: 100\nShake: 50\nWater Bottel: 20\nCoffee: 30\nTea: 25\nBlack Tea: 50\nMilkshake: 70\nSmoothie: 90\nCookies: 10\nChocolate Cake: 150\nIce Cream: 50\nGreek Salad: 100\nFruit Salad: 80\nPapaya Salad: 70\nMixed Salad: 120\nHot Milk: 30\nLassi: 30\nTea Latte: 60\nCappuccino: 80\nHot Chocolate: 70\nMojito: 80\nIced Tea: 40\nBrownie: 100\nMuffin: 80\nDonut: 50\nPancake: 70\nFrench Fries: 100\nFried Chicken: 120\nGrilled Beef: 150\nSushi: 180\nTacos: 150")

# Order Total Amount

order_total = 0
 
item_1 = input('Enter the name of item you want to order = ')

if item_1 in menu:
    order_total += menu[item_1]
    print(f'Your item {item_1} has been added to your order')

else:
    print(f'Ordered item {item_1} is not avaliable')

another_order = input('Do you want to add another item? (Yes/No): ')

if another_order == 'Yes':
    item_2 = input('Enter the name of item you want to order = ')
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'Item {item_2} has been added to order')
    else:
        print(f'Ordered item {item_2} is not available')

print(f'The total amout of item to pay is {order_total}')