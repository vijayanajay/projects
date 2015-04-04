from behave import *

use_step_matcher("re")

@given("a user")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@when("I log in")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("I see my account summary")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@step("I see a warm and welcoming message")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@step("I log out")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("I see a cold and heartless message")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass