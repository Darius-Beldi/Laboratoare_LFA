def load_file(file_name):
    text_clean = []
    with open(file_name, 'r') as text:
        for line in text:
            if line.strip():
                if line[0] != "#":
                    text_clean.append(line.strip())  # in text_without_comments will be the text without the comments or empty lines

    content = {}
    in_section = 0                              #varible that tests if i am currently in a state
    for cuvant in text_clean:
        if cuvant[len(cuvant)-1] == ":":
            in_section = 1
            section_name = cuvant[:len(cuvant)-1]
            content[section_name] = []
            continue                               #for each new section creates a new entry in the dictionary

        if in_section == 1:
            if cuvant == "End":
               in_section=0                         # end means the section is over
            else:
                content[section_name].append(cuvant)
    rulestemps = []
    for rule in content["Rules"]:
        temp3=[]
        temp3=rule.split(" -> ")
        temp = []
        temp.append(temp3[0])
        temp2 = []
        temp2 = temp3[1].split(" ")
        temp.append(tuple(temp2))
        rulestemps.append(tuple(temp))
    content["Rules"] = rulestemps

    return(content)

def get_sections(dictionary):
    key_list = []
    for key in dictionary:
        key_list.append(key)            #here will be the list of all the section names
    return(key_list)

def get_section_content(dictionary, section_name):
    return (dictionary[section_name])       #will return the content of the section i requested

