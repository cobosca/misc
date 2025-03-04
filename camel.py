x = input("Enter camel case: ").strip()

snake = ""

for char in range(0, len(x)):
    if x[char:char+1].isupper():
        snake += "_"
        snake += x[char:char+1].lower()
    else:
        snake += x[char:char+1].lower()
        
print(f"Snake case: {snake}")
        
