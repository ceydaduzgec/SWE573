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

    def tearDown(self):
        super().tearDown()

    def test_create_glimpse(self):
        form_data = {
            "title": "New Glimpse Test",
            "text": "This is a description.",
            "url": "This is really important.",
            "status": Glimpse.Status.PUBLIC,
        }
        url = reverse("glimpses:create")
        self.client.force_login(user=self.user)
        response = self.client.post(url, data=form_data, follow=True)
        self.assertEquals(response.status_code, 200)
