word = 'kaak'

def is_palindrom(word):
    if word[::] == word [::-1]:
        return True
    else:
        return False

print(is_palindrom(word))

list_word = list(word)







