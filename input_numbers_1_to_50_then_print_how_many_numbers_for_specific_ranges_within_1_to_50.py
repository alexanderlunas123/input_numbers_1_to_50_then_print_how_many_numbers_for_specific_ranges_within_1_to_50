entries_for_1_to_10 = []

while True:
    user_input = input("Enter a number (1-50): ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input > 50:
            print("Invalid number.")
            print("Proceeding to: 'presenting the data' (processing...)")
            break 
        elif user_input < 1:
            print("Invalid number.")
            print("Proceeding to: 'presenting the data' (processing...)")
            break
        else:
            if 1 <= user_input <= 10:
                entries_for_1_to_10.append(user_input)             
    else:
        print("Invalid input, must be a digit.")
        print("Please try again.")


numbers_of_1_to_10 = len(entries_for_1_to_10)  
print(numbers_of_1_to_10)     