from pwn import process, remote


def get_next(cur: int, n: int) -> int:
    number = str(cur * cur)
    if (len(number) - n) % 2 != 0:
        number = '0' + number

    return int(number[(len(number) - n) // 2: (len(number) + n) // 2])


def main():
    rem = process(["python3", "ye_old_prng.py"])

    assert rem.recvline().decode().strip() == "Welcome to Ye Old PRNG!"

    rem.recvuntil("flag\n")
    rem.sendline('2')
    for _ in range(10):
        num = int(rem.recvline().decode().split()[4].strip('.'))
        print(num)

        rem.sendline(str(get_next(num, 100)))
        assert rem.recvline().decode().strip() == "Correct."

    print(rem.recvall(1).decode().strip())


if __name__ == '__main__':
    main()
