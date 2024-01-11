import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from apps.product.models import Product
from apps.user.models import BuyerProfile


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


# class TestUserEndpoints:
#     endpoint = "/user/signup/buyer/"

#     def test_create(self, api_client):
#         buyer = baker.prepare(BuyerProfile)
#         expected_json = {
#             "user": {
#                 "username": buyer.user.username,
#                 "password": buyer.user.password,
#                 "email": buyer.user.email,
#                 "address": buyer.user.address,
#             },
#             "name": buyer.name,
#             "phone": buyer.phone,
#         }
#         response = api_client.post(self.endpoint, data=expected_json, format="json")
#         assert response.status_code == 201
#         assert json.loads(response.content) == expected_json
