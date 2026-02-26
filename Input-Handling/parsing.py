try:
    userInput = input("Input four numbers separated with a space: ")
    
    #Split the input, and map them as integers (for example)
    a, b, c, d = map(int, userInput.split())

    #Output
    print(f"The first number was {a}")
    print(f"The first number was {b}")
    print(f"The first number was {c}")
    print(f"The first number was {d}")
except Exception as e:
    #Make sure to error handle!
    print(f"Error. Invalid Input. {e}")

