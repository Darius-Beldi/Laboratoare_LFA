def cfg_emulator(cfg_dict):
    import random

    start_symbol = cfg_dict['Starting Symbol'][0]
    productions = {}

    for lhs, rhs in cfg_dict['Rules']:
        if lhs not in productions:
            productions[lhs] = []
        productions[lhs].append(list(rhs))

    def generate(symbol):
        if symbol not in productions:
            # If the symbol is a terminal, return it as is
            return symbol
        else:
            # Choose a random production rule for the non-terminal
            expansion = random.choice(productions[symbol])
            result = ''
            for sym in expansion:
                result += generate(sym)
            return result

    generated_string = generate(start_symbol)
    print(generated_string)