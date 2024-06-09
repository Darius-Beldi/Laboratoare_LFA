# This is the main file to run the emulator
from c_parser import load_file
from nfa_checker import check
from emulator import emulator

dictionary = load_file("input.in")
check(dictionary, show_errors=1)
emulator(dictionary)