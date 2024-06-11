shoppingList = ["milk", "banana", "suger", "bread", "coffee"]
buddyList = ["chocolate chip", "oatmeal raisin"]
def menu():
    print("Main Menu".center(50, "*"))
    menuText = """
    1 -> Add Item 
    2 -> Remove Item
    3 -> Print List 
    4 -> Add Roommate's List 
    5 -> Move item to top
    6 -> Find item
    7 -> Arrange in Ascending Order
    8 -> Arrange in Decending Order
    9 -> Empty Shopping List
    0 -> Exit: """
    choice = int(input(menuText))
    if choice == 1:
        addItem()
    elif choice == 2:
        removeItem()
    elif choice == 3:
        printList()
    elif choice == 4:
        addList()
    elif choice == 5:
        moveToTop()
    elif choice == 6:
        findItem()
    elif choice == 7:
        sortList()
    elif choice == 8:
        reverseList()
    elif choice == 9:
        emptyList()
    elif choice ==0:
        quit()
    else:
        print("Invalid Choice. Try Again...")
        menu()
def addItem():
    item = input("Enter item name to add: ")
    shoppingList.append(item)
    print(f"{item} added in the list. New list is\n{shoppingList}")
    menu()
def removeItem():
    item = input("Enter item name to add: ")
    shoppingList.remove(item)
    print(f"{item} removed from the list. New list is\n{shoppingList}")
    menu()
def addList(list = buddyList):
    for item in list:
        shoppingList.append(item)
    printList()
    menu()
def printList():
    if len(shoppingList) != 0:
        print(f"Total {len(shoppingList)} items in the list.")
        print(shoppingList)
    else:
        print("Your shopping list is empty right now. Please add some items")
    menu()
def findItem():
    item = input("Enter item to find in list: ")
    itemCount = shoppingList.count(item)
    if itemCount > 0:
        itemIndex = shoppingList.index(item)
        print(f"{item} is at position {itemIndex}")
        printList()
        menu()
    else:
        print(f"{item} not in the list")
        printList()
        menu()
def sortList():
    shoppingList.sort()
    printList()
    menu()
def reverseList():
    shoppingList.sort(reverse=True)
    printList()
    menu()
def emptyList():
    shoppingList.clear()
    print('Thanks for shopping with me..')
    print(shoppingList)
    shortMenu()
def moveToTop():
    item = input("Enter item to move to top: ")
    itemCount = shoppingList.count(item)
    if itemCount > 0:
        shoppingList.remove(item)
        shoppingList.insert(0, item)
        print(f"{item} moved to top of the list. New list is\n{shoppingList}")
        menu()
    else:
        print("item not in the list")
        menu()
def shortMenu():
    print("Welcome to Shopping List Maker".center(50, "*"))
    menuText = """
    1 -> Main Menu 
    2 -> Exit """
    choice = int(input(menuText))
    if choice == 1:
        menu()
    else:
        print('See you later. Goodbye!!')
        quit()

shortMenu()
