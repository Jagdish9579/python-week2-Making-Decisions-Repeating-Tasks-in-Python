def calculate_grade(marks):
    """Return the grade and an encouraging message."""
    if marks >= 90:
        return "A", "Excellent! Outstanding work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! Keep improving! 😊"
    elif marks >= 60:
        return "D", "You passed! Work harder next time! 💪"
    else:
        return "F", "Don't give up! Learn and try again! 📚"


def get_valid_marks():
    """Keep asking until the user enters valid marks."""
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter a value from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("=" * 35)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 35)

    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade, message = calculate_grade(marks)

    print("\n" + "=" * 35)
    print(f"RESULT FOR {name.upper()}")
    print("=" * 35)
    print(f"Marks: {marks:g}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    print("=" * 35)


if __name__ == "__main__":
    main()
