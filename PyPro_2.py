class Person:
    """
    Describers person
    """
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname} - phone: {self.phone}"


class Student(Person):
    def __init__(self, name, surname, phone, university, direction):
        super().__init__(name, surname, phone)
        self.university = university
        self.direction = direction

    def __str__(self):
        return f"Student {self.surname} {self.name}, institution: {self.direction}, " \
               f"course: {self.university}, phone: {self.phone}"


class Group:
    def __init__(self, students):
        self.students = students

    def append_student(self, student):
        self.students.append(student)

    def search_student(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        self.result = ""
        for i in range(len(self.students)):
            self.result += str(i + 1) + ". " + self.students[i].surname + "\n"
        return self.result


Student_1 = Student("Uma", "Thurman", "0441282231", "Harvard University", "Medical")
Student_2 = Student("Quentin", "Tarantino", "0441322201", "Harvard University", "Law")
Student_3 = Student("John", "Travolta", "0447772101", "Harvard University", "Business")
Student_4 = Student("Samuel", "Jackson", "0442223311", "Harvard University", "Divinity")
Student_5 = Student("Maria", "Medeiros", "0441221281", "Stanford University", "Economy")
Student_6 = Student("Bruce", "Willis", "0441791541", "Stanford University", "Geology")
Student_7 = Student("Christopher", "Walken", "0445479541", "Stanford University", "Chemistry")
Student_8 = Student("Steven", "Buscemi", "0441179541", "Yale University", "Management")
Student_9 = Student("Michae", "Madsen", "0442228822", "Yale University", "Art")
Student_10 = Student("Lucy", "Liu", "04412211198", "Yale University", "Biology")

group = [Student_1, Student_2, Student_3, Student_4, Student_5, Student_6, Student_7, Student_8, Student_9, Student_10]
Group_persons = Group(group)
print(Group_persons)
print()

Group_persons.append_student(Student_10)
print(Group_persons)

print(Group_persons.search_student("Travolta"))

Group_persons.remove_student(Student_5)
print(Group_persons)
