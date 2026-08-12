"""
Week 2 - Activity 5: Temperature converter
-------------------------------------------------------------
OOP project to take user's input of temperature with prefix (like F for Fahrenheit, or C for Celsius) 
and then convert it to Celsius if Fahrenheit passed or to Fahrenheit if Celsius passed.
"""

class Temperature_Converter():

    def __init__(self, temp: str):
        self.temp = temp
        self.temp_prefix = temp[0] if temp else ''
        self.temp_number = temp[1:] if len(temp) > 1 else ''

    def is_valid(self):
        if self.temp_prefix not in ('F', 'C'):
            return False
        try:
            float(self.temp_number)
            return True
        except ValueError:
            return False
    
    def fahrenheit_to_celsius(self, value):
        return round((value - 32) * 5 / 9, 2)
    
    def celsius_to_fahrenheit(self, value):
        return round((value * 9 / 5) + 32, 2)
    
    def convert(self):
        if not self.is_valid():
            print("Invalid input. Please enter the temperature with correct 'C' or 'F' prefix.")
        
        value = float(self.temp_number)

        if self.temp_prefix == 'F':
            celsius = self.fahrenheit_to_celsius(value)
            return f"{self.temp} degrees Fahrenheit is convert to {celsius: .2f} degrees Celsius"
        else: #prefix == 'C'
            fahrenheit = self.celsius_to_fahrenheit(value)
            return f"{self.temp} degrees Celsius is convert to {fahrenheit: .2f} degrees Fahrenheit"

def main():
    print("=======Temperature Converter========")
    print("Enter temperature value starting with 'F'(Fahrenheit or 'C'(Celsius), e.g. F51 or C25.) ")
    print("Type 'esc' to exit.\n")

    while True:
        user_input = input("Enter temperature: ").strip()

        if user_input.lower() == 'esc':
            print("Bye!")
            break

        converter = Temperature_Converter(user_input)
        print(converter.convert())
        print()

if __name__ == "__main__":
    main()



        
