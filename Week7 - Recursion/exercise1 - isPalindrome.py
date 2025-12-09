def ispalindrome(word):
    list = []
    reverse = ""
    size = len(word)
    for i in range(size,0,-1):
        list.append(word[i-1])
    for i in range(len(list)):
        reverse = reverse+str(list[i])
    if reverse == word:
        return True
    else:
        return False
word = "racecar"
print(ispalindrome(word))