def main():
    print("Welcome to the Mad Libs Game!\n")
    
    # Ask the user for words
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    adverb = input("Enter an adverb: ")
    
    # Create the story
    story = f"""
    Today I went to {place} and it was a very {adjective} day.
    I saw a {noun} that could {verb} {adverb}!
    Everyone around me was so surprised and started laughing.
    It was one of the best days ever!
    """
    
    # Print the final story
    print("\nHere is your Mad Lib story:")
    print(story)

if __name__ == "__main__":
    main()
