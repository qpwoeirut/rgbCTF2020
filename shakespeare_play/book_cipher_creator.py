from random import choice


def encrypt():
    with open("play", 'r') as f:
        lines = [line for line in f]
    plaintext = "itsanrgbtreeeeeee!"
    assert set(plaintext) <= set(''.join(lines)), set(plaintext) - set(''.join(lines))

    positions = {}
    for row,line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch in positions:
                positions[ch].append((row, col))
            else:
                positions[ch] = [(row, col)]

    print(sorted(positions.keys()))

    cipher = "\n".join([str(choice(positions[c])) for c in plaintext])
    cipher = cipher.replace('(', '').replace(')', '')
    print(cipher)

    with open("some_numbers.txt", 'w') as out:
        out.write(cipher)
