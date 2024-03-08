add1=0
print("Welcome to Sree Ram store")
while True:
    user_price=input("Enter the price:")
    if user_price != "q":
        add1=(add1+int(user_price))
    else:
        print("Total price of items:",add1)
        break

print("\n Thank you for Shopping ")         



