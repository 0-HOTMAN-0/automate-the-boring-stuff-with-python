import random
aNumber = random.randint(1, 20)
print("I'm thinking of a number between 1 to 20.")
i = 0
while i < 6:
    print('Take a guess.')
    guess = int(input())
    i = i + 1
    if guess < aNumber:
        print('Your guess is too low')
    elif guess > aNumber:
        print('Your guess is too high')
    else:
        break
if guess == aNumber:
    print('Good job. You guessed my number in ' + str(i) + ' guesses!')
else :
    print('Nope. The number I was thinking of was ' + str(aNumber))
