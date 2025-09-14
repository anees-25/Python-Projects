def show_menu():
    # Display menu options to the user
    print("--- Shopping List Manager --- \n1. Add an item\n2. Remove an Item\n3. View list\n4. Exit program")
   
def shopping_list_manager():
    shopping_list = []  # Empty list to store shopping items

    while True:  # Keep running until user chooses to exit
        show_menu()  # Show menu each time
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Add item
            item = input("Enter item to add: ")
            shopping_list.append(item)  # Append item to list
            print(f"'{item}' added to the list.")

        elif choice == "2":
            # Remove item
            item = input("Enter item to remove: ")
            if item in shopping_list:  # Check if item exists in list
                shopping_list.remove(item)
                print(f"🗑️ '{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == "3":
            # View list
            if not shopping_list:  # If list is empty
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == "4":
            # Exit program
            print("Exiting Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")

# Run the shopping list manager
shopping_list_manager()


# def show_menu():
#     
# def shopping_list_manager():
#     shopping_list = []
#     while True:
#         show_menu()
#         choice = input("Enter your choice (1-4): ")
#         if choice == "1":
#             item = input("Enter item to add: ")
#             shopping_list.append(item)
#             print(f" {item} added to the list.")
#         elif choice == "2":
#             item = input("Enter item to remove: ")
#             if item in shopping_list:
#                 shopping_list.remove(item)
#                 print(f"{item} removed from the list. ")
#             else:
#                 print(f"{item} not found in the list. ")
#         elif choice == "3":
#             if not shopping_list:
#                 print("your shopping list is empty. ")
#             else:
#                 print("\n Your Shopping List: ")
#                 for i, item in enumerate(shopping_list, start = 1):
#                     print(f"{i}. {item}")
#         elif choice == "4":
#             print("Exiting Shopping List Manager. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter 1-4.")
# shopping_list_manager()