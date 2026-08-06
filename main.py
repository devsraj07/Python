def generate_fibonacci(n):
   
    a, b = 0, 1
   
    # print numbers as long as they are less than or equal to N
    while a <= n:
        print(a, end = " ")
        a, b = b, a + b
    print()

def cal_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    try:
        user_input = input("Enter a number:")
        n = int(user_input)

        if n < 0:
            print("Please enter non-negative numbers.")
            return
        
        #Print all values in the fibonacci series upto N
        generate_fibonacci(n)

        #Calculate and print the factorial of N
        factorial_result = cal_factorial(n)
        print(f"The factorial of {n} ({n}!) is: {factorial_result}")
    
    except ValueError:
        print("Invalid input, please enter a valid integer.")

if __name__ == "__main__":
    main()

        
    

