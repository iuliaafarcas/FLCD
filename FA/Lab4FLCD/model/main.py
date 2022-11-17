from model.FiniteAutomata import FiniteAutomata

if __name__ == '__main__':
    def print_menu():
        print("1.Print set of states")
        print("2.Print alphabet")
        print("3.Print transitions")
        print("4.Print initial state")
        print("5.Print final states")
        print("6.Check if string is accepted ")


    while True:
        fa = FiniteAutomata()
        fa.readFromFile()
        print_menu()
        option = input("Choose option: ")
        if option == "1":
            print(fa.writeStates())
        elif option == "2":
            print(fa.writeAlphabet())
        elif option == "3":
            print(fa.writeTransition())
        elif option == "4":
            print(fa.writeInitialState())
        elif option == "5":
            print(fa.writeFinalStates())
        elif option == "6":
            given_string = input("Give a string: ")
            if fa.is_accepted(given_string):
                print("Accepted")
            else:
                print("Not accepted")
        else:
            print("Program done")
            break
