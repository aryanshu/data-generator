from data_generator.generator_script import FakeDataGenerator

if __name__ == "__main__":
    generate_data = FakeDataGenerator()
    tables = ['user_profile','user_interests', 'swipe', 'user_image']

    for table in tables:
        generate_data.generate_data(amount=100, table=table)



