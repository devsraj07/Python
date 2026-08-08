def inputfloat(hint):
  """ 
  Prints hint and asks to enter number.
  Repeats until decimal number is entered.
  """
  ret = False
  while ret is False:
    ret = input(hint)
    try:
        return ret
    except ValueError:
      print("Please enter number")

class BMIcalculator:
    w = 0.0
    h = 0.0

    @staticmethod
    def getdata():
        """
        Get weight in kgs and height in cms.
        Height is entered in cetimetres and stored in metres
        """
        BMIcalculator.w = float(input("Please enter your weight in kilograms:"))
        BMIcalculator.h = float(input("Please enter your height in centimetres:"))/100
    
    @staticmethod
    def calculate():
        """
        Calculate and return bmi
        """
        return round(BMIcalculator.w/(BMIcalculator.h*BMIcalculator.h),2)


def main():
  print("\n","="*42,"\n")
  print("Hello, let's calculate your BMI.");
  
  calc = BMIcalculator()
  print()
  calc.getdata()
  bmi=calc.calculate()
  print(f"Your BMI is {bmi}")
  print("\n","="*42,"\n")

if __name__ == "__main__":
    main()