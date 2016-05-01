from behave import *
from selenium import webdriver
from wsgiref import simple_server
from django.core import management
from opinionanalysis import model
from opinionanalysis import web_app


def before_all(context):
    # Check http://www.whoisnicoleharris.com/2015/03/19/bdd-part-two.html
    # for using with PhantomJS

    context.server = simple_server.WSGIServer(('', 6081))
    context.server.set_app(web_app.main(environment='test'))
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()
    context.browser = webdriver.Chrome()


def before_scenario(context, scenario):
    # Reset the database before each scenario
    # This means we can create, delete and edit objects within an
    # individual scenerio without these changes affecting our
    # other scenarios
    management.call_command('flush', verbosity=0, interactive=False)

    # At this stage we can (optionally) mock additional data to
    # setup in the database. For example, if we know that all
    # of our tests require a 'SiteConfig' object,
    # we could create it here.


def after_all(context):
    # Quit our browser once we're done!
    context.browser.quit()
    context.browser = None
