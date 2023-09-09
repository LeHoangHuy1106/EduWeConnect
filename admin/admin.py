import datetime
import random
import string

import requests


from users.tests import Test_AddStudent


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


def display_menu():
    print("\nPlease choose an option:")
    print("1. Add student")
    print("2. Add teacher")
    print("3. add teacher, student join in classs")
    print("4. create announcement")
    print("5. Exit")

def say_hello():
    print("Hello, User!")
    return_to_menu()

def display_datetime():
    now = datetime.datetime.now()
    print("Current Date and Time:", now.strftime('%Y-%m-%d %H:%M:%S'))
    return_to_menu()

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
            display_datetime()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


def AddStudents():
    # add student năm 2020
    username = "admin01"
    password = "123456"
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
    admission_year = input("admission_year")

    student= {
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

    Test_AddStudent(username, password, student)
    return_to_menu()





if __name__ == "__main__":
    main()

