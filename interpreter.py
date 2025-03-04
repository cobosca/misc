def main():

    expression = input("Expression: ")

    x, y, z = expression.split(" ")
    
    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    elif y == "/":
        return float(x) / float(z)
    else:
        return"Invalid operation!"
    

print(round(main(), 1))