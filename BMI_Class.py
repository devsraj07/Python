class BMICalculater:
    weight = 0
    height = 0
    bmi = 0

    @staticmethod
    def get_input():
        BMICalculater.weight = float(input("Enter weight in kg: "))
        BMICalculater.height = float(input("Enter height in cms: "))


    @staticmethod
    def calculate_bmi():
        BMICalculater.height = BMICalculater.height / 100
        BMICalculater.bmi = BMICalculater.weight / (BMICalculater.height**2)
        BMICalculater.bmi = round(BMICalculater.bmi,2)

    @staticmethod
    def display_bmi():
        print(BMICalculater.bmi)

if __name__== "__main__":
    obj_bmi = BMICalculater()
    obj_bmi.get_input()
    obj_bmi.calculate_bmi()
    obj_bmi.display_bmi()
