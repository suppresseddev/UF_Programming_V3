def lettercount():
    word = input("Enter a word: ").lower()
    letter = input("Enter the letter to count: ").lower()
    wordlist = word.split()
    count = word.count(letter)
    print(f"{letter} appears {count} times.")
lettercount()