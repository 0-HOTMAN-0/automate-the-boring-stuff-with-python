while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        print("I'm fine, thanks. Who are you?")
        continue
    print("Hello Joe. What is the password? (It's a fish)")
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')