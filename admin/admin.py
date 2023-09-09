import datetime
import random
import string

import requests




def Login(username, password):
    url = 'http://127.0.0.1:8000/users/accounts/login/'

    # Thay thế bằng thông tin đăng nhập của tài khoản admin
    login_data = {
        "username": f"{username}",
        "password": f"{password}"
    }

    # Đăng nhập và lấy access token
    response_login = requests.post(url, json=login_data)
    access_token = response_login.json().get('access_token')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    return headers

def Test_AddStudent(username, password, student_data):
    url = 'http://127.0.0.1:8000/users/students/create/'
    headers = Login(username, password)
    # Thay thế bằng dữ liệu tạo học sinh tương ứng
    response = requests.post(url, json=student_data, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_AddTeacher(username, password, student_data):
    url = 'http://127.0.0.1:8000/users/teachers/create/'
    headers = Login(username, password)
    # Thay thế bằng dữ liệu tạo học sinh tương ứng
    response = requests.post(url, json=student_data, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_add_teacher_join_classroom (username, password, classroom_id,username_teacher):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/add-teachers/"
    headers = Login(username, password)
    data = {
                "teachers": [username_teacher]
            }
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_add_student_join_classroom (username, password, classroom_id,username_student):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/add-students/"
    headers = Login(username, password)
    data = {
                "students": [username_student]
            }
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_create_announcement(username, password):
    url = f"http://127.0.0.1:8000/announcement/add/"
    headers = Login(username, password)
    data ={
        "title": input("title:"),
        "creation_date": "2023-09-11T11:20:30Z",
        "content": input("content:")
    }
    response = requests.post(url,  headers=headers, json=data)
    print(response.status_code)
    print(response.json())



def display_menu():
    print("\nPlease choose an option:")
    print("1. Add student")
    print("2. Add teacher")
    print("3. add teacher join in classs")
    print("4. add student join in classs")
    print("5. create announcement")



def return_to_menu():
    input("Press '0' to return to the main menu...")
    # Note: You can also add error handling here to ensure that the user only enters '0'.

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            AddStudents()
        elif choice == "2":
            AddTeacher()
        elif choice == "3":
            AddTeacherJoinInClass()
            break
        elif choice == "4":
            AddStudentJoinInClass()
            break
        elif choice == "5":
            CreateAnnouncement()
            break
        else:
            print("Invalid choice. Please choose again.")


def AddTeacherJoinInClass():
    username = "admin01"
    password = "123456"
    classroom_id = input("class id (vd: class00002):")
    teacher_id = input("username teacher (vd:gv20200002):")
    Test_add_teacher_join_classroom(username, password, classroom_id, teacher_id)
    return_to_menu()


def AddStudentJoinInClass():
    username = "admin01"
    password = "123456"
    classroom_id = input("class id (vd: class00002):")
    student_id = input("username student (vd:hs20200001:)")
    Test_add_student_join_classroom(username, password, classroom_id, student_id)
    return_to_menu()



def AddStudents():
    # add student năm 2020

    username = "username"
    first_name = input("first name:")
    last_name = input("class name:")
    email = f"{username}@example.com"
    password = "password"
    gender = random.choice(['Male', 'Female'])
    phone_number = '0123456789'
    id_card = ''.join(random.choices(string.digits, k=9))
    birth_date = f"{random.randint(1980, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    address = f"{random.randint(1, 100)} {random.choice(['Street', 'Avenue'])}, {random.choice(['City', 'Town'])}"
    admission_year = input("admission_year:")

    student = {
            "user": {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password
            },
            "gender": gender,
            "phone_number": phone_number,
            "id_card": id_card,
            "birth_date": birth_date,
            "address": address,
            "admission_year": admission_year
        }
    username = "admin01"
    password = "123456"
    Test_AddStudent(username, password, student)
    return_to_menu()

def AddTeacher():

    username = "teacher"
    first_name = input("first name:")
    last_name = input("clast name:")
    hire_year = int(input("hire year:"))
    email = f"{username}@example.com"
    password = "password"
    gender = random.choice(['Male', 'Female'])
    phone_number = '0123456789'
    id_card = ''.join(random.choices(string.digits, k=9))
    birth_date = f"{random.randint(1980, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    address = f"{random.randint(1, 100)} {random.choice(['Street', 'Avenue'])}, {random.choice(['City', 'Town'])}"
    hire_date = f"{hire_year}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    years_of_experience = random.randint(0, 20)
    graduation_school = "Graduation School"
    specialized_subject = "Specialized Subject"

    teacher_data = {
        "user": {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        },
        "gender": gender,
        "phone_number": phone_number,
        "id_card": id_card,
        "birth_date": birth_date,
        "address": address,
        "hire_date": hire_date,
        "years_of_experience": years_of_experience,
        "graduation_school": graduation_school,
        "specialized_subject": specialized_subject
    }




    username = "admin01"
    password = "123456"
    Test_AddTeacher(username, password, teacher_data)
    return_to_menu()

def CreateAnnouncement():
    username  ="admin01"
    password = "123456"
    Test_create_announcement(username, password)
if __name__ == "__main__":
    main()

