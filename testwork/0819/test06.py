class Teacher():
    def __init__(self, id, name,sex, age, subject):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.subject = subject
    def __str__(self):
        return f"教师编号: {self.id}, 姓名: {self.name}, 性别: {self.sex}, 年龄: {self.age}, 科目: {self.subject}"


class Course:
    def __init__(self, course_id, name, time, description):
        self.course_id = course_id
        self.name = name
        self.time = time
        self.description = description

    def __str__(self):
        return f"课程编号: {self.course_id}, 名称: {self.name}, 创建时间: {self.time}, 课程描述: {self.description}"


class MainApp:
    def main(self):
        # 创建教师对象
        teacher1 = Teacher("t001", "薛之谦", "男", 26, "python")
        teacher2 = Teacher("t002", "张碧晨", "女", 24, "PHP")
        teacher3 = Teacher("t003", "张杰", "男", 28, "python")

        # 创建课程对象
        course1 = Course("s001", "python", "2020-02-08", "python学科")
        course2 = Course("s002", "PHP", "2020-02-09", "PHP系统开发")

        # 打印每个教师对象的所有属性
        print(teacher1)
        print(teacher2)
        print(teacher3)

        # 打印每个课程对象的所有属性
        print(course1)
        print(course2)


if __name__ == "__main__":
    app = MainApp()
    app.main()



