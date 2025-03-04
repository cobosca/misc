x = input("Greeting: ").lower().strip()
if x[:5] == "hello":
    print("$0")
elif x[:1] == "h":
    print("$20")
else:
    print("$100")