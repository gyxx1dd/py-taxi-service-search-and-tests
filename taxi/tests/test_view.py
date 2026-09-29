from django.test import TestCase
from django.urls import reverse


class PublicViewTest(TestCase):
    def test_access_to_private_car_list(self):
        url = reverse("taxi:manufacturer-list")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

