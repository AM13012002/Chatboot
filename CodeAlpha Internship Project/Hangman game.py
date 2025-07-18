import random
words = ["apple", "tiger", "chair", "house", "robot"]
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6
display_word = ["_"] * len(secret_word)
while attempts_left > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Correct!")
    else:
        attempts_left -= 1
        print("Wrong guess!")
if "_" not in display_word:
    print("\n🎉 You won! The word was:", secret_word)
else:
    print("\n❌ You lost! The word was:", secret_word)