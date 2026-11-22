class Student:
    def set_student_details(self, reg_no, name, batch, section):
        self.__reg_no = reg_no
        self.__name = name
        self.__batch = batch
        self.__section = section

    def display_student_details(self):
        print("Registration Number:", self.__reg_no)
        print("Name:", self.__name)
        print("Batch:", self.__batch)
        print("Section:", self.__section)


class StudentPerformance(Student):
    def set_marks(self, gfg, el, project, lab, total):
        self.__gfg = gfg
        self.__el = el
        self.__project = project
        self.__lab = lab
        self.__total = total

    def display_performance(self):
        self.display_student_details()
        print("GFG Marks:", self.__gfg, "out of 6")
        print("EL Activities Marks:", self.__el, "out of 2")
        print("Project Milestone-1 Marks:", self.__project, "out of 2")
        print("Lab Marks:", self.__lab, "out of 7.5")
        print("Total Marks:", self.__total)

    def display_component_percentages(self):
        print("GFG Percentage:", round(self.__gfg / 6 * 100, 2))
        print("EL Activities Percentage:", round(self.__el / 2 * 100, 2))
        print("Project Milestone-1 Percentage:", round(self.__project / 2 * 100, 2))
        print("Lab Percentage:", round(self.__lab / 7.5 * 100, 2))


student1 = StudentPerformance()
student1.set_student_details("S26BMTCSU0001", "Abhishek Sharma", 1, "S1")
student1.set_marks(5, 2, 2, 2, 15)
student1.display_performance()
student1.display_component_percentages()
