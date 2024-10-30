
while True:
    while True:
        user_input = input("Enter a number (1-50): ")
        if user_input.isdigit():    
            user_input = int(user_input)  
            if 1 <= user_input <= 50:
                break
            else:
                print("Invalid input, must be between 1 and 50.")
                print("Please try again.")        
        else:
            print("Invalid input, must be a digit.")
            print("Please try again.")
    
    while True:
        another_entry = input("Would you like to submit another number? (Yes/No): ").capitalize()    
        # if statement evaluating if the response is == to 'No'  
        if another_entry == "No":
            # break if returned true
            break
            # elif statement evaluating if or else the respond is == to 'Yes'
        elif another_entry == "Yes":
            # break if returned true
            break
        # else statement; raises the error
        else: 
            # print invalid
            print("Invalid input, 'Yes' or 'No' only.")
            # notice the user/s to redo
            print("Please try again.")      
    
    # if statement that is looped inside the loop 1; after the first evaluation for 'No' response, this will be the final decider to finished the main loop (loop 1), if this returned false, the main loop will start again; only means that the user/s respond with a 'Yes'
    if another_entry == "No":
        # break the main loop (loop 1)
        break 
