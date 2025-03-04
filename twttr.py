vowels = ["a", "e", "i", "o", "u"]
output = ""
found = False
x = input("Write a message...")

for char in range(0, len(x)):
    for nr in range(0, len(vowels)):
        if x[char:char+1].lower() == vowels[nr]:
            found = True
            break
    if not found:
        output += x[char:char+1]
        continue
    found = False
    
print(output)

