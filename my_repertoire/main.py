# Defining constants
SEE_REPERTOIRE_OPTION = "1"
ADD_PIECE_OPTION = "2"
DELETE_PIECE_OPTION = "3"
EXIT_OPTION = "4"

list_of_options = ["See Repertoire.", "Add Piece.",
                   "Delete Piece.", "Exit"]


# Method to print the screen
def clear_screen():
    for x in range(100):
        print()


# Method to print the title of the app
def print_title():
    print("-------------------- Repertoire Manager --------------------")
    print()


# Method to print the menu
def print_menu():
    for x in range(len(list_of_options)):
        print("{}. {}".format(x+1, list_of_options[x]))
    print()


if __name__ == "__main__":
    master_loop = True

    while master_loop:
        clear_screen()

        print_title()
        print_menu()

        users_option = input("Choose an option: ")

        if users_option == SEE_REPERTOIRE_OPTION:
            print()
        elif users_option == ADD_PIECE_OPTION:
            print()
        elif users_option == DELETE_PIECE_OPTION:
            print()
        elif users_option == EXIT_OPTION:
            master_loop = False
        else:
            print("Sorry, you did not choose a correct option :(")
            input("But don't worry please press enter to continue...")

    print("Thank you for using Repertoire Manager")
    input("Press enter to continue...")