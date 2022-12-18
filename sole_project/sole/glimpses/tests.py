from django.test import TestCase
from django.urls import reverse
from sole.glimpses.models import Glimpse
from sole.users.factory import UserFactory


class GlimpseTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = UserFactory(
            email="testuser@super.com",
            username="johnnyjoe",
            first_name="Joe",
            password="aad3fa",
        )
        cls.user.set_password("aad3fa")
        cls.user.save()

    def tearDown(self):
        super().tearDown()

    def test_create_glimpse(self):
        form_data = {
            "title": "New Glimpse Test",
            "description": "This is a description.",
            "url": "This is really important.",
            "status": Glimpse.Status.PUBLIC,
        }

        login = self.client.login(username="johnnyjoe", password="aad3fa")
        self.assertTrue(login, "Could not log in")

        response = self.client.post(reverse("glimpses:create"), data=form_data, follow=True)
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(Glimpse.objects.last().title, "New Glimpse Test")
