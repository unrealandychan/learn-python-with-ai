
# Lesson 9: Solution

print("Countdown from 10:")
i = 10
while i > 0:
    print(i)
    i -= 1

print("\nRocket Launch Countdown:")
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")


secret_number = 7
guess = 0
while guess != secret_number:
    guess_str = input("\nGuess the secret number (1-10): ")
    guess = int(guess_str)

print("You guessed it! The secret number was 7.")
