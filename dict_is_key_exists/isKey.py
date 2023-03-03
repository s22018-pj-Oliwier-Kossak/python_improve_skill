S = {x:x+1 for x in range(10000) if x%23 == 0}


def isKey(dict,key):
    if key in dict:
        return True
    else:
        return False

print(isKey(S,7430))