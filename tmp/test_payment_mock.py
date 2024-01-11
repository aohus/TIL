import pytest
from apps.payment.services import check_product_stock
from apps.payment.services import update_wallet_transaction
from rest_framework.exceptions import ValidationError


@pytest.mark.parametrize(
    "quantity, should_raise",
    [
        (4, False),  # Sufficient stock, should not raise ValidationError
        (6, True),  # Insufficient stock, should raise ValidationError
    ],
)
def test_check_stock(mocker, quantity, should_raise):
    mocker.patch(
        "apps.payment.models.order.OrderDetail.objects.filter",
        return_value=mocker.Mock(aggregate=lambda **kwargs: {"stock": 5}),
    )

    product_mock = mocker.Mock(stock=10, deleted_at=None)
    order_detail_data = [{"product": product_mock, "quantity": quantity}]

    if should_raise:
        with pytest.raises(ValidationError):
            check_product_stock(order_detail_data)
    else:
        try:
            check_product_stock(order_detail_data)
        except ValidationError:
            pytest.fail("Unexpected ValidationError raised")


# def test_update_wallet_transaction(mocker):
#     mocker.patch(
#         "apps.payment.services.Wallet.get_balance",
#         return_value=20000,
#     )
#     order = {"total_price": 2000, "user": "user"}
#     result = update_wallet_transaction(order)

#     assert result.amount == 2000
#     assert result.mileage == 2000 * 0.03
