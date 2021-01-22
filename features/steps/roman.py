from behave import *
from src.sample.roman_class import *
from assertpy import assert_that

use_step_matcher("re")


@given("a decimal number equal to (?P<arabic>.+)")
def step_impl(context, arabic):
    context.arabic = int(arabic)


@when("a roman number equal to (?P<roman>.+)")
def step_impl(context, roman):
    context.roman = roman


@then("arabic number should be equal to roman")
def step_impl(context):
    context.result = roman(context.arabic)
    assert_that(context.result).is_equal_to(context.roman)

