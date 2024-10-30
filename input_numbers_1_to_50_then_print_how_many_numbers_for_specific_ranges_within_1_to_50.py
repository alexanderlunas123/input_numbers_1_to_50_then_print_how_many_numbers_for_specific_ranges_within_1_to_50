

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
        print("Invalid input, must be a digit.")
        print("Please try again.")
    
  