from django.test import TestCase
from django.contrib.auth.models import User

from user.models import Profile


class ProfileModelTestCase(TestCase):
    databases = {"test"}

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        self.profile = Profile.objects.create(
            user=self.user,
            date_of_birth="1990-01-01",
            photo="users/2023/10/14/test.jpg",
            street="teststreet",
            apartment="test123",
            city="testcity",
            postal_code="66-200",
            state="teststate",
            country="testcountry",
        )

    def test_str_rep(self):
        expected_str = "testuser's profile"
        actual_str = str(self.profile)
        self.assertEqual(actual_str, expected_str)

    def tearDown(self) -> None:
        return super().tearDown()
