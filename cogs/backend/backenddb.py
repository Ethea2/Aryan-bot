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

    def write_file(self, data):
        save_path = "./cogs/jsonFiles/"
        full_path_file = os.path.join(save_path, f"{self.server}.json")

        with open(f"{full_path_file}", f'w+') as file:
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
        save_path = "./cogs/jsonFiles/"
        full_path_file = os.path.join(save_path, f"{self.server}")

        with open(f"{full_path_file}.json", 'r') as file:
            temporary_data = json.load(file)

        main_pair = self.randomize_pair(temporary_data)

        with open(f"{full_path_file}-paired.json", 'w+') as file:
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
            random_second_pair = random.randint(0, len(second_pair_list)-1)
            holder = [item, second_pair_list[random_second_pair]]
            final_pair.append(holder)
        
        return final_pair