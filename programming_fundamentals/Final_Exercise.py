Don_Quijote = True
Twelve_rules_for_life = True
Atomic_Habits = True
Sophies_Choice = True


while True:
    user_input = input("")


    if user_input == "Don_Quijote":
        if Don_Quijote:
            Don_Quijote = False
            print("You have taken the book: Don_Quijote")
        else:
            print("The book 'Don_Quijote' is not available")

    elif user_input == "Twelve_rules_for_life":
        if Twelve_rules_for_life:
            Twelve_rules_for_life = False
            print("You have taken the book: Twelve_rules_for_life")
        else:
            print("The book 'Twelve_rules_for_life' is not available")

    elif user_input == "Atomic_Habits":
        if Atomic_Habits:
            Atomic_Habits = False
            print("You have taken the book: Atomic_Habits")
        else:
            print("The book 'Atomic_Habits' is not available")

    elif user_input == "Sophies_Choice":
        if Sophies_Choice:
            Sophies_Choice = False
            print("You have taken the book: Sophies_Choice")
        else:
            print("The book 'Sophies_Choice' is not available")


    elif user_input == "Return_Don_Quijote":
        if not Don_Quijote:
            Don_Quijote = True
            print("You have returned the book: Don_Quijote")
        else:
            print("The book 'Don_Quijote' was not taken")

    elif user_input == "Return_Twelve_rules_for_life":
        if not Twelve_rules_for_life:
            Twelve_rules_for_life = True
            print("You have returned the book: Twelve_rules_for_life")
        else:
            print("The book 'Twelve_rules_for_life' was not taken")

    elif user_input == "Return_Atomic_Habits":
        if not Atomic_Habits:
            Atomic_Habits = True
            print("You have returned the book: Atomic_Habits")
        else:
            print("The book 'Atomic_Habits' was not taken")

    elif user_input == "Return_Sophies_Choice":
        if not Sophies_Choice:
            Sophies_Choice = True
            print("You have returned the book: Sophies_Choice")
        else:
            print("The book 'Sophies_Choice' was not taken")
    else:
        print("Invalid input. Please enter a valid command.")
