entries_for_1_to_10 = []
entries_for_11_to_20 = []
entries_for_21_to_30 = []
entries_for_31_to_40 = []
entries_for_41_to_50 = []

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
            elif 11 <= user_input <= 20:
                entries_for_11_to_20.append(user_input)
            elif 21 <= user_input <= 30:
                entries_for_21_to_30.append(user_input)    
            elif 31 <= user_input <= 40:
                entries_for_31_to_40.append(user_input)    
            elif 41 <= user_input <= 50:
                entries_for_41_to_50.append(user_input)    
    else:
        print("Invalid input, must be a digit.")
        print("Please try again.")

print("Result:")

numbers_of_1_to_10 = len(entries_for_1_to_10)  
numbers_of_11_to_20 = len(entries_for_11_to_20)
numbers_of_21_to_30 = len(entries_for_21_to_30)
numbers_of_31_to_40 = len(entries_for_31_to_40)
numbers_of_41_to_50 = len(entries_for_41_to_50)
print(f"1-10 = {numbers_of_1_to_10}")     
print(f"11-20 = {numbers_of_11_to_20}")
print(f"21-30 = {numbers_of_21_to_30}")
print(f"31-40 = {numbers_of_31_to_40}")
print(f"41-50 = {numbers_of_41_to_50}")