#Name: Dang Anh Duc
#Submit day: 24/4/2017
#Brief program details:
#Link to Github:
from operator import itemgetter
print("""Shopping List 1.0
3 items loaded from items.csv""")
def main():
    while True:
        try:
            user_input=get_user_input()
            while user_input!="R" and user_input!="C" and user_input!="A" \
                    and user_input!="M" and user_input!="Q":
                print("This is not a valid input!")
                user_input=get_user_input()
            else:
                if user_input=="R":
                    user_enter_r()
                elif user_input=="C":
                    user_enter_c()
                elif user_input=="A":
                    user_enter_a()
                elif user_input=="M":
                    user_enter_m()
                else:
                    user_enter_q()
                    break
        except ValueError:
            print("This is not a valid input!")

def get_user_input():
    print("""Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit
""")
    enter=str(input("Enter your choice:"))
    return enter

def load_items():
    product_file = open("items.csv")
    product_data = product_file.readlines()
    product_file.close()
    new_product_data = []
    for each in product_data:
        split_data = each.strip().split(",")
        new_product_data.append(split_data)
        new_product_data.sort(key=itemgetter(2))
    return new_product_data
def user_enter_r():
    product_list = []
    price_list = []
    priority_list = []
    product_data_list=load_items()
    for each in product_data_list:
        if each[3] == "r":
            product_list.append(each[0])
            price_list.append(each[1])
            priority_list.append(each[2])
        else:
            pass
    total_price = [float(value) for value in price_list]
    if len(product_list)==0:
        print("No required items")
    else:
        for each in range(len(product_list)):
            print("{}. {:20} $  {:5} ({})".format(each, product_list[each], price_list[each], priority_list[each]))
        print("Total expected price for {} items: ${}".format(len(product_list), sum(total_price)))

def user_enter_c():
    product_list = []
    price_list = []
    priority_list = []
    product_data_list = load_items()
    for each in product_data_list:
        if each[3] == "c":
            product_list.append(each[0])
            price_list.append(each[1])
            priority_list.append(each[2])
        else:
            pass
    total_price = [float(value) for value in price_list]
    if len(product_list)==0:
        print("No completed items")
    else:
        for each in range(len(product_list)):
            print("{}. {:20} $  {:5} ({})".format(each, product_list[each], price_list[each], priority_list[each]))
        print("Total expected price for {} items: ${}".format(len(product_list), sum(total_price)))

def user_enter_a():
    product=str(input("Enter name of item:"))
    while product=="":
        print("Input can not be blank")
        product=str(input("Enter a valid name:"))
    else:
        pass
    valid_price=False
    while not valid_price:
        try:
            price = float(input("Enter price of item::"))
            while price<=0:
                print("This is invalid price!")
                price = float(input("Enter price of item:"))
            valid_price=True
        except ValueError:
            print("Please enter a valid number!")
    valid_priority=False
    while not valid_priority:
        try:
            priority = int(input("Enter priority of item:"))
            while priority not in range(1,4):
                print("Priority must be 1, 2 or 3")
                priority = int(input("Enter a valid number:"))
            valid_priority=True
        except  ValueError:
            print("Please enter a valid number!")
    product_file = open("items.csv", "a")
    product_file.write("{},{},{},r\n".format(product,price,priority))
    product_file.close()

def user_enter_m():
    product_list = []
    price_list = []
    priority_list = []
    item_name_completed = []
    item_price_completed = []
    item_priority_completed = []
    product_data_list = load_items()
    for each in product_data_list:
        if each[3] == "r":
            product_list.append(each[0])
            price_list.append(each[1])
            priority_list.append(each[2])
        else:
            item_name_completed.append(each[0])
            item_price_completed.append(each[1])
            item_priority_completed.append(each[2])
    total_price = [float(value) for value in price_list]
    if len(product_list)==0:
        print("No required items")
    else:
        for each in range(len(product_list)):
            print("{}. {:20} $  {:5} ({})".format(each, product_list[each], price_list[each], priority_list[each]))
        print("Total expected price for {} items: ${}".format(len(product_list), sum(total_price)))
        valid_item_mark=False
        while not valid_item_mark:
            try:
                item_mark = int(input("Enter the number of an item to mark as completed:"))
                while item_mark >= len(product_list):
                    print("Invalid input! Please enter a valid number")
                    item_mark = int(input("Enter the number of an item to mark as completed:"))
                else:
                    product_file = open("items.csv", "w+")
                    if len(item_name_completed)==0:
                        pass
                    else:
                        for i in range(len(item_name_completed)):
                            product_file.write("{},{},{},c\n".format(item_name_completed[i], item_price_completed[i],
                                                             item_priority_completed[i]))
                    for i in range(len(product_list)):
                        if i!=item_mark:
                            product_file.write("{},{},{},r\n".format(product_list[i], price_list[i], priority_list[i]))
                        else:
                            product_file.write("{},{},{},c\n".format(product_list[i], price_list[i], priority_list[i]))
                    product_file.close()
                valid_item_mark=True
            except ValueError:
                print("Please enter a valid number")

def user_enter_q():
    print("""4 items saved to items.csv
Have a nice day :)
""")

main()