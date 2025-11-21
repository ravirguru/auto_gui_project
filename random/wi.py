# s = "i loVE Python"
# # i LOve pYTHON
# words = s.split()
# #print(words)
# li = []
# for word in words:
#     converted_list = []
#     for j in range(len(word)):
#             letter = word[j]
#         if j == 0:
#             converted_list.append(letter)
#             continue
#         temp = ord(letter)
#         if 65 <= temp <= 90:
#             converted_list.append(chr(temp + 32))
#         elif 97 <= temp <= 122:
#             converted_list.append(chr(temp - 32))
#         else:
#             converted_list.append(letter)
#     li.append("".join(converted_list))
# print(" ".join(li))
#
#
s = "i loVE Python"
words = s.split()
li = []

for word in words:
    converted_list = []
    for j in range(len(word)):
        letter = word[j]

        if j == 0:
            converted_list.append(letter)
            continue

        temp = ord(letter)
        if 65 <= temp <= 90:
            converted_list.append(chr(temp + 32))
        elif 97 <= temp <= 122:
            converted_list.append(chr(temp - 32))
        else:
            converted_list.append(letter)

    li.append("".join(converted_list))   # ← FIX HERE

print(" ".join(li))
