import factory
import factory.fuzzy
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from factory.faker import faker

User = get_user_model()
FAKE = faker.Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: "user{}@gmail.com".format(n))
    username = factory.Sequence(lambda n: "user{}".format(n))
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_active = True
    is_staff = False
    is_superuser = False
