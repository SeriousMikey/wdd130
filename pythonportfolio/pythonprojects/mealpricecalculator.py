print("Hi, welcome to Chili's!")
print("I'm kinda bad at remembering the prices, so you'll need to tell me. Sorry in advance.")
childs_meal = float(input("Do you know what the price of a children's meal is? "))
adults_meal = float(input("And how much is an adult's meal? "))
print('Good, good...')
num_child = int(input("Now, how many children are there? "))
num_adult = int(input("And how many adults are there? "))
print("Thanks that helps a lot!")
print('')
sales_tax = float(input("Sorry, it looks like the computers are broken somehow... Do you happen to know the sales tax rate? "))
meal_subtotal = (childs_meal * num_child) + (adults_meal * num_adult)
meal_tax = float(meal_subtotal * (sales_tax / 100))
print("Alright, I got your check ready for ya! Here you go! ")
print('')
print(f'Subtotal: ${meal_subtotal:.2f}')
print(f'Sales Tax: ${meal_tax:.2f}')
tip = float(input('Tip: $'))
total = float(meal_subtotal + meal_tax + tip)
print(f"Total: ${total:.2f}")
print('')
print("Since the computers are broken, we can only take payment in cash. Sorry! ")
payment = float(input('How much will you be giving me? '))
change = payment - total
print('')
print(f'Alright, your change comes out to ${change:.2f}')
print("Have a nice day!")