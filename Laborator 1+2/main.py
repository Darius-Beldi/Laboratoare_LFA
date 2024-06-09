# This is the main file to run the emulator
from c_parser import load_file
from dfa_checker import check
from emulator import emulator

dictionary = load_file("dfa/treasure_hunt2.in")
check(dictionary, show_errors=1)
emulator(dictionary)


