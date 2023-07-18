import random
from faker import Faker
from utils import constants

class UserInterests:
    def __init__(self, i):
        self.row_data = {}
        self.row_data['userid'] = i
        self.row_data["ayurveda"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["bollywood"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["classical_music"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["gym"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["sports"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["music"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["reading"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["hiking"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["cooking"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["dancing"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["photography"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["painting"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["gaming"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["traveling"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["movies"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["fashion"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["gardening"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["yoga"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["writing"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["cycling"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["swimming"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["pets"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["technology"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["meditation"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["food"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["volunteering"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["crafts"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["cricket"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["indian_cuisine"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["spirituality"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["history_and_culture"] = constants.binary_boolean_value[abs(hash(i))%2]
        self.row_data["regional_dance"] = constants.binary_boolean_value[abs(hash(i))%2]

