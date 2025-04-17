import random

def display_hangman(tries):
    stages = [
        "😵\n👕\n👖\n👟👟",   # 0 tries left
        "😵\n👕\n👖\n👟",      # 1 try left
        "😵\n👕\n👖",          # 2 tries left
        "😵\n👕",             # 3 tries left
        "😵",                # 4 tries left
        "",                  # 5 tries left (nothing shown yet)
    ]
    return stages[tries]

def choose_word():
    words = ["python", "banana", "apple", "guitar", "rocket", "flower", "emoji", "laptop", "pencil"]
    return random.choice(words)

def main():
    print("🎉 Welcome to Hangman (Emoji Version)! 🎉\n")
    
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 5

    # Create a display word with underscores
    display_word = ["_" for _ in word]

    while tries >= 0 and "_" in display_word:
        print("Word:", " ".join(display_word))
        print(display_hangman(tries))
        guess = input("🔤 Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please guess a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try again.\n")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            print("✅ Correct guess!\n")
            for idx, letter in enumerate(word):
                if letter == guess:
                    display_word[idx] = guess
        else:
            print("❌ Wrong guess!\n")
            tries -= 1

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print(display_hangman(0))
        print("💀 Game Over! The word was:", word)

if __name__ == "__main__":
    main()
