while True:
    number = input("Enter a number: ")
    try:
        value = int(number)
        if value < 0:
            print("Try again.")
            continue
        break
    except ValueError:
        print("Not an integer")
print(value)
