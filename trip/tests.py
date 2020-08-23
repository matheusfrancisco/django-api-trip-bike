import json
from django.contrib.auth import get_user_model
from django.urls import reverse
from model_bakery import baker

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Trip
from .serializers import TravelSerialization
# Create your tests here.


class BaseViewTest(APITestCase):
    client = APIClient()

    def login_client(self, username="", password=""):
        response = self.client.post(
            reverse("create-token"),
            data=json.dumps(
                {
                    'username': username,
                    'password': password
                }
            ),
            content_type='application/json'
        )
        self.token = response.data['token']
        # set the token in the header
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token

    def setUp(self):
        User = get_user_model()
        self.user_to_filter = User.objects.create_superuser(
            "temporary",
            "temporary@gmail.com",
            "temporary"
        )
        user_fake = User.objects.create_superuser(
            "temporaryy",
            "temporaryy@gmail.com",
            "temporaryy"
        )
        baker.make(
            Trip,
            user=self.user_to_filter,
            _quantity=10,
            classification=1,
        )
        baker.make(
            Trip,
            user=user_fake,
            _quantity=10,
            classification=1,
        )


class GetTripTest(BaseViewTest):
    def test_get_all_trip_to_user_auth(self):
        self.login_client("temporary", "temporary")
        response = self.client.get(
            reverse("list-travels")
        )
        expected = Trip.objects.filter(user=self.user_to_filter)
        serialized = TravelSerialization(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_a_trip(self):
        self.login_client("temporary", "temporary")
        response = self.client.get(
            "/api/v1/trip/details/1/",
        )
        expected = Trip.objects.get(pk=1)
        serialized = TravelSerialization(expected)
        self.assertEqual(response.data, serialized.data)


class UpdateTripTest(BaseViewTest):

    def test_update_a_trip_rate(self):
        """
        """
        self.login_client("temporary", "temporary")
        response = self.client.put(
            "/api/v1/trip/details/1/",
            data=json.dumps({
                "rate": 4,
                "classification": 2
            }),
            content_type='application/json'
        )
        self.assertEqual(response.data["rate"], 4)
        self.assertEqual(response.data["classification"], 2)

    def test_update_a_trip_with_invalid_rate(self):
        self.login_client("temporary", "temporary")
        trip = Trip.objects.get(pk=1)
        response = self.client.put(
            "/api/v1/trip/details/1/",
            data=json.dumps({
                "rate": 6,
                "classification": 2
            }),
            content_type='application/json'
        )
        self.assertEqual(
            response.data["message"],
            "Rate is invalid, please use number between 1 and 5"
        )
        self.assertEqual(
            trip.classification,
            '1'
        )

    def test_update_a_invalida_classification(self):
        self.login_client("temporary", "temporary")
        response = self.client.put(
            "/api/v1/trip/details/1/",
            data=json.dumps({
                "classification": 7
            }),
            content_type='application/json'
        )
        self.assertEqual(
            response.data["message"],
            "Classifications invalid"
        )
