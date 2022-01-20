from behave import *
from src.validateISBNNumber import validateISBNNumber


@given('ISBN Number validation')
def step_impl(context):
    context.validateISBNNumber = validateISBNNumber


@when('the number is {number}')
def step_impl(context, number):
    context.result = context.validateISBNNumber.validate(number)


@then('Its {result}')
def step_impl(context, result):
    assert str(context.result) == result