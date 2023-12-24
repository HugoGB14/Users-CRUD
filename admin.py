import json

class admin:
    def __init__(self, filename):
        self.filename = filename
    def load_data(self):
        with open(self.filename, 'r') as file:
            self.data = json.load(file)
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
    def ret_user(self, id):
        return self.data[id]
    def add_user(self, user_data):
        self.data.append(user_data)
        self.save_data()

    def update_user(self, username, new_data):
        for user in self.data:
            if user["Username"] == username:
                user.update(new_data)
                self.save_data()
                break

    def remove_user(self, username):
        self.data = [user for user in self.data if user["Username"] != username]
        self.save_data()