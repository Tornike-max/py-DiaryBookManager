import sys
import json


from diarybook import Diary, DiaryBook
from utils import read_from_json_into_app


class Menu:

    def __init__(self):
        self.diarybook = DiaryBook()

        print(self.diarybook)

        self.choises = {
            "1": self.show_all_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.sort_by,
            '5': self.quit
        }

    def show_all_diaries(self):

        if len(self.diarybook.diaries) == 0:
            print("No diaries available")
        else:
            for diary in self.diarybook.diaries:
                print(f"{diary.id} - {diary.memo}")

    def add_diary(self):
        memo = input("Enter a memo: ")
        tags = input("Enter Tags")

        file_name = input('Enter File name to create new user data')

        user_file = f'{file_name}.json'

        new_diary = {
            'memo': memo,
            'tags': tags
        }

        try:
            with open(user_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(new_diary)

        with open(user_file, 'w') as file:
            json.dump(data, file, indent=4)

        print("Your note has been added successfully")

        self.diarybook.new_diary(memo, tags)
        print("Your note has been added successfully")

    def search_diaries(self):
        keyword = input("Enter a keyword")
        filtered_diaries = self.diarybook.search_diary(keyword)
        if len(filtered_diaries) == 0:
            print("We couldn't find any diaries'")
        else:

            for diary in filtered_diaries:
                print(f"{diary.id} - {diary.memo}")

    def populate_database(self):
        diaries = read_from_json_into_app("data.json")
        for diary in diaries:
            self.diarybook.diaries.append(diary)

    def sort_by(self):
        # ვკითხულობთ დეითას რომელიც არის data.json-ში და დეითას, რომელიც იქ არის ვანიჭებთ ცვლადს რომელიც არის data.
        # შემდეგ ვქმნით ახალ ფაილს სადაც სორტირებას ვაკეთებთ.
        with open('data.json', 'r') as file:
            data = json.load(file)

        sorted_data = sorted(data, key=lambda x: x['memo'])

        with open('sorted.json', 'w') as file:
            json.dump(sorted_data, file, indent=4)

    def quit(self):
        print('Thanks for using our diarybook')
        sys.exit(0)

    def display_menu(self):
        print("""
              1:Show Diaries
              2:Add Diary
              3:Filter Using keyword 
              4:Sort by id
              5:Quit program
              """)

    def run(self):
        self.register_user()
        while self.login_user() == True:
            self.populate_database()
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choises.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def register_user(self):
        print('Register User')
        email = input('Enter your email address: ')
        password = input('Enter your password: ')

        new_user = {
            'email': email,
            'password': password
        }

        filename = "register.json"

        try:
            with open(filename, 'r') as file:
                existing_users = json.load(file)
        except FileNotFoundError:
            existing_users = []

        existing_users.append(new_user)

        with open(filename, 'w') as file:
            json.dump(existing_users, file, indent=4)

        print("Your registration has been completed successfully")

    def login_user(self):
        print('Login User')
        email = input('Enter your email address: ')
        password = input('Enter your password: ')

        with open('register.json', 'r') as file:
            user_data = json.load(file)

        for user in user_data:
            if email == user['email'] and password == user['password']:
                print('User successfully logged in')
                return True

        print('Error while logging in. Incorrect email or password.')
        return False


if __name__ == '__main__':
    Menu().run()
