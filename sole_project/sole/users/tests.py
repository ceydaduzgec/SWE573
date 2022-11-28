from django.core.exceptions import ValidationError
from django.test import TestCase
from sole.users.factory import UserFactory


class UserAccountTests(TestCase):
    def test_new_superuser(self):
        super_user = UserFactory(
            email="testuser@super.com",
            username="johnnyjoe",
            first_name="Joe",
            password="aad3fa",
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
            password="aad3fa",
            is_active=False,
        )
        self.assertEqual(user.email, "testuser@user.com")
        self.assertEqual(user.username, "username")
        self.assertEqual(user.first_name, "firstname")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

    def test_empty_fields(self):
        with self.assertRaisesMessage(ValidationError, "'password': ['This field cannot be blank.']"):
            UserFactory(
                email="testuser@user.com",
                username="username1",
                first_name="first_name",
                password="",
            )
        with self.assertRaisesMessage(ValidationError, "'email': ['This field cannot be blank.']"):
            UserFactory(
                email="",
                username="username1",
                first_name="first_name",
                password="asdas12312",
            )
        with self.assertRaisesMessage(ValidationError, "'username': ['This field cannot be blank.']"):
            UserFactory(
                email="testuser@user.com",
                username="",
                first_name="first_name",
                password="asdas12312",
            )

    def test_username_regex(self):
        with self.assertRaisesMessage(
            ValidationError,
            "'username': ['Username is invalid. Only lowercase English letters, period and underscore characters are allowed. Minimum length is three characters.']",
        ):
            UserFactory(
                email="testuser@user.com",
                username="ASDSA",
                first_name="first_name",
                password="asdas12312",
            )
        with self.assertRaisesMessage(
            ValidationError,
            "'username': ['Username is invalid. Only lowercase English letters, period and underscore characters are allowed. Minimum length is three characters.']",
        ):
            UserFactory(
                email="testuser@user.com",
                username="ae",
                first_name="first_name",
                password="asdas12312",
            )
        with self.assertRaisesMessage(
            ValidationError,
            "'username': ['Username is invalid. Only lowercase English letters, period and underscore characters are allowed. Minimum length is three characters.']",
        ):
            UserFactory(
                email="testuser@user.com",
                username="ae",
                first_name="first_name",
                password="asdas12312",
            )

    def test_unique_fields(self):
        UserFactory(
            email="testuser@user.com",
            username="username1",
            first_name="first_name",
            password="asdasf",
        )
        with self.assertRaisesMessage(ValidationError, "'email': ['User with this Email already exists.']"):
            UserFactory(
                email="testuser@user.com",
                username="josy",
                first_name="Josh",
                password="asdsad",
            )
        with self.assertRaisesMessage(ValidationError, "'username': ['User with this Username already exists.']"):
            UserFactory(
                email="tesfs@user.com",
                username="username1",
                first_name="Josh",
                password="asdsad",
            )
