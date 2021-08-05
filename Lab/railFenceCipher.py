def encryptRailFence(text, key):
    rail=[['\n' for i in range(len(text))]
                  for j in range(key)]
    for i in (0, key):
        for j in range(0, len(text)):
            rail[i][j] = '\n'

    dir_down = false
    row = 0 
    col = 0

    for i in range(0, len(text)):
        if row == 0 or row == key-1:
            dir_down = not dir_down
        rail[row][col+1]=text[i]
        if dir_down == true:
            row+=1
        else:
            row-=1

    result = ''

    for i in range(0, key):
        for j in range(0, len(text)):
            if rail[i][j]!='\n':
                result.push_back(rail[i][j])

    return result

def decryptRailFence(cipher, key):
    pass

if __name__ == '__main__':
    print(encryptRailFence('run away from there',3))
    print(decryptRailFence('ra meu wyfo hmarte',3))
