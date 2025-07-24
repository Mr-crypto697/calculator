#GPA Calculator Program

def calculate_gpa(grades, course_units):
    total_points = 0
    total_units = 0

    for grade, units    in zip(grades, course_units):
        # Convert letter grades to grade points
        if grade == 'A':
            points = 4.0
        elif grade == 'B':
            points = 3.0
        elif grade == 'C':
            points = 2.0
        elif grade == 'D':
            points = 1.0
        elif grade == 'F':
            points = 0.0
        else:
            print(f"Invalid grade '{grade}' entered. Please enter grades A, B, C, D, or F.")
            return None

        total_points += points * units 
        total_units += units   

    if total_units  == 0:
        return 0.0

    gpa = total_points / total_units   
    return gpa

def main():
    num_courses = int(input("Enter the number of courses: "))

    grades = []
    course_units = []

    for _ in range(num_courses):
        grade = input("Enter the grade (A, B, C, D, F): ").upper()
        units   = float(input("Enter the course units for the course: "))
        grades.append(grade)
        course_units.append(units  )

    gpa = calculate_gpa(grades, course_units)

    if gpa is not None:
        print(f"Your GPA is: {gpa:.2f}")

if __name__ == "__main__":
    main()