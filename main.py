import datetime
import sys

# welcome to the store message
print(f"{'-' * 100}\n{' ' * 35}WELCOME TO ABC ENTREPRISES\n{'-' * 100}\n")
print("Kamal Pokhari, kathmandu, Nepal \t\t\t\t\t\t\t\t\t\t\t Phone: +977 9821526347")


# user input function for sale and buy
# update stock function,2 for sales and buy
# invoice generation function
# define the function of buying section
def display():
    file = open("stock.txt", "r")
    print(f"{'=' * 100}\n{' ' * 35}ABC ENTERPRISES STOCK\n{'=' * 100}\n")
    temp = []

    for line in file:
        line = line.replace("\n", '')
        temp.append(line.split(","))

    print("Name" + (" " * 15) + "|Brand" + (" " * 12) + "|Price" + (" " * 11) + "|Quantity" + (
            " " * 9) + "|Processor" + (" " * 7) + "|Graphic Card")
    print("=" * 100)

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            space: int = 18 - len(temp[i][j])
            print(temp[i][j] + (space * ' '), end="")
        print("\n")
        print("-" * 100)
    file.close()
    print("=" * 100)
    print(temp)
    return temp


# defining the function of selling section
def order():
    temp = display()
    price = 0
    order1 = input("what would u like to order? ").lower()
    quantity = int(input("Ënter the quantity: "))
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if order1 == temp[i][0].lower():
                temp[i][3] = str(int(temp[i][3]) + quantity)
                price = int(temp[i][2]) * quantity

            break

    with open("stock.txt", "w") as file:
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                file.write(temp[i][j])
                if j != 5:
                    file.write(", ")
            file.write("\n")

    return price

def sell():
    display()
    with open('stock.txt', 'r') as file:
        lines = file.readlines()


# taking among 2 input from the user
option = input("Do you want to order/sell laptop? ").lower()
if option == "order":
    priceValue = order()
    print(priceValue)
elif option == "sell":
    # option for selling the laptop
    sell()

else:
    # if except of buy/sell other input is taken.
    print("Sorry Admin! Option not available!")

