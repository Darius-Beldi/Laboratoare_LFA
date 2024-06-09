def exhaust_epsilon(dictionary, current_state):

    transitions_from_current_state = []
    for transition in dictionary["Delta"]:
        if transition[0] == current_state:
            transitions_from_current_state.append(transition)
    transitions_from_current_state1 = []
    for transition in transitions_from_current_state:
        if transition[1] == "E":
            for trns in dictionary["Delta"]:
                if transition[2] == trns[0]:
                    transitions_from_current_state1.append(trns)

    return transitions_from_current_state1


def emulator(dictionary):
    inp = input("Input the string: ").split()
    current_state = dictionary["Starting State"][0]
    threads = []
    i = 0
    while i < len(inp):
        letter = inp[i]
        
        possible_transitions = exhaust_epsilon(dictionary, current_state)
        pt=[]
        for transition in possible_transitions:
            if transition[1] == letter:
                pt.append(transition)
        i = i+1
        print(pt)

  #  for letter in inp:
   #     for transition in dictionary["Delta"]:
    #        if transition[0] == current_state:
     #           while transition[1] == "E":
      #              current_state = transition[0]


       #             and transition[1] == letter):
        #        current_states_list.append(transition[2])

#    for i in range(len(current_states_list)):
 #       if current_states_list[i] in dictionary["Final States"]:
  #          print("The string is accepted")
   #         break
    #    else:
     #       print("The string is not accepted")
      #      break
