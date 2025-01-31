# Formal Language Automata and Grammar Toolkit

A Python toolkit for working with formal language constructs including Deterministic Finite Automata (DFA), Non-deterministic Finite Automata (NFA), and Context-Free Grammars (CFG). The toolkit provides parsers, checkers, and emulators for each type of formal language structure.

## Features

The toolkit supports processing and validation of DFAs, NFAs (including epsilon transitions), and CFGs through file-based input. It includes input parsing with comment support, comprehensive error checking, and interactive emulation capabilities.

## Input Format Example

### DFA/NFA:
```
States:
q0
q1
q2
End

Sigma:
a
b
End

Delta:
q0, a, q1
q1, b, q2
End

Starting State:
q0
End

Final States:
q2
End
```

### CFG:
```
Variables:
S
A
B
End

Sigma:
a
b
End

Rules:
S -> A B
A -> a A
A -> a
B -> b B
B -> b
End

Starting Symbol:
S
End
```

## Usage

1. Create your input file following the format above
2. For DFA/NFA: `python main.py`
3. For CFG: `python main_cfg.py`

Error codes provided by checkers:
- Code 1: Empty section
- Code 2: Invalid transitions/rules
- Code 3: Invalid starting/final states or symbols

## License

This project is open source and available under the MIT License.
