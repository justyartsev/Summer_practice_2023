old_string = "We all want the truth".lower()
new_string = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
rot_alphabet = "nopqrstuvwxyzabcdefghijklm"
for el in old_string:
    if el == " ":
        new_string += " "
    else:
        index = alphabet.find(el)
        new_string += rot_alphabet[index]
print(old_string)
print(new_string)
