from faker import Faker
from datetime import datetime
import random


class DataGenrator:
    def __init__(self, fake, min_latitude, max_latitude, min_longitude, max_longitude):
        self.fake = fake
        self._name = self.fake.name()
        self._age = self.fake.random_int(min=18, max=70)
        self._location = self.fake.city()
        self._occupation = self.fake.job()
        self._interests = self.fake.random_elements(elements=('Technology', 'Sports', 'Music', 'Art', 'Travel'), length=3)
        self._dob = self.fake.date_between_dates(date_start=datetime(1980, 1, 1), date_end=datetime(2004, 12, 31))
        self._email = self.fake.email()
        self._min_latitude = min_latitude
        self._max_latitude = max_latitude
        self._min_longitude = min_longitude
        self._max_longitude = max_longitude
        self._phone_number = self.fake.phone_number()

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone_number

    @property
    def age(self):
        return self._age

    @property
    def location(self):
        return self._location

    @property
    def occupation(self):
        return self._occupation

    @property
    def interests(self):
        return self._interests

    @property
    def email(self):
        return self._email

    @property
    def dob(self):
        return self._dob

    def generate_profile_description(self):
        description = f"Hi, I'm {self.name}! I'm {self.age} years old and I live in {self.location}.Currently, I work as a {self.occupation}. My main interests include {', '.join(self.interests)}. Feel free to reach out to me if you share any of these passions!"
        return description

    def generate_bio(self):
        bio = f"{self.name}, {self.age}, {self.location}, {self.occupation}"
        return bio[:100]

    def generate_random_location(self):
        latitude = random.uniform(self._min_latitude, self._max_latitude)
        longitude = random.uniform(self._min_longitude, self._max_longitude)
        location = f"lat:{latitude} long:{longitude}"
        return location







