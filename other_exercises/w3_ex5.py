
class Student:

    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year

# Write a Python function student_data () which will print the id of a
# student (student_id).

# If the user passes an argument student_name or student_class the function
# will print the student name and class.


def student_data(id, **kwargs):
    if "student_name" and "student_class" in kwargs:
        string = "Student_Id:{}, Student_Name:{}, Student_Class:{}"
        print(string.format(id, kwargs['student_name'],
                            kwargs['student_class']))
    else:
        print("Student_Id:{}".format(id))


student_data(id ="XRC213" , student_name="John Doe",
             student_class="CS")
student_data(id="XRC213")
