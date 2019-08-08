def getMissingLetters(phrase):
    if not isinstance(phrase, str):
        raise ValueError('Phrase parameter should be a string value.')

    letters = 'abcdefghijklmnopqrstuvwxyz'
    return "".join([i for i in letters if i not in phrase])