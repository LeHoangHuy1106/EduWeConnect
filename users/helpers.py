from django.contrib.auth.models import User


# Trong quá trình thêm giáo viên
def create_teacher_account(user_data, graduation_year, current_teacher_count):
    # Tạo username theo quy tắc
    username = f"gv{graduation_year}{current_teacher_count + 1:04}"

    # Tạo password mặc định là số điện thoại
    password = user_data['phone_number']

    # Tạo tài khoản User
    user = User.objects.create_user(username=username, password=password, is_active=False, **user_data)

    return user

def create_student_account(user_data, admission_year, current_student_count):
    # Tạo username theo quy tắc
    username = f"hs{admission_year}{current_student_count + 1:04}"

    # Tạo password mặc định là số điện thoại
    password = user_data.pop('phone_number', '')  # Loại bỏ phone_number khỏi user_data
    user_data['is_active'] = False  # Mặc định tài khoản là không kích hoạt
    # Tạo tài khoản User
    user = User.objects.create_user(username=username, password=password, **user_data)
    return user