import pytest
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient

from apps.payment.models.order import Order
from apps.payment.models.order import OrderDetail
from apps.payment.models.wallet import Wallet
from apps.payment.services import check_product_stock
from apps.payment.services import pay
from apps.payment.services import rollback_pay
from apps.payment.services import update_wallet_transaction
from apps.product.models import Category
from apps.product.models import Product
from apps.user.models import BuyerProfile
from apps.user.models import StoreProfile
from apps.user.models import User


@pytest.fixture
def create_login_buyer(db):
    user = User.objects.create_user(
        username="buyer", password="testpass", is_buyer=True
    )
    BuyerProfile.objects.create(user=user, name="Buyer1", phone="01012345678")
    client = APIClient()
    client.login(username=user.username, password="testpass")
    return user, client


@pytest.fixture
def create_login_store(db):
    user = User.objects.create_user(
        username="store", password="testpass", is_store=True
    )
    StoreProfile.objects.create(
        user=user, name="Store1", phone="01076504321", business_number="1234567"
    )
    client = APIClient()
    client.login(username=user.username, password="testpass")
    return user, client


@pytest.fixture
def create_products(db, create_login_store):
    store, _ = create_login_store
    category = Category.objects.create(name="TestCategory")
    product = Product.objects.create(
        name="Product",
        price=1000,
        stock=10,
        user=store.user,
        category=category,
        description="Description for Product",
    )
    return product


# views.py : Wallet Create
@pytest.mark.django_db
def test_post_wallet(create_login_buyer):
    user, client = create_login_buyer
    transaction = {"user": user.id, "transaction_type": 1, "amount": 10000}
    response = client.post(f"/payment/wallet/", data=transaction, format="json")
    assert response.status_code == 201


# service.py functions
@pytest.mark.django_db
def test_update_wallet_transaction_insufficient_balance(create_login_buyer):
    user, client = create_login_buyer
    Wallet.objects.create(user=user, transaction_type=0, amount=1000)
    order = {"total_price": 2000, "user": user}
    with pytest.raises(ValidationError):
        update_wallet_transaction(order)


@pytest.mark.django_db
def test_update_wallet_transaction_sufficient_balance(create_login_buyer):
    user, client = create_login_buyer
    Wallet.objects.create(user=user, transaction_type=0, amount=2000)
    order = {"total_price": 2000, "user": user}
    result = update_wallet_transaction(order)
    assert result.amount == 2000
    assert result.mileage == 2000 * 0.03


@pytest.mark.django_db
def test_update_product_stock_insufficient_stock(create_login_store):
    user, _ = create_login_store
    category = Category.objects.create(name="test")
    product = Product.objects.create(
        user=user, name="Test Product", price=1000, category=category, stock=10
    )
    order_detail_data = {"product": product, "quantity": 11}
    with pytest.raises(ValidationError):
        check_product_stock([order_detail_data])


@pytest.mark.django_db
def test_pay_success(create_login_buyer):
    user, _ = create_login_buyer
    Wallet.objects.create(user=user, transaction_type=0, amount=2000)
    order = {"total_price": 2000, "user": user}
    category = Category.objects.create(name="test")
    product = Product.objects.create(
        user=user, name="Test Product", price=1000, category=category, stock=10
    )
    order_detail_data = {"product": product, "quantity": 2}
    result = pay(order, [order_detail_data])
    assert result.mileage == 2000 * 0.03
    assert Wallet.get_balance(user=result.user) == 0
