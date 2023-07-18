import random
from faker import Faker
from utils import constants

class Model:
    def __init__(self, i, bio, description, email, name, number, job, location, dob):
        self.row_data = {}
        self.row_data['id'] = i
        self.row_data['bio'] = bio
        self.row_data['children'] = constants.binary_value[abs(hash(i))%2]
        self.row_data['description'] = description
        self.row_data['diet'] = constants.diet[abs(hash(i)) % 3]
        self.row_data['dob'] = dob
        self.row_data['drink'] = constants.binary_value[abs(hash(i)) % 2]
        self.row_data['education'] = constants.education[abs(hash(i)) % 7]
        self.row_data['email'] = email
        self.row_data['exercise'] = constants.exercise[abs(hash(i)) % 4]
        self.row_data['first_name'] = str(name.split(" ")[-2])
        self.row_data['gender'] = constants.gender[abs(hash(i)) % 3]
        self.row_data['global'] = constants.glob[abs(hash(i)) % 2]
        self.row_data['higher_range'] = random.randint(25, 60)
        self.row_data['last_name'] = str(name.split(" ")[-1])
        self.row_data['location'] = location
        self.row_data['lower_range'] = random.randint(18, 25)
        self.row_data['maximum_distance'] = 50
        self.row_data['personality'] = constants.personality[abs(hash(i)) % 3]
        self.row_data['pets'] = constants.pets[abs(hash(i)) % 6]
        self.row_data['phone_number'] = f"+91 {number[3:]}"
        self.row_data['preferance'] = constants.preferance[abs(hash(i)) % 4]
        self.row_data['profile_score'] = random.randint(0, 10) / 10
        self.row_data['relation_goal'] = constants.relation_goal[abs(hash(i)) % 4]
        self.row_data['sleeping'] = constants.sleeping[abs(hash(i)) % 3]
        self.row_data['smoke'] = constants.smoke[abs(hash(i)) % 3]
        self.row_data['star_sign'] = constants.star_sign[abs(hash(i)) % 12]
        self.row_data['status'] = constants.status[abs(hash(i)) % 5]
        self.row_data['vaccinated'] = constants.vaccinated[abs(hash(i)) % 4]
        self.row_data['work_at'] = job

