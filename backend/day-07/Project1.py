my_list = []
def menu():
    print("""Options:
        1. Add item to the shopping list
        2. View shopping list
        3. Remove item from the shopping list
        4. Quit""")
    
def option1():
    global my_list
    item = input("Enter the item you want to add: ")
    my_list.append(item)
    return (f"{item} has been added to your shopping list. \n")

def option2():
    global my_list
    result = "Your shopping list:\n"
    for item in my_list:
        result += f"{item}\n"
    return result
    

def option3():
    item = input("Enter the item you want to remove: ")
    if item in my_list:
        my_list.remove(item)
        return f"{item} has been removed from your shopping list."
    else:
        return f"{item} is not in your shopping list."

def option4():
    return "Goodbye!"

def system():
    

    switch = {
    1: option1,
    2: option2,
    3: option3,
    4: option4
}
    while True:
        menu()
        choice = int(input("Enter the number of your choice: "))
        if choice in switch:
            result = switch[choice]()
            print(result)
            if choice == 4:
                break
        else:
            print("Invalid")


def main():
    system()





if __name__ == "__main__":
    main()