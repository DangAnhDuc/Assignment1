# Name: Dang Anh Duc
# Submit day: 24/4/2017
# Brief program details:My python file is coded for assignment 1. In this file, with each choice of user the program will
#  proceed into each function.In each function,information of items from items.csv file will be loaded and then put into
#  many list. Based on 3 main type of list (name, price,priority) and the last component to know which item is requrire
# or completed, we can run the program more eassy. Finally, after each function finish, the information will be write
# again to items.csv file to be used in next user's choice
# Link to Github: https://github.com/DangAnhDuc/Assignment1
from operator import itemgetter
#display welcome message with name
print("""Welcome to shopping List 1.0 by Dang Anh Duc
3 items loaded from items.csv""")
def main():
    #call load_item function
    list_required_items=load_item()
    #arrange list_required_items in order by comparing priority
    list_required_items.sort(key=itemgetter(2))
    #create empty list_completed_items
    list_completed_items = []
    while True:
        try:
            #call get_user_input function to display the menu and get menu choice
            user_input = get_user_input()
            # check user_input with infinite loop and try/except code to proceed to next fucntion
            while user_input.upper() != "R" and user_input.upper() != "C" and user_input.upper() != "A" \
                    and user_input.upper() != "M" and user_input.upper() != "Q":
                print("This is not a valid input!")
                user_input = get_user_input()
            else:
                #user_input.upper()="R" is true
                if user_input.upper() == "R":
                    #display message when list_required_items is empty
                    if len(list_required_items) == 0:
                        print("No required items")
                    #call print_items function to display required items from list_required_items
                    else:
                        print("Required items:")
                        print_items(list_required_items)
                #user_input.upper()="C" is true
                elif user_input.upper() == "C":
                    # display message when list_completed_items is empty
                    if len(list_completed_items) == 0:
                        print("No completed items")
                    #call print_items function to display completed items from list_completed_items
                    else:
                        print("Completed items:")
                        print_items(list_completed_items)
                #user_input.upper()="A" is true
                elif user_input.upper() == "A":
                    new_items=[]
                    input_product = str(input("Enter name of item:"))
                    # Error-check user inputs for the product name
                    while input_product == "":
                        print("Input can not be blank")
                        input_product = str(input("Enter a valid name:"))
                    else:
                        pass
                    valid_price = False
                    # Error-check user inputs for the price
                    while not valid_price:
                        try:
                            input_price = float(input("Enter price of item::"))
                            while input_price <= 0:
                                print("This is invalid price!")
                                input_price = float(input("Enter price of item:"))
                            # return valid_price=True to end the error-checking loop
                            valid_price = True
                        except ValueError:
                            print("Please enter a valid number!")
                    valid_priority = False
                    # Error-check user inputs for the priority
                    while not valid_priority:
                        try:
                            input_priority = int(input("Enter priority of item:"))
                            while input_priority not in range(1, 4):
                                print("Priority must be 1, 2 or 3")
                                input_priority = int(input("Enter a valid number:"))
                            #return valid_priority=True to end the error-checking loop
                            valid_priority = True
                        except ValueError:
                            print("Please enter a valid number!")
                    #print the item have been added to the required list
                    print("{}, ${:.2f} (priority {}) added to shopping list".format(input_product, input_price,
                                                                                    input_priority))
                    #add each information of new item to the list
                    new_items.append(input_product)
                    new_items.append(str(input_price))
                    new_items.append(str(input_priority))
                    new_items.append('r')
                    #add new_items to list_required_items
                    list_required_items.append(new_items)
                #user_input.upper()="M" is true
                elif user_input.upper() == "M":
                    #display message when list_required_items is empty
                    if len(list_required_items) == 0:
                        print("No required items")
                    #call complete_an_item to mark an item as completed
                    else:
                        complete_an_item(list_completed_items, list_required_items)
                #user_input.upper()="Q" is true
                else:
                    #quit the program after display goodbye mesage
                    print("{} items saved to items.csv".format(len(list_required_items)+len(list_completed_items)))
                    print("Have a nice day :)")
                    break
        except ValueError:
            #display error mesage when user_input is wrong type of variable
            print("This is not a valid input!")

# PESUDOCODE
# open items.csv file
# read data from file through each line and put in into product_data list(1 line is 1 element of list)
# closed items.csv file
# create new_product_data list
# for each element in product_data list
    # splitdata=each.strip().split(",")
    # new_product_data.append(split_data)
# return new_product_data to main function to use
def load_item():
    product_file = open("items.csv")
    product_data = product_file.readlines() #read each line in items.csv file
    product_file.close()
    new_product_data = [] #list of information of each item
    for each in product_data:
        split_data = each.strip().split(",") #remove space in each line and divide name,price and
        new_product_data.append(split_data)
    return  new_product_data
def get_user_input():
    #display program menu
    print("""Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit
""")
    #get choice from user and return to main function
    user_choice = str(input("Enter your choice:"))
    return user_choice
#PSEUDPCODE
#display the list_required_items by using print_items function
#valid_items_mark=False
#while not valid_item_mark
    #try:
        #item_number=int(input("Enter the number of an item to mark as completed:"))
        #while item_number not in range(0,len(list_required_items)):
            #display error message
            #ask to input item_number again
            # return valid_items=True to end the error checking loop
#except ValueError:
    #display error message
    #display item have been mark as completed
    #for i in range(len(list_required_items)):
    #     replace list_required_items[item_number][3] = 'c'
    # list_completed_items.append(list_required_items[item_number])
    # list_required_items.remove(list_required_items[item_number])
    # output_file = open("items.csv", "w")
    # for each in list_required_items:
    #     output_file.write("{},{},{},{}\n".format(each[0], each[1], each[2], each[3]))
    # closed output_file
    # output_file = open("items.csv", "a")
    # for each in list_completed_items:
    #     output_file.write("{},{},{},{}\n".format(each[0], each[1], each[2], each[3]))
    # closed output_file
def complete_an_item(list_completed_items, list_required_items):  # do the mark an item as completed
    # feature
    # print the list_required_items for user to choose
    print_items(list_required_items)
    valid_item_mark = False
    # Error-check user inputs for the sequence number of item
    while not valid_item_mark:
        try:
            #get the number of item user want to mark as completed
            item_number = int(input("Enter the number of an item to mark as completed:"))
            while item_number not in range(0, len(list_required_items)):
                print("Invalid item number")
                item_number = int(input("Enter the number of an item to mark as completed:"))
            #return valid_items=True to end the error checking loop
            valid_item_mark = True
        except ValueError:
            print("Invalid input; enter a number")
    #display item which have been marked as completed
    print("{} marked as completed".format(list_required_items[item_number][0]))
    for i in range(len(list_required_items)):  # change the item from list_required_items to list_completed_items
        list_required_items[item_number][3] = 'c' #change the situation of items from "r" to "c"
    list_completed_items.append(list_required_items[item_number]) #add item to list_completed_items
    list_required_items.remove(list_required_items[item_number])  #remove item out of list_required_items

    output_file = open("items.csv", "w")  # clear the information and rewrite to the file
    for each in list_required_items:
        output_file.write("{},{},{},{}\n".format(each[0], each[1], each[2], each[3]))
    output_file.close()
    output_file = open("items.csv", "a") #open file and add the completed items
    for each in list_completed_items:
        output_file.write("{},{},{},{}\n".format(each[0], each[1], each[2], each[3]))
    output_file.close()
def print_items(list_items):  # print the list of items as the sample output with name, price and priority
    list_items.sort(key=itemgetter(2))  # sort the list by priority
    item_names = []  # list of item's names
    item_prices = []  # list of item's prices
    priority_items = []  # list of item's priorities

    for each in list_items:
        item_names.append(each[0])
        item_prices.append(float(each[1])) #change the format of value of price to put it to item_price list
        priority_items.append(each[2])
    for i in range(0, len(list_items)):
        print("{}. {:20} $  {:5} ({})".format(i, item_names[i], item_prices[i], priority_items[i]))
    print("Total expected price for {} items: ${:.2f}".format(len(list_items), sum(item_prices)))

main()