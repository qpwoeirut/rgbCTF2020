from base64 import b64decode  # we'll need to decode base64 text, so let's import a library to do that

with open("basic_chall.txt", 'r') as f:  # read in the challenge text
    s = f.read()

while "rgb" not in s.lower() and s:  # once our flag is fully decoded, it'll have "rgb" in it
    print(s)  # print out our progress
    try:  # try binary first
        s = ''.join([chr(int(c, 2)) for c in s.split()])
        print('bin')
    except ValueError:  # int(c, 2) will raise a ValueError if c has characters besides 0 or 1
        try:  # try octal next
            s = ''.join([chr(int(c, 8)) for c in s.split()])
            print('oct')
        except ValueError:  # Do the same
            try:
                s = ''.join([chr(int(c, 16)) for c in s.split()])
                print('hex')
            except ValueError:  # finally if binary, octal, and hex don't work, we know it has to be base64
                s = b64decode(s).decode()
                print('b64')
print(s)  # this should have our answer!
