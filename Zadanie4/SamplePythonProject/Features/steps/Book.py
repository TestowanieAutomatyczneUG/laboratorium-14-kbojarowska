from behave import *
from src.Book import Book
from src.Author import Author

@given('book title {title}')
def step_impl(context, title):
    context.title = title


@given('book author {firstname}, {lastname}, {email}')
def step_impl(context, firstname, lastname, email):
    context.author = Author(firstname, lastname, email)


@given('book isbn {isbn}')
def step_impl(context, isbn):
    context.isbn = isbn

@when('creating book')
def step_imp(context):
    try:
        context.book = Book(context.title, context.author, context.isbn)
    except Exception as e:
        context.e = True

@then('book is {created}')
def step_imp(context,created):
	if created == 'created':
		assert context.book
	else:
		assert context.e