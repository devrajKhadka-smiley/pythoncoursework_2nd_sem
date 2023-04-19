import datetime

x = datetime.datetime.now()

# welcome to the store message
print(f"{'-' * 100}\n{' ' * 35}WELCOME TO ABC ENTREPRISES\n{'-' * 100}\n")
print("Kamal Pokhari, kathmandu, Nepal \t\t\t\t\t\t\t\t\t\t\t Phone: +977 9821526347")
print(f"{'-' * 100}\n{' ' * 35}Have a Great Day ! Admin\n{'-' * 100}\n")

print("\t\t Type 'Order' to order the laptop from the manufacturer!")
print("\t\t Type 'Sell' to sell the laptop from our stock.")
print("Type '3' to exit the system")


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
    return temp


# defining the function of selling section
def order():
    temp = display()
    price = 0
    c = 0
    order1 = input("what would u like to order? ").lower()
    quantity = int(input("Enter the quantity: "))
    while quantity <= 0:
        print("Enter a valid quantity")
        quantity = int(input("Enter the number of laptops you want to sell"))

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if order1 == temp[i][0].lower():
                temp[i][3] = str(int(temp[i][3]) + quantity)
                price = int(temp[i][2]) * quantity
                c = 1
            break
    if c == 0:
        print("item is not available")

    with open("stock.txt", "w") as file:
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                file.write(temp[i][j])
                if j != 5:
                    file.write(",")
            file.write("\n")
    return price


def sell():
    price = 0
    c = 0
    temp = display()
    order1 = input("What would you like to sell?:   ").lower()
    brand_name = input("name of the laptop brand").lower()
    customer_name = input("enter the name of the customer").capitalize()

    # quantity = int(input("How many laptop you want to sell? "))
    while True:
        try:
            quantity = int(input("How many laptop you want to sell? "))
        except ValueError:
            print("Only numbering value is available")
        else:
            if quantity <= 0:
                print("Enter a valid quantity")
            else:
                break

    for i in range(len(temp)):
        # for j in range(len(temp[i])):
        if order1 == temp[i][0].lower():
            temp[i][3] = str(int(temp[i][3]) - quantity)
            price = int(temp[i][2].replace("$", "")) * quantity
            c = 1
            sales_invoice(order1, brand_name, customer_name, quantity)
            break
    if c == 0:
        print("item is not available")

    with open("stock.txt", "w") as file:
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                file.write(temp[i][j])
                if j != 5:
                    file.write(",")
            file.write("\n")
    return order1, brand_name, customer_name, quantity


def sales_invoice(order1, brand_name, customer_name, quantity):
    date = x.strftime("%Y-%m-%d")
    time = x.strftime("%H-%M-%S")
    _ = open(f"sell_invoice({date}{time}).txt", 'x')

    with open(f"sell_Invoice({date}{time}).txt", 'w') as file:
        file.write(f"{'=' * 35}\n")
        file.write(f"\t\t\t\t\t SAlES INVOICE\n")
        file.write(f"\t\tABC ENTERPRISES\n")
        file.write(f"\t\t\t\tDate: {date}\n")
        file.write(f"\t\t\t\tTime:{time}\n")
        file.write(f"{'=' * 35}\n")

        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Laptop Name: {order1} \n")
        file.write(f"Brand Name: {brand_name}\n")
        file.write(f"quantity: {quantity}\n")
        file.write(f"{'=' * 35}\n")

        file.write("Total Amount : \n")
        file.write("Vat Amount: \n")
        file.write("Shipping Amount: \n")
        file.write(f"{'=' * 35}\n")

        file.write("Total Amount: \n")

        file.write(f"{'=' * 35}\n")
        file.write(f"\t\t\tThank You\n")
        file.write(f"{'=' * 35}\n")
        # ===========================================================================
        print(f"=" * 35)
        print(f"\t\t\t\t\t SAlES INVOICE")
        print(f"\t\tABC ENTERPRISES")
        print(f"\t\t\t\tDate: ", date)
        print(f"\t\t\t\tTime: ", time)
        print(f"=" * 35)

        print(f"Customer Name: {customer_name} ")
        print(f"Laptop Name: {order1} ")
        print(f"Brand Name: {brand_name} ")
        print(f"quantity: {quantity}")
        print(f"=" * 35)

        print("Total Amount : ")
        print("Vat Amount: ")
        print("Shipping Amount: ")
        print(f"=" * 35)

        print("Total Amount: ")

        print(f"{'=' * 35}\n")
        print(f"\t\t\tThank You!")
        print(f"{'=' * 35}\n")


# taking among 2 input from the user
continue_loop = True
while continue_loop:
    priceValue = 0
    option = input("Do you want to order/sell laptop? ").lower()

    if option == "order":
        priceValue = order()
        print(priceValue)

    elif option == "sell":
        # option for selling the laptop
        sell()

    else:
        # if except of buy/sell other input is taken.
        if option == "3":
            quit()
        else:
            print("Sorry Admin! Option not available!")

    ch = input("Do you want to continue(yes/no)?").lower()
    if ch == "no":
        continue_loop = False

    priceValue, order1, brand_name, customer_name, quantity = sell()
    sales_invoice(order1, brand_name, customer_name, quantity, priceValue)
