def main():
    a = int(input("a="))
    b = int(input("b="))
    print("x ir", sakne(a,b))

# Funkcija aprekina vienadojuma a*x=b sakni
# jebkuram a un b vertibam
def sakne(a,b):
    return b//a

if __name__ == "__main__":
    main()
