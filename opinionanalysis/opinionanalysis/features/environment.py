from selenium import webdriver
from splinter import Browser
from django.core import management
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'opinionanalysis.settings'
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'http://localhost:8082'

def before_all(context):
    # Check http://www.whoisnicoleharris.com/2015/03/19/bdd-part-two.html
    # for using with PhantomJS
    from django.test import utils
    context.config.setup_logging()

    utils.setup_test_environment()
    context.browser = Browser()
    context.server_url = 'http://localhost:8082/'


def before_scenario(context, scenario):
    # Set up the scenario test environment

    # We must set up and tear down the entire database between
    # scenarios. We can't just use db transactions, as Django's
    # TestClient does, if we're doing full-stack tests with Mechanize,
    # because Django closes the db connection after finishing the HTTP
    # response.
    from django.db import connection

    django.setup()
    connection.creation.create_test_db(verbosity=1, autoclobber=True)

def after_all(context):
    from django.test import utils
    utils.teardown_test_environment()
    context.browser.quit()
    context.browser = None