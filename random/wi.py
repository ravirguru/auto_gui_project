s = "i loVE Python"
# i LOve pYTHON
for i in range(len(s)):
    if i == 0:
        continue
    words = s.split()
    print(words)
    li = []
    for word in words:
        for j in range(len(word)):
            letter = word[j]
            if letter[j] == 0:
                continue
            temp = ord(letter)
            if 65 <= temp <=90:
                li.append(chr(temp+32))
            if 97 <= temp <= 122:
                li.append(chr(temp - 32))
        print(" ".join(li))

