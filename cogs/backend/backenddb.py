import os
import json

class Database:

    def __init__(self, server):
        self.server = server

    def write_file(self, data):
        save_path = "./cogs/jsonFiles/"
        full_path_file = os.path.join(save_path, f"{self.server}.json")
        with open(f"{full_path_file}", 'w+') as file:
            data = json.load(file)
            if f"{self.server}" in data.keys():
                data[f"{self.server}"].append(data)
                file.seek(0)
                file.dump(data)
            else:
                data[f"{self.server}"] = data
                file.seek(0)
                file.dump(data)


    def add_person(self, userID, userName, pseudonym, wishes):
        data =[
                {
                    "userName" : "",
                    "userID" : "",
                    "pseudonym" : "",
                    "wishes" : []
                }
            ]

        data[0]['userID'] = userID
        data[0]['userName'] = userName
        data[0]['pseudonym'] = pseudonym
        data[0]['wishes'] = [wish for wish in wishes]
        
        self.write_file(data)
