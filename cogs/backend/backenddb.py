import os
import json
import random

class DiscordUser:
    def __init__(self, userID, userName, pseudonym, wishes):
        self.userID = userID
        self.pseudonym = pseudonym
        self.userName = userName
        self.wishes = wishes


class Database:
    def __init__(self, server):
        self.server = server
        self.save_path = "./cogs/jsonFiles/"
        self.full_path_file = os.path.join(self.save_path, f"{self.server}.json")
        self.full_path_file_pair = os.path.join(self.save_path, f"{self.server}")


    def write_file(self, data):
        if os.path.exists(self.full_path_file):
            exists = 'r'
        else:
            exists = 'w'


        with open(f"{self.full_path_file}", f'{exists}+') as file:
            try:
                data_base = json.load(file)
                cleaned_data = self.clean_data(data_base, data)
                cleaned_data[f"{self.server}"].append(data)
                print(cleaned_data)
                file.seek(0)
                json.dump(cleaned_data, file)
            except:
                placeholder = {
                        f"{self.server}":[
                            
                        ]
                    }
                json.dump(placeholder,file)
                file.seek(0)
                data_base = json.load(file)
                data_base[f"{self.server}"].append(data)
                file.seek(0)
                json.dump(data_base, file)


    def clean_data(self, main_data, data):
        for i in range(len(main_data[f'{self.server}'])):
            if main_data[f'{self.server}'][i]['userName'] == data['userName']:
                main_data[f'{self.server}'].pop(i)
                print(main_data)
        return main_data


    def add_person(self, userID, userName, pseudonym, wishes):
        data = DiscordUser(userID, userName, pseudonym, wishes)
        self.write_file(data.__dict__)



    def pair_people(self):
        with open(f"{self.full_path_file_pair}.json", 'r') as file:
            temporary_data = json.load(file)

        main_pair = self.randomize_pair(temporary_data)

        with open(f"{self.full_path_file_pair}-paired.json", 'w+') as file:
            json.dump(main_pair, file)



    def randomize_pair(self, temporary_data):
        first_pair_list = []
        second_pair_list = []
        final_pair = []

        main_data = temporary_data[f'{self.server}']

        for i in range(len(main_data)):
            if i % 2 == 0:
                first_pair = random.randint(0, len(main_data)-1)
                move_person = main_data.pop(first_pair)
                first_pair_list.append(move_person)
            else:
                second_pair = random.randint(0, len(main_data)-1)
                move_person = main_data.pop(second_pair)
                second_pair_list.append(move_person)

        for item in first_pair_list:
            random_second_pair = second_pair_list.pop(random.randint(0, len(second_pair_list)-1))
            holder = [item, random_second_pair]
            final_pair.append(holder)
        
        return final_pair


    def get_pair(self, userID):
        with open(f'{self.full_path_file_pair}-paired.json', 'r') as file:
            complete_data = json.load(file)

        print(complete_data)
        for outer_item in complete_data:
            if userID in outer_item[0].values() or userID in outer_item[1].values():
                for inner_item in outer_item:
                    if userID != inner_item['userID']:
                        return inner_item
                        break
           
        return False