import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DataBaseConnector:
    def __init__(self, config_file_path="resources/application.yml"):
        self.config = self._load_config(config_file_path)
        self.source_engine = self._create_source_engine()
        self.source_session = self._create_source_session()

    def _load_config(self, file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def _create_source_engine(self):
        db_host_source = self.config['database_source']['hostname_source']
        db_name_source = self.config['database_source']['database_source']
        db_user_source = self.config['database_source']['username_source']
        db_password_source = self.config['database_source']['password_source']
        db_port_source = self.config['database_source']['port_id_source']

        source_db_url = f"postgresql://{db_user_source}:{db_password_source}@{db_host_source}:{db_port_source}/{db_name_source}"
        source_engine = create_engine(source_db_url)
        return source_engine

    def _create_source_session(self):
        SourceSession = sessionmaker(bind=self.source_engine)
        source_session = SourceSession()
        return source_session
