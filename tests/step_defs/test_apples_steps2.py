from pytest_bdd import scenario, given,when,then,scenarios,parsers
from apples.apples import AppleCart

#@scenario(feature_name='..//features/apples.feature', scenario_name='Add apples to the cart')
#def test_add():
#    pass

#@scenario(feature_name='..//features/apples.feature', scenario_name='Remove apples from the cart')
#def test_add2():
#    pass



scenarios('..//features/apples.feature')


EXTRA_TYPES = {
    'Number': int,
}

# @given("the cart has 0 apples",target_fixture= 'cart')
@given(parsers.cfparse('the cart has "{initial:Number}" apples',extra_types = EXTRA_TYPES),target_fixture='cart')
def cart(initial):
    return AppleCart(start_apples=initial)

#@when("4 apples are added to the cart")
@when(parsers.cfparse('"{adder:Number}" apples are added to the cart',extra_types = EXTRA_TYPES))
def add_apples(cart,adder):
    print('cart before add', cart.apple_count)
    cart.add_apples_to_cart(adder)
    print('cart after add',cart.apple_count)

#@then("the cart contains 4 apples")
@then(parsers.cfparse('the cart contains "{counter:Number}" apples',extra_types = EXTRA_TYPES))
def cart_has_total(cart,counter):
    print('counter',counter)
    print('cart.apple_count for then',cart.apple_count)
    assert cart.apple_count == counter

#@given("the cart has 8 apples",target_fixture= 'cart')
#def cart():
#    return AppleCart(8)

#@when("4 apples are removed from the cart")
@when(parsers.cfparse('"{remover:Number}" apples are removed from the cart',extra_types=EXTRA_TYPES))
def remove_apples(cart,remover):
    cart.remove_apples_from_cart(remover)
