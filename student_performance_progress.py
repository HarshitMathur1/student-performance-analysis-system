import csv

CSV_FILE = "students.csv"
SUBJECTS = {
    "subject1": "Subject 1",
    "subject2": "Subject 2",
    "subject3": "Subject 3",
    "lab_marks": "Lab"
}
COLUMNS = ["student_id", "name", "batch_no"] + list(SUBJECTS.keys())


def create_file():
    try:
        with open(CSV_FILE, "r", newline=""):
            pass
    except FileNotFoundError:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS)


def get_students():
    create_file()
    students = []

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                marks = []
                for subject in SUBJECTS:
                    mark = float(row[subject])
                    if mark < 0 or mark > 100:
                        raise ValueError
                    marks.append(mark)

                student = {
                    "id": row["student_id"].strip(),
                    "name": row["name"].strip(),
                    "batch": int(row["batch_no"]),
                    "marks": marks
                }

                if student["id"] and student["name"]:
                    students.append(student)

            except (ValueError, KeyError, TypeError):
                print("A row has incorrect data. Skipping it.")

    return students


def get_average(student):
    return sum(student["marks"]) / len(SUBJECTS)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "D"


def add_student():
    students = get_students()
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("This ID is already used.")
            return

    name = input("Enter student name: ").strip()

    try:
        batch = int(input("Enter batch number: "))
        if batch <= 0:
            print("Enter a valid batch number.")
            return

        marks = []
        for subject in SUBJECTS.values():
            mark = float(input("Enter marks in " + subject + " (0-100): "))
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return
            marks.append(mark)

    except ValueError:
        print("Please enter numbers for batch and marks.")
        return

    if student_id == "" or name == "":
        print("Student ID and name cannot be empty.")
        return

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, batch] + marks)

    print("Student added successfully.")


def show_students():
    students = get_students()

    if not students:
        print("No students found.")
        return

    print("\nALL STUDENTS")
    print("ID\tName\tBatch\tAverage\tGrade")

    for student in students:
        average = get_average(student)
        print(student["id"], student["name"], student["batch"],
              round(average, 2), get_grade(average), sep="\t")


def main():
    create_file()

    while True:
        print("\nSTUDENT MARKS SYSTEM")
        print("1. Add student")
        print("2. Show all students")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            print("Program closed.")
            break
        else:
            print("Please enter a number from 1 to 3.")


if __name__ == "__main__":
    main()
