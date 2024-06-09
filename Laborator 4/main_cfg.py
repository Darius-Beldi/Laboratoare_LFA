# This is the main file to run the emulator
from c_parser import load_file
from cfg_checker import check
from cfg_emulator import cfg_emulator
dictionary = load_file("input.in")
check(dictionary, 1)
print(dictionary)
cfg_emulator(dictionary)