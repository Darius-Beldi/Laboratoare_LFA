"""
This is the checker for your DFA
If you want the checker to tell you what is wrong, it has the option of printing an error code if you switch the value of show_errors to 1
This can be done when you call the function

Error codes and their meaning:

If section is empty: error code 1
If something is wrong in the Delta section: error code 2
If something is wrong in either Starting States or Final states: error code 3
"""

def check(dictionary, show_errors=0):

    # checks if any section is empty
    for section_name in dictionary:
        if not dictionary[section_name]:
            if show_errors == 1:
                print(f"{section_name} section is empty")
            return 1

    #checks if section Delta is declared correctly
    for transition in dictionary["Delta"]:
        if transition[0] not in dictionary["States"]:
            if show_errors == 1:
                print(f"State {transition[0]} not declared in section States")
            return 2
        if transition[2] not in dictionary["States"]:
            if show_errors == 1:
                print(f"State {transition[2]} not declared in section States")
            return 2

    for transition in dictionary["Delta"]:
        if transition[1] not in dictionary["Sigma"]:
            if show_errors == 1:
                print(f"Letter {transition[1]} not declared in section Sigma")
            return 2

    #checks if the final state is in the States section

    for state in dictionary["Final States"]:
        if state not in dictionary["States"]:
            if show_errors == 1:
                print(f"")
            raise 3

    #checks if there are more than one starting states
    if len(dictionary["Starting State"]) != 1:
        if show_errors == 1:
            print("There are more starting states")
        return 3

    # checks if the starting state is in the States section
    for state in dictionary["Starting State"]:
        if state not in dictionary["States"]:
            if show_errors == 1:
                print(f"State {state} not declared in section States")
            return 3


    return 0
