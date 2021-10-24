from pytest_bdd import scenario, given,when,then
from apples.apples import AppleCart

@scenario(feature_name='..//features/apples.feature', scenario_name='Add apples to the cart')
def test_add():
    pass

@scenario(feature_name='..//features/apples.feature', scenario_name='Remove apples from the cart')
def test_add2():
    pass

@given("the cart has 0 apples",target_fixture= 'cart')
def cart():
    return AppleCart()

@when("4 apples are added to the cart")
def add_apples(cart):
    cart.add_apples_to_cart(4)

@then("the cart contains 4 apples")
def cart_has_total(cart):
    cart.apple_count == 4

@given("the cart has 8 apples",target_fixture= 'cart')
def cart():
    return AppleCart(8)

@when("4 apples are removed from the cart")
def remove_apples(cart):
    cart.remove_apples_from_cart(4)


