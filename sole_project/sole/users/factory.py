import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from factory.faker import faker

from .models import User

FAKE = faker.Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Sequence(lambda n: "person{}".format(n))
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
