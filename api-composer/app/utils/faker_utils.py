from faker import Faker

fake = Faker()

def generate_fake_data(data_type: str):
    if data_type == "string":
        return fake.word()
    elif data_type == "number":
        return fake.random_number()
    elif data_type == "integer":
        return fake.random_int(min=1, max=100)
    elif data_type == "email":
        return fake.email()
    elif data_type == "date":
        return fake.date()
    else:
        return fake.word()
