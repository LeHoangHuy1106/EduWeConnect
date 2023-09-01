import requests
from faker import Faker
import random
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




fake = Faker()

def create_data_classroom(n):
    classroom_data = []

    for i in range(5):
        class_id = "class_id"
        subject_id = "sub001"
        info = fake.paragraph()
        is_active = True

        classroom = {
            "class_id": class_id,
            "teachers": [],
            "students": [],
            "subject": subject_id,
            "info": info,
            "is_active": is_active
        }

        classroom_data.append(classroom)
    return classroom_data


def Test_AddClassRoom(username, password, data):
    url = 'http://127.0.0.1:8000/classroom/add-classroom'
    headers = Login(username, password)
    # Thay thế bằng dữ liệu tạo học sinh tương ứng
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.json())


def Test_update_info_classroom (username, password, classroom_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/update-info/"
    headers = Login(username, password)
    data = {
              "info": "Updated classroom information"
            }
    response = requests.put(url, json=data, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_deactivate_classroom (username, password, classroom_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/deactivate/"
    headers = Login(username, password)
    data = {
              "is_active": False
            }
    response = requests.put(url, json=data, headers=headers)
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

def Test_get_list_class_student_join (username, password):
    url = f"http://127.0.0.1:8000/classroom/list-classrooms/"
    headers = Login(username, password)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_get_list_active_class_student_join (username, password):
    url = f"http://127.0.0.1:8000/classroom/list-active-classrooms/"
    headers = Login(username, password)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.json())


def Test_get_list_active_class_student_join (username, password):
    url = f"http://127.0.0.1:8000/classroom/list-active-classrooms/"
    headers = Login(username, password)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_get_list_deactive_class_student_join (username, password):
    url = f"http://127.0.0.1:8000/classroom/list-deactive-classrooms/"
    headers = Login(username, password)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_get_student_join_classroom (username, password, classroom_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/students/"
    headers = Login(username, password)
    response = requests.get(url,  headers=headers)
    print(response.status_code)
    print(response.json())

def Test_get_teacher_join_classroom (username, password, classroom_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/teachers/"
    headers = Login(username, password)
    response = requests.get(url,  headers=headers)
    print(response.status_code)
    print(response.json())

def Test_create_posst_in_class (username, password, classroom_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/create-post/"
    headers = Login(username, password)
    data = {
              "post_id": "id_post",
              "content": fake.paragraph(),
              "author": 1,
              "created_date": "2023-08-31T10:00:00Z",
              "likes": [],
              "classroom": "class_id",
              "is_edited": False
}
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_edit_posst_in_class (username, password, classroom_id, post_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/update-post/{post_id}/"
    headers = Login(username, password)
    data = {
              "content": fake.paragraph(),
}
    response = requests.put(url, json=data, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_delete_posst_in_class (username, password, classroom_id, post_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/delete-post/{post_id}/"
    headers = Login(username, password)
    response = requests.delete(url,  headers=headers)
    print(response.status_code)
    print(response.json())

def Test_like_posst_in_class (username, password, classroom_id, post_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/like/{post_id}/"
    headers = Login(username, password)
    response = requests.post(url,  headers=headers)
    print(response.status_code)
    print(response.json())


def Test_get_post_in_class (username, password, classroom_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/posts/"
    headers = Login(username, password)
    response = requests.get(url,  headers=headers)
    print(response.status_code)
    print(response.json())

def Test_get_listlike_posst_in_class (username, password, classroom_id, post_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/{post_id}/liked-users/"
    headers = Login(username, password)
    response = requests.get(url,  headers=headers)
    print(response.status_code)
    print(response.json())

def Test_comment_post (username, password, classroom_id, post_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/{post_id}/create-comment/"
    headers = Login(username, password)
    data = {
            "comment_id": "id",
            "content": fake.paragraph(),
            "author": 1,
            "created_date": "2023-08-31T12:00:00Z",
            "post": "post12345"
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_get_comment_post (username, password, classroom_id, post_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/{post_id}/comments/"
    headers = Login(username, password)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.json())

def Test_create_score (username, password, classroom_id, student_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/student/{student_id}/add-score/"
    headers = Login(username, password)
    data = {
          "student": "student_id",
          "classroom": "classroom_id",
          "score_system_1": "8.5,7.0,9.5",
          "score_system_2": "[9.0,8.0,7.5]",
          "score_system_3": "8.8"
        }
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)

    print(response.json())

def Test_get_score_student (username, password, student_id, year, semester):

    url = f"http://127.0.0.1:8000/classroom/student/{student_id}/scores/{year}/{semester}/"
    headers = Login(username, password)
    response = requests.get(url,  headers=headers)
    print(response.status_code)
    print(response.json())

def Test_get_score_class (username, password, classroom_id):
    url = f"http://127.0.0.1:8000/classroom/{classroom_id}/student/list-scores/"
    headers = Login(username, password)
    response = requests.get(url,  headers=headers)
    print(response.status_code)
    print(response.json())

def Add_ClassRoom():
    username = "admin01"
    password = "123456"
    list = create_data_classroom(5)
    for data in list:
        Test_AddClassRoom(username, password, data)

def ChangeInfoClassroom():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_update_info_classroom(username, password, classroom_id)

def DeactivateClassroom():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_deactivate_classroom(username, password, classroom_id)

def AddTeacherJoinInClass():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_add_teacher_join_classroom(username, password, classroom_id, 'gv20200001')


def AddStudentJoinInClass():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_add_student_join_classroom(username, password, classroom_id, 'hs20200001')
    Test_add_student_join_classroom(username, password, classroom_id, 'hs20200002')
    Test_add_student_join_classroom(username, password, classroom_id, 'hs20200003')
    Test_add_student_join_classroom(username, password, classroom_id, 'hs20200004')
def GetListClassJoinIn():
    username = "admin01"
    password = "123456"
    Test_get_list_class_student_join(username, password)
    print("======================")
    username = "hs20200001"
    password = "123456"
    Test_get_list_class_student_join(username, password)

def GetListAtiveClassJoinIn():

    print("======================")
    username = "admin01"
    password = "123456"
    Test_get_list_active_class_student_join(username, password)


def GetListDeAtiveClassJoinIn():

    print("======================")
    username = "admin01"
    password = "123456"
    Test_get_list_deactive_class_student_join(username, password)

def GetStudentJoinClass():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_get_student_join_classroom(username, password, classroom_id)

def GetTeacherJoinClass():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_get_teacher_join_classroom(username, password, classroom_id)

def CreatePost():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_create_posst_in_class(username, password, classroom_id)

def EditPost():
    username = "hs20200001"
    password = "123456"
    classroom_id = "class00001"
    post_id ="postclass0000100002"
    Test_edit_posst_in_class(username, password, classroom_id,post_id)
def DeletePost():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    post_id ="postclass0000100001"
    Test_delete_posst_in_class (username, password, classroom_id,post_id)
def LikePost():
    username = "gv20200002"
    password = "123456"
    classroom_id = "class00001"
    post_id ="postclass0000100001"
    Test_like_posst_in_class (username, password, classroom_id,post_id)

def GetPost():
    username = "hs20200001"
    password = "123456"
    classroom_id = "class00001"
    Test_get_post_in_class(username, password, classroom_id)

def GetListLikePost():
    username = "hs20200001"
    password = "123456"
    classroom_id = "class00001"
    post_id ="postclass0000100001"
    Test_get_listlike_posst_in_class (username, password, classroom_id,post_id)

def AddComment():
    username = "gv20200002"
    password = "123456"
    classroom_id = "class00001"
    post_id ="postclass0000100002"
    Test_comment_post(username, password, classroom_id,post_id)


def GetComment():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    post_id = "postclass0000100002"
    Test_get_comment_post(username, password, classroom_id, post_id)

def CreateScore():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    student_id= "hs20200001"
    Test_create_score(username, password, classroom_id, student_id)

def GetScore():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_get_score_class (username, password, classroom_id)

def GetScoreClass():
    username = "admin01"
    password = "123456"
    classroom_id = "class00001"
    Test_get_score_class(username, password, classroom_id)

def GetScoreStudent():
    username = "admin01"
    password = "123456"
    student_id= "hs20200001"
    year = '2023'
    semester = "1"
    Test_get_score_student (username, password, student_id, year, semester)

if __name__ == '__main__':
    # Add_ClassRoom()
    # ChangeInfoClassroom()
    # DeactivateClassroom()
    # AddTeacherJoinInClass()
    # AddStudentJoinInClass()
    # GetListClassJoinIn()
    # GetListAtiveClassJoinIn()
    # GetListDeAtiveClassJoinIn()
    # GetStudentJoinClass()
    # print("---")
    # GetTeacherJoinClass()
    # CreatePost()
    # EditPost()
    # DeletePost()
    # LikePost()
    # GetPost()
    # # GetListLikePost()
    AddComment()
    # GetComment()
    # CreateScore()
    # GetScore()
    # GetScoreStudent()