from behave import *
from src.BookDatabase import BookDatabase
from unittest.mock import *


@given('book database')
def step_imp(context):
    context.database = Database()


@given('using {function}, result {result}')
def step_imp(context, function, result):
    context.database.function = Mock(getattr(Database, function))
    context.database.function.return_expected_result = str(result)

@when('function {function}')
def step_imp(context, function ):
    context.result = context.database.function()


@then('result {expected_result}')
def step_imp(context, expected_result):
    assert context.result == str(expected_result)