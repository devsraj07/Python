class BMICalculater:
    weight = 0
    height = 0
    bmi = 0

    def calculate_bmi():
        bmi = weight / ((height**2) / 100)
        bmi = round(bmi,2)

    def display_bmi():
        print(bmi)

if __name__== "__main__":
    user_weight = float(input("Enter weight: "))
    user_height = float(input("Enter height: "))
    obj_bmi = BMICalculater()
    obj_bmi.weight = user_weight
    obj_bmi.height = user_height
    obj_bmi.calculate_bmi()
    obj_bmi.display_bmi()
