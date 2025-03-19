class User:
    def __init__(self, name: str, email: str, password: str):
        self.__name = name
        self.__email = email
        self.__password = password


    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name: str):
        self.__name = name

    def set_email(self, email: str):
        self.__email = email

    def set_password(self, password: str):
        self.__password = password


user = User("Іван", "ivan@example.com", "securepassword123")

user.set_name("Петро")
user.set_email("petro@example.com")
user.set_password("newpassword456")

print("Ім'я:", user.get_name())
print("Електронна пошта:", user.get_email())
print("Пароль:", user.get_password())
