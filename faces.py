def convert(s):
    x = s.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

def main():
    x = convert(input("I will change any smileys in your text...\n"))
    print(x)
    
main()
    