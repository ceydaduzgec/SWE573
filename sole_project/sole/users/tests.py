from django.test import TestCase
from sole.users.factory import UserFactory


class UserAccountTests(TestCase):
    def test_new_superuser(self):
        super_user = UserFactory(
            email="testuser@super.com",
            username="johnnyjoe",
            first_name="Joe",
            is_superuser=True,
            is_staff=True,
        )
        self.assertEqual(super_user.email, "testuser@super.com")
        self.assertEqual(super_user.username, "johnnyjoe")
        self.assertEqual(super_user.first_name, "Joe")
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "johnnyjoe")

    def test_new_user(self):
        user = UserFactory(
            email="testuser@user.com",
            username="username",
            first_name="firstname",
            is_active=False,
        )
        self.assertEqual(user.email, "testuser@user.com")
        self.assertEqual(user.username, "username")
        self.assertEqual(user.first_name, "firstname")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

    def test_empty_fields(self):  # TODO: correct required field
        UserFactory(
            email="",
            username="username1",
            first_name="first_name",
            password="password",
            is_superuser=True,
        )
