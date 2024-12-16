def main():
    grades = []
    print("Enter five grades:")
    for i in range(5):
        grade = float(input(f"Grade {i + 1}: "))
        grades.append(grade)

    if len(grades) != 5:
        print("Error: You must enter exactly five grades.")
    else:
        # Calculate the range and average
        grade_range, average = calculate_range_and_average(grades)

        # Display the results
        print(f"\nRemaining grades after dropping the lowest two: {sorted(grades)[2:]}")
        print(f"Range of remaining grades: {grade_range}")
        print(f"Average of remaining grades: {average:.2f}")

def calculate_range_and_average(grades):
    # Sort the grades and drop the lowest two
    sorted_grades = sorted(grades)
    remaining_grades = sorted_grades[2:]

    grade_range = max(remaining_grades) - min(remaining_grades)
    average = sum(remaining_grades) / len(remaining_grades)

    return grade_range, average

main()