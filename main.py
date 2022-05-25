from audioop import reverse


def is_palindrom(word):
    reversed_word = ''
    for i in range(len(word)-1,-1,-1):
        reversed_word += word[i]
    if word.lower() == reversed_word.lower():
        return True
    else:
        return False
    


