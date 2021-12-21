import os
import json

class DiscordUser:
    def __init__(self, userID, userName, pseudonym, wishes):
        self.userID = userID
        self.pseudonym = pseudonym
        self.userName = userName
        self.wishes = wishes


class Database:
    def __init__(self, server):
        self.server = server

    def write_file(self, data):
        save_path = "./cogs/jsonFiles/"
        full_path_file = os.path.join(save_path, f"{self.server}.json")
        with open(f"{full_path_file}", 'w+') as file:
            if os.stat(full_path_file).st_size == 0:
                placeholder = {
                    f"{self.server}":[
                        
                    ]
                }
                json.dump(placeholder,file)
                file.seek(0)
                print("FILE FUCKIGN EMPTY?!?!")
            data_base = json.load(file)
            print(data_base)
           # if f"{self.server}" in data_base.keys():
            data_base[f"{self.server}"].append(data)
            file.seek(0)
            json.dump(data_base, file)
           # else:
           #     data_base[f"{self.server}"].append(data)
           #     file.seek(0)
           #     json.dump(data, file)


    def add_person(self, userID, userName, pseudonym, wishes):
        data = DiscordUser(userID, userName, pseudonym, wishes)
        self.write_file(data.__dict__)

