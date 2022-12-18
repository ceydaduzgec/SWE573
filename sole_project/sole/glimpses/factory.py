import factory
import factory.fuzzy
from django.utils.timezone import utc
from factory.django import DjangoModelFactory
from factory.faker import faker
from sole.glimpses.models import Glimpse
from sole.users.factory import UserFactory

FAKE = faker.Faker()


class GlimpseFactory(DjangoModelFactory):
    class Meta:
        model = Glimpse

    title = factory.fuzzy.FuzzyText(length=50)
    description = factory.fuzzy.FuzzyText(length=255)
    url = factory.Faker("url")
    status = factory.fuzzy.FuzzyChoice(Glimpse.Status.choices)

    author = factory.SubFactory(UserFactory)
    creation_datetime = factory.Faker("date_time", tzinfo=utc)
    update_datetime = factory.Faker("date_time", tzinfo=utc)
