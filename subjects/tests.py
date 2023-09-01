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


def AddSubject():
    url = 'http://127.0.0.1:8000/subjects/add-subject/'
    subject_list = [
        {"id_subject": "sub00", "name": "Mathematics"},
        {"id_subject": "sub00", "name": "Physics"},
        {"id_subject": "sub00", "name": "Chemistry"},
        {"id_subject": "sub00", "name": "Biology"},
        {"id_subject": "sub00", "name": "History"},
        {"id_subject": "sub00", "name": "Geography"},
        {"id_subject": "sub00", "name": "English"},
        {"id_subject": "sub00", "name": "Computer Science"},
        {"id_subject": "sub00", "name": "Literature"},
        {"id_subject": "sub00", "name": "Physical Education"},
        {"id_subject": "sub00", "name": "homeroom"}
    ]

    header =Login("admin01", "123456")

    for subject_data in subject_list:
        response = requests.post(url, json=subject_data, headers= header)

        print(response.status_code, response.json())

if __name__ == '__main__':
    AddSubject()