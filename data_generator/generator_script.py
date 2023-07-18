import traceback

from config.database_connection import DataBaseConnector
import yaml
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.sql.expression import func
from sqlalchemy import select
from model.Model import Model
from data_generator.fake_data_generator import DataGenrator
from model.UserInterests import UserInterests
from faker import Faker
import logging

class FakeDataGenerator:
    def __init__(self):
        self._fake = Faker()
        self._email_set = set()
        self._count_duplicate = 0

    def generate_data(self, amount, table):
        try:
            connector = DataBaseConnector()
            source_session = connector.source_session
            source_engine = connector.source_engine

            if table == 'user_profile':
                self.user_profile_data_generator(connector, source_engine, source_session, amount)

            if table == 'user_interests':
                self.user_insterests_data_generetor(connector, source_engine, source_session, amount)

            print(f"committed successfully")
        except Exception as e:
            print(f"Exception occurred {e}, {traceback.print_exc()}")

        finally:
            source_session.close()

    def user_profile_data_generator(self, connector, source_engine, source_session, amount):
        metadata = MetaData()
        table = Table('user_profile', metadata, autoload_with=source_engine)
        max_id_query = text("SELECT MAX(id) FROM user_profile")
        result = source_session.execute(max_id_query)
        max_id = result.scalar()

        total_rows = max_id

        for i in range(total_rows+1, total_rows+amount+1):
            fake_obj = DataGenrator(self._fake, 20, 22, 20, 23)

            while fake_obj.email in self._email_set:
                self._count_duplicate = self._count_duplicate+1
                fake_obj = DataGenrator(self._fake, 20, 22, 20, 23)

            row_obj = Model(i, fake_obj.generate_bio(), fake_obj.generate_profile_description(), fake_obj.email, fake_obj.name, fake_obj.phone,  fake_obj.occupation, fake_obj.generate_random_location(), fake_obj.dob)
            self._email_set.add(fake_obj.email)

            insert_statement = table.insert().values(**row_obj.row_data)
            source_session.execute(insert_statement)
        logging.info(self._count_duplicate)

        source_session.commit()


    def user_insterests_data_generetor(self, connector, source_engine, source_session, amount):
        metadata = MetaData()
        table = Table('user_interests', metadata, autoload_with=source_engine)
        max_id_query = text("SELECT MAX(userid) FROM user_interests")
        result = source_session.execute(max_id_query)
        max_id = result.scalar()

        total_rows = max_id

        for i in range(total_rows+1, total_rows+amount+1):
            user_obj = UserInterests(i)
            insert_statement = table.insert().values(**user_obj.row_data)
            source_session.execute(insert_statement)
        source_session.commit()


if __name__ == "__main__":
    generate_data = FakeDataGenerator()
    generate_data.generate_data(amount=1)


