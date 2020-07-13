from random import randint  # yeah i know its not cryptographically secure but it's much easier to break the RNG below


BOUNDS = (3, 100)


def print_options():
    print("Options:")
    print("0) Quit")
    print("1) Generate (up to) 100 random numbers")
    print("2) Guess the next number 10 times for the flag")


def get_next(cur: int, n: int) -> int:
    number = str(cur * cur)
    if (len(number) - n) % 2 != 0:
        number = '0' + number

    return int(number[(len(number) - n) // 2: (len(number) + n) // 2])


def generate():
    n = int(input(f"Enter n (between {BOUNDS[0]} and {BOUNDS[1]}): "))
    if n < BOUNDS[0]:
        print(f"The value you entered for n was {n}, which is too small")
        return
    if n > BOUNDS[1]:
        print(f"The value you entered for n was {n}, which is too large")
        return

    seed_number = randint(pow(10, n - 1), pow(10, n) - 1)
    number = seed_number
    already_seen = set()
    counter = 0

    for i in range(100):
        counter += 1
        already_seen.add(number)

        number = get_next(number, n)

        if number in already_seen:
            break
        print(number)

    print("Done!")


def challenge():
    n = 100
    seed_number = randint(pow(10, n - 1), pow(10, n) - 1)
    print(f"My current number is {seed_number}. What number will come next?")

    guess = int(input().strip())
    return guess == get_next(seed_number, n)


def main():
    print("Welcome to Ye Old PRNG!")

    while True:
        print_options()
        cmd = int(input().strip())
        if cmd == 0:
            break
        elif cmd == 1:
            generate()
        elif cmd == 2:
            for _ in range(10):
                if challenge() is True:
                    print("Correct.")
                else:
                    print("Incorrect.")
                    return
            with open("flag.txt", 'r') as flag:
                print(f"Here's your flag: {flag.read()}")
            return


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("ERROR:", e)