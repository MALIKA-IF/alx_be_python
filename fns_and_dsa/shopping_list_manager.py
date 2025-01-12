shopping_list=["A","B","C","D"]

def add_items(x):
  shopping_list.append(x)
 
def display_list():
    for x in shopping_list:     
        print(x)

def remove_list(item):
    for x in shopping_list: 
        while x==item:
          shopping_list.remove(item)
          break
       

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice=int(input("Enter your choice: "))

        if choice == '1':
            # Prompt for and add an item
            x=input("enter your Items ")
            add_items(x)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            y=input("enter your Items ")
            remove_list(y)
            pass
        elif choice == '3':
            # Display the shopping list
            display_list()
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
