import random
from datetime import datetime
from faker import Faker
import data

faker = Faker('ru_RU')

def create_user_credentials():
    first_name = faker.first_name()  # Генерация имени
    last_name = faker.last_name()  # Генерация фамилии
    phone_number = f"+7{faker.random_number(digits=10)}"  # Генерация телефона
    return first_name, last_name, phone_number  # Возвращаем кортеж (first_name, last_name, phone_number)

def create_data(start_year=2025, end_year=2025):# Генерация случайной даты
    start_date = datetime(start_year, 4, 3)
    end_date = datetime(end_year, 5, 29)

    random_date = faker.date_between(start_date=start_date, end_date=end_date)
    return random_date.strftime('%d.%m.%Y')

#Выбор рандомной улицы и номера дома
def generate_random_address():
    street = random.choice(data.Addresses.addresses)
    house_number = random.randint(1, 100)
    return f"{street}, д.{house_number}"

#Выбор случайной  станции метрро из списка
def generate_random_metro_station():
    stantion = random.choice(data.MetroStantions.metro_stantions)
    return stantion






