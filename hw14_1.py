class GroupLimitExceededError(Exception):
    """Виняток для ситуації, коли у групі понад 10 студентів."""

    def __init__(self, message="Cannot add more than 10 students to the group"):
        self.message = message
        super().__init__(self.message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name and
                    self.record_book == other.record_book)
        return False

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupLimitExceededError()
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)
        else:
            print(f"Student with last name {last_name} not found.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 18, 'Anrey', 'Lincoln', 'AN142')
st4 = Student('Female', 20, 'Don', 'Williams', 'AN145')
st5 = Student('Male', 40, 'Tom', 'Smith', 'AN142')
st6 = Student('Female', 65, 'Martin', 'White', 'AN145')
st7 = Student('Male', 37, 'Andre', 'Robinson', 'AN142')
st8 = Student('Female', 23, 'Sandra', 'Moore', 'AN145')
st9 = Student('Male', 19, 'Chak', 'Harris', 'AN142')
st10 = Student('Female', 21, 'Lee', 'King', 'AN145')
st11 = Student('Male', 70, 'Jackie', 'Chan', 'AN142')

gr = Group('<PD1>')

for student in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]:
    gr.add_student(student)

print("Initial group:")
print(gr)

try:
    for i in range(11):
        st = Student('Male', 20 + i, f'FirstName{i}', f'LastName{i}', f'AN1{i}')
        try:
            gr.add_student(st)
        except GroupLimitExceededError as e:
            print(e)
            break
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Group after attempting to add 11 students:")
print(gr)