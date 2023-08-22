from flask_seeder import Seeder, Faker, generator
from app.models.user import User
import random


class UserSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=User,
            init={
                "id": generator.Sequence(),
                "name": generator.Name(),
                "email": generator.Email(),
                "password": "12345678",
                "role": random.choice(['user', 'admin']),
                "username": generator.Name().replace(' ',  '_')
            }
        )

        for user in faker.create(10):
            print(user)
            self.db.session.add(user)
