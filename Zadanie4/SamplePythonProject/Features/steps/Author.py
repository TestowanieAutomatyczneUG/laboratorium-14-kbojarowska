from behave import *
from src.Author import Author


@given("firstname {firstname}")
def step_impl(context, firstname):
    context.firstname = firstname

@given("lastname {lastname}")
def step_impl(context, lastname):
    context.lastname = lastname

@given("email {email}")
def step_impl(context, email):
    context.email = email

@when("creating author")
def step_impl(context):
    try:
        context.author = Author(context.firstname, context.lastname, context.email)
    except:
        context.error = True

@then("author created")
def step_impl(context):
    assert context.author

@then("failure")
def step_impl(context):
    assert context.failure