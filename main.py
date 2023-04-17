import datetime

# welcome to the store message
print(f"{'-' * 100}\n{' ' * 35}WELCOME TO ABC ENTREPRISES\n{'-' * 100}\n")
print("Kamal Pokhari, kathmandu, Nepal \t\t\t\t\t\t\t\t\t\t\t Phone: +977 9821526347")


# define the function of buying section
def display():
    file = open("stock.txt", "r")
    print(f"{'=' * 100}\n{' ' * 35}ABC ENTERPRISES STOCK\n{'=' * 100}\n")
    temp = []

    for line in file:
        line = line.replace("\n", '')
        temp.append(line.split(","))

    print("Name" + (" " * 15) + "|Brand" + (" " * 12) + "|Price" + (" " * 13) + "|Quantity" + (
            " " * 10) + "|Processor" + (" " * 9) + "|Graphic Card")
    print("=" * 100)

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            space: int = 18 - len(temp[i][j])
            print(temp[i][j] + (space * ' '), end="")
        print("\n")
        print("-" * 100)
    file.close()
    print("=" * 100)


# defining the function of selling section
def sell():
    display()
    with open('laptops.txt', 'r') as file:
        lines = file.readlines()
        laptops = [line.strip().split(',') for line in lines]
    distributor_name = input("Enter your name:").capitalize()
    laptop_name = input("Enter name of laptop:").lower()
    brand_name = input("Enter brand name of laptop:").lower()
    quantity = int(input("Enter Quantity:"))


# defining the function of selling section
def buy():
    # buy_laptop = input("Which laptop would you like to buy?").lower()
    with open('stock.txt', 'r') as file:
        lines = file.readlines()
        laptops = [line.strip().split(',') for line in lines]

    laptop_name = input("Enter name of laptop:").lower()
    brand_name = input("Enter brand name of laptop:").lower()
    customer_name = input("Enter your name:").capitalize()
    quantity = int(input("Enter Quantity:"))


# taking among 2 input from the user
option = input("Do you want to buy/sell laptop? ").lower()
if option == "buy":
    buy()

elif option == "sell":
    # option for selling the laptop
    sell()

else:
    # if except of buy/sell other input is taken.
    print("Service not available!")
