"""
This is the checker for your CFG
If you want the checker to tell you what is wrong, it has the option of printing an error code if you switch the value of show_errors to 1
This can be done when you call the function

Error codes and their meaning:

If section is empty: error code 1
If something is wrong in the Rules section: error code 2
If something is wrong with the Starting Symbol: error code 3
"""

def check(dictionary, show_errors=0):

    # checks if any section is empty
    for section_name in dictionary:
        if not dictionary[section_name]:
            if show_errors == 1:
                print(f"{section_name} section is empty")
            return 1

    #checks if section Delta is declared correctly
    for rule in dictionary["Rules"]:
        if rule[0] not in dictionary["Variables"]:
            if show_errors == 1:
                print(f"Variable {rule[0]} not declared in section Variables")
            return 2
        for symbol in rule[1]:
            if symbol not in dictionary["Sigma"] and symbol not in dictionary["Variables"]:
                if show_errors == 1:
                    print(f"Symbol {symbol} not declared in section Sigma or Variables")
                return 2

    #checks if there are more than one starting states
    if len(dictionary["Starting Symbol"]) != 1:
        if show_errors == 1:
            print("There are more starting states")
        return 3

    # checks if the starting state is in the States section
    for state in dictionary["Starting Symbol"]:
        if state not in dictionary["Variables"]:
            if show_errors == 1:
                print(f"Starting Symbol {state} not declared in section Variables")
            return 3


    return 0
