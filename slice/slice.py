a = '!ooe&sj7?czaa()lmxuo,t2fa^4rtngk'


print(a[-2::-3])

word = 'python_das.txt'
def is_start_python_is_end_txt(word):
    if word[:6] == "python" and word[-4:] ==".txt":
        return True
    else:
        return False

print(is_start_python_is_end_txt(word))


