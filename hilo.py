lowest = 1
highest = 100

print("Please think of a number between {} and {}".format(lowest, highest))
input("Press Enter to start")

guesses = 1
while True:
    print("\tGuessing between {} to {}".format(lowest, highest))
    guess = lowest + (highest - lowest) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?" 
                     " Enter h(for 'guess higher') or l(for 'guess lower'), "
                     " or c(for a 'correct guess') if my guess was correct: "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. Increase the lowest value by one more than the guess
       lowest = guess + 1
    elif high_low == "l":
        # Guess lower. Decrease the lowest value by one less than the guess
        highest = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break

    else:
        print("Please enter h, l or c")

    guesses += 1