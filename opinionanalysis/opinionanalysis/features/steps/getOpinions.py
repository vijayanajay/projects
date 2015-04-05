from behave import *

use_step_matcher("re")

@given("a feed")
def step_impl(context):
    context.feed = "http://www.livemint.com/rss/opinion"
    context.browser.visit(url='http://localhost:8082/getopinions/')


@when("all the articles are extracted")
def step_impl(context):
    pass

@then(u'I see (?P<number>.*) feeds in the Article table')
def step_impl(context, number):
    """
    :type context behave.runner.Context
    """

    pass


@step("all the fields are filled in")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass