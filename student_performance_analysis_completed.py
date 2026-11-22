import csv
from pathlib import Path

file_name = Path(__file__).with_name("students.csv")


def load_students():
    students = []

    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if len(row) == 1 and ";" in row[0]:
                    row = row[0].split(";")

                if len(row) == 12:
                    row = row[1:]

                if len(row) == 11:
                    for i in range(len(row)):
                        row[i] = row[i].strip()
                    students.append(row)
                elif len(row) != 0:
                    print("A row has an incorrect number of columns. Check the CSV file.")

    except FileNotFoundError:
        print("students.csv was not found beside this Python file.")
        print("Keep students.csv in the same folder as this program.")

    return students


def show_students():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    print("\nALL STUDENTS")

    for student in students:
        print("Registration Number:", student[0])
        print("Name:", student[1])
        print("Batch:", student[2])
        print("Section:", student[3])
        print("Total Marks:", student[10])
        print("------------------------------")


def search_student():
    students = load_students()
    reg_no = input("Enter registration number: ").strip()
    found = False

    for student in students:
        if student[0] == reg_no:
            print("\nSTUDENT REPORT")
            print("Registration Number:", student[0])
            print("Name:", student[1])
            print("Batch:", student[2])
            print("Section:", student[3])
            print("Lecture Faculty:", student[4])
            print("Lab Faculty:", student[5])
            print("GFG Marks:", student[6], "out of 6")
            print("EL Activities Marks:", student[7], "out of 2")
            print("Project Milestone-1 Marks:", student[8], "out of 2")
            print("Lab Marks:", student[9], "out of 7.5")
            print("Total Marks:", student[10])
            found = True
            break

    if found == False:
        print("Student not found.")


def show_ranking():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if float(students[j][10]) > float(students[i][10]):
                temp = students[i]
                students[i] = students[j]
                students[j] = temp

    print("\nSTUDENT RANKING")
    rank = 1

    for student in students:
        print("Rank:", rank, "Name:", student[1], "Total Marks:", student[10])
        rank = rank + 1


def show_class_summary():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    total = 0
    highest = students[0]
    lowest = students[0]

    for student in students:
        total = total + float(student[10])

        if float(student[10]) > float(highest[10]):
            highest = student

        if float(student[10]) < float(lowest[10]):
            lowest = student

    average = total / len(students)

    print("\nCLASS SUMMARY")
    print("Number of students:", len(students))
    print("Average Total Marks:", round(average, 2))
    print("Highest scorer:", highest[1], "-", highest[10])
    print("Lowest scorer:", lowest[1], "-", lowest[10])

    names = ["GFG", "EL Activities", "Project Milestone-1", "Lab"]
    maximum_marks = [6, 2, 2, 7.5]
    percentages = []

    print("\nASSESSMENT AVERAGES")

    for i in range(4):
        total_marks = 0

        for student in students:
            total_marks = total_marks + float(student[i + 6])

        average_marks = total_marks / len(students)
        percentage = average_marks / maximum_marks[i] * 100
        percentages.append(percentage)

        print(names[i], "average:", round(average_marks, 2), "out of", maximum_marks[i])
        print("Average percentage:", round(percentage, 2), "%")
        print("*" * int(percentage / 5))

    highest_component = 0
    lowest_component = 0

    for i in range(1, 4):
        if percentages[i] > percentages[highest_component]:
            highest_component = i
        if percentages[i] < percentages[lowest_component]:
            lowest_component = i

    print("\nKEY INSIGHTS")
    print("Strongest component:", names[highest_component])
    print("Component to review:", names[lowest_component])


def add_student():
    students = load_students()
    reg_no = input("Enter registration number: ").strip()

    if reg_no == "":
        print("Registration number cannot be empty.")
        return

    for student in students:
        if student[0] == reg_no:
            print("This registration number already exists.")
            return

    name = input("Enter student name: ").strip()
    batch = input("Enter batch: ").strip()
    section = input("Enter section: ").strip()
    lecture_faculty = input("Enter lecture faculty name: ").strip()
    lab_faculty = input("Enter lab faculty name: ").strip()

    if name == "" or batch == "" or section == "":
        print("Name, batch and section cannot be empty.")
        return

    names = ["GFG", "EL Activities", "Project Milestone-1", "Lab"]
    maximum_marks = [6, 2, 2, 7.5]
    marks = []

    for i in range(4):
        while True:
            try:
                mark = float(input("Enter " + names[i] + " marks: "))

                if mark >= 0 and mark <= maximum_marks[i]:
                    marks.append(str(mark))
                    break
                else:
                    print("Enter marks between 0 and", maximum_marks[i])
            except ValueError:
                print("Please enter a number.")

    while True:
        try:
            total_marks = float(input("Enter Total Marks given by faculty: "))
            if total_marks >= 0:
                break
            else:
                print("Total Marks cannot be negative.")
        except ValueError:
            print("Please enter a number.")

    new_student = [reg_no, name, batch, section, lecture_faculty, lab_faculty]

    for mark in marks:
        new_student.append(mark)

    new_student.append(str(total_marks))

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_student)

    print("Student added successfully.")


def export_analysis():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    names = ["GFG", "EL Activities", "Project Milestone-1", "Lab"]
    maximum_marks = [6, 2, 2, 7.5]

    with open("component_analysis.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Assessment", "Maximum Marks", "Class Average", "Average Percentage"])

        for i in range(4):
            total = 0

            for student in students:
                total = total + float(student[i + 6])

            average = total / len(students)
            percentage = average / maximum_marks[i] * 100
            writer.writerow([names[i], maximum_marks[i], round(average, 2), round(percentage, 2)])

    print("Analysis saved in component_analysis.csv")


def main():
    while True:
        print("\nSTUDENT PERFORMANCE ANALYSIS SYSTEM")
        print("1. Show all students")
        print("2. Search student")
        print("3. Show ranking")
        print("4. Show class summary")
        print("5. Add student")
        print("6. Export analysis")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_students()
        elif choice == "2":
            search_student()
        elif choice == "3":
            show_ranking()
        elif choice == "4":
            show_class_summary()
        elif choice == "5":
            add_student()
        elif choice == "6":
            export_analysis()
        elif choice == "7":
            print("Program closed.")
            break
        else:
            print("Please enter a number from 1 to 7.")


main()
