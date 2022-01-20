from behave import *
from src.FizzBuzz import FizzBuzz

use_step_matcher("parse")


@given('there is FizzBuzz game')
def step_impl(context):
    context.FizzBuzz = FizzBuzz()


@when(u'I get the number {number:d}')
def step_impl(context, number):
    context.result = context.FizzBuzz.game(number)

@then('Its Fizz')
def step_impl(context):
    assert context.result == "Fizz"


@then('Its FizzBuzz')
def step_impl(context):
    assert context.result == "FizzBuzz"


@then('Its Buzz')
def step_impl(context):
    assert context.result == "Buzz"

@then('Its {result:d}')
def step_impl(context, result):
    assert context.result == int(result)
