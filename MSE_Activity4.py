#To calculate body mass index(BMI)
def calculate_bmi():
    try:
        #ask user for height(in centimeters) and weight(in kgs)
        user_weight = float(input("Enter your weight in kilograms: "))
        user_height = float(input("Enter your height in centimeters: "))

        #convert height from centimeters to meters
        height_mtrs = user_height / 100

        #calculate BMI
        bmi = user_weight / (height_mtrs ** 2)
        bmi = round(bmi, 2) # round the result to 2 decimal places

        print(f"Your BMI is: {bmi}")
    except ValueError:
        print("Please enter a valid numbers for weight and height.")

if __name__== "__main__":
    calculate_bmi()


