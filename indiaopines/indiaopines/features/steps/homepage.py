__author__ = 'Ajay'

@given(u'I am a guest user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am a guest user')

@when(u'I navigate to the homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I navigate to the homepage')

@then(u'I will see a atleast 10 articles')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will see a atleast 10 articles')

@then(u'I will be able to read the first article')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will be able to read the first article')

@then(u'the article has more than 300 words')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the article has more than 300 words')