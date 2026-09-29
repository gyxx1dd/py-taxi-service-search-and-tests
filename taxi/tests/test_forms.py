from django.test import TestCase

from taxi.forms import CarForm, DriverUserSearchForm, CarSearchForm, ManufacturesSearchForm, DriverCreationForm
from taxi.models import Manufacturer, Car, Driver


class CarFormTest(TestCase):
    def test_car_form_create(self):
        manufactur = Manufacturer.objects.create(name="Zavod", country="Zavod")
        Driver.objects.create(
            username="vasia",
            password="123123",
        )
        driver = Driver.objects.all()
        form_data = {
            "model": "Haip",
            "manufacturer": manufactur,
            "drivers": driver,
        }

        form = CarForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(list(form.cleaned_data),
                         list(form_data))


class SearchTest(TestCase):
    def test_search_driver(self):
        data = {
            "username": "vania",
        }

        form = DriverUserSearchForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)

    def test_search_car(self):
        data = {
            "model": "bmw",
        }

        form = CarSearchForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)

    def test_search_manufacture(self):
        data = {
            "name": "zavod",
        }

        form = ManufacturesSearchForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)


class DriverCreateTest(TestCase):
    def test_create_car(self):
        data = {
            "username": "vasia",
            "license_number": "NGH2222",
            "first_name": "vasia",
            "last_name": "vasia",
            "password1": "123",
            "password2": "123",
        }

        data2 = {
            "username": "vasia",
            "first_name": "vasia",
            "last_name": "vasia",
            "password1": "123",
        }

        form = DriverCreationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.cleaned_data, data2)
