import requests
import random
import string

"""Student"""
def Test_login(username, password):

    url = 'http://127.0.0.1:8000/users/accounts/login/'

    # Thay thế bằng thông tin đăng nhập của tài khoản admin
    login_data = {
        "username": f"{username}",
        "password": f"{password}"
    }

    # Đăng nhập và lấy access token
    response_login = requests.post(url, json=login_data)
    print(response_login.json().get('message'))
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
def Test_Change_password(username, password):
    url = f'http://127.0.0.1:8000/users/accounts/change-password/{username}/'

    headers = Login(username, password)
    data = {
        "old_password": "0123456789",
        "new_password": "123456"
    }

    response = requests.put(url, json=data, headers=headers)
    response_json = response.json()  # Chuyển phản hồi thành dạng JSON
    print(response_json)  # In phản hồi JSON ra màn hình
def Test_Get_List_Student(username, password):
    url = 'http://127.0.0.1:8000/users/students/get-list-student/'
    headers = Login(username, password)
    # Gửi yêu cầu GET để lấy danh sách học sinh
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.json())
def Test_Get_detail_student_by_usename(username, password):
    url = 'http://127.0.0.1:8000/users/students/detail/hs20210003/'
    headers = Login(username, password)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.json())
def Test_AddStudent(username, password, student_data):
    url = 'http://127.0.0.1:8000/users/students/create/'
    headers = Login(username, password)
    # Thay thế bằng dữ liệu tạo học sinh tương ứng
    response = requests.post(url, json=student_data, headers=headers)
    print(response.status_code)
    print(response.json())
"""Teacher"""
def Test_AddTeacher(username, password, student_data):
    url = 'http://127.0.0.1:8000/users/teachers/create/'
    headers = Login(username, password)
    # Thay thế bằng dữ liệu tạo học sinh tương ứng
    response = requests.post(url, json=student_data, headers=headers)
    print(response.status_code)
    print(response.json())
##############DATA##################
def Create_List_Student_Data(admission_year,n):
    student_data_list = []
    for i in range(n):
        username = "username"
        first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
        last_name = ''.join(random.choices(string.ascii_uppercase, k=7))
        email = f"{username}@example.com"
        password = "password"
        gender = random.choice(['Male', 'Female'])
        phone_number = '0123456789'
        id_card = ''.join(random.choices(string.digits, k=9))
        birth_date = f"{random.randint(1980, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        address = f"{random.randint(1, 100)} {random.choice(['Street', 'Avenue'])}, {random.choice(['City', 'Town'])}"
        admission_year = admission_year

        data = {
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

        student_data_list.append(data)

    return student_data_list
def create_List_Teacher_data(hire_year, n):
    data =[]
    for i in range(n):
        username = "teacher"
        first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
        last_name = ''.join(random.choices(string.ascii_uppercase, k=7))
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
        data.append(teacher_data)

    return data

def AddTeachers():
    # add student năm 2020
    username = "admin01"
    password = "123456"
    list_teacher_data = create_List_Teacher_data(2020,5)
    for teacher in list_teacher_data:
        Test_AddTeacher(username, password, teacher)
def AddStudents():
    # add student năm 2020
    username = "admin01"
    password = "123456"
    list_student_data = Create_List_Student_Data(2020,5)
    for student in list_student_data:
        Test_AddStudent(username, password, student)

    # add student năm 2021
    username = "admin01"
    password = "123456"
    list_student_data = Create_List_Student_Data(2021,5)
    for student in list_student_data:
        Test_AddStudent(username, password, student)
if __name__ == '__main__':
    """test add list student"""
    # AddStudents()
    """ test login"""
    username = "hs20200002"
    password =  "123456"

    # not exist account
    # Test_login(username,password)
    # change password in first login
    # Test_Change_password(username,password)

    """ get detail student"""
    username = "gv20200002"
    password = "123456"
    # Test_Get_List_Student(username, password)
    # Test_Get_detail_student_by_usename(username, password)
    """test add list student"""
    # AddTeachers()
    # not exist account
    # username = "gv20200001"
    # password = "0123456789"
    Test_login(username,password)
    # change password in first login
    # username = "gv20200001"
    # password = "0123456789"
    # Test_Change_password(username,password)


