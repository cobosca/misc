def main():
    x = input("What time is it? ")
    time = convert(x)
    if time >= 7.00 and time <= 8.00:
        return "Breakfast time"
    elif time >= 12.00 and time <= 13.00:
        return "Lunch time"
    elif time >= 18.00 and time <= 19.00:
        return "Dinner time"
    
def convert(time):
    hours, minutes = time.split(":")
    ctime = round(int(hours) + int(minutes)/60, 2)
    return ctime

if __name__ == "__main__":
    answer = main()
    if answer:
        print(answer)