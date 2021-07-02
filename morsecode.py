from pprint import pprint

import pandas

data = pandas.read_csv('morse code.csv', header=None, index_col=0)
code = data.to_dict()[1]


def morsify(text=str):
    """ converts string to morse code """
    morse_code = []
    for let in text.lower():
        if let != " ":
            try:
                morse = code[let]
            except KeyError:
                return f"There is no morse code for the character '{let}'."
        else:
            morse = "  "
        morse_code.append(morse)
    str = ' '.join(morse_code)
    return str
