total_inserted = 0
price = 50

while True:
    if price - total_inserted > 0:
        print(f"Amount due: {price - total_inserted}")
    else:
        print(f"Change Owed: {abs(price - total_inserted)}")
        break
    x = int(input("Insert Coin: "))
    if x == 25 or x == 10 or x == 5:
        total_inserted += x
        