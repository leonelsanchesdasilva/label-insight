def getMissingLetters(phrase):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print("".join([i for i in letters if i not in phrase]))