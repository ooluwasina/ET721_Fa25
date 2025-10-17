"""
Daniel Oluwasina
Oct 8th, 2025
Lab 9, test input and output data
"""

def main():
    while True:
        try:
            num_student = int(input("Enter number of students: "))
            if num_student <=0:
                print("Number of students must be greater than 0, Please try again")
            else:
                break
        except ValueError:
            print("invalid input. Please enter a positive nunumerical value")

    total_sum_grades = 0
    for i in range(num_student):
        while True:
            try:
                grade = float(input(f"Enter grade fot student {i+1}"))
                if 0<=grade<=100:
                    total_sum_grades += grade
                    break
                else:
                    print("Invalid input. Enter a grade between 0 and 100: ")
            except ValueError:
                print("Invalid input! Enter a numerical value")
    
    average = total_sum_grades / num_student

    print(f"The class average is{average: .2f}")

if __name__ == "__main__":
    main()