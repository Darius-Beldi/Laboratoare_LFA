def emulator(dictionary):
    inp = input("Input the string: ").split()
    current_state = dictionary["Starting State"][0]

    for letter in inp:
        for transition in dictionary["Delta"]:
            if transition[0] == current_state and transition[1] == letter:
                current_state = transition[2]
                break

    if current_state in dictionary["Final States"]:
        print("The string is accepted")
    else:
        print("The string is not accepted")
