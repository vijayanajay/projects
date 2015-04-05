from selenium import webdriver
from splinter import Browser
from django.core import management
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'opinionanalysis.settings'


def before_all(context):
    # Check http://www.whoisnicoleharris.com/2015/03/19/bdd-part-two.html
    # for using with PhantomJS
    from django.test import utils

    utils.setup_test_environment()
    ## If you use South for migrations, uncomment this to monkeypatch
    ## syncdb to get migrations to run.
    # from south.management.commands import patch_for_test_db_setup
    # patch_for_test_db_setup()

    ### Set up the WSGI intercept "port".
    host = context.host = 'localhost'
    port = context.port = '17681'
    # NOTE: Nothing is actually listening on this port. wsgi_intercept
    # monkeypatches the networking internals to use a fake socket when
    # connecting to this port.
    context.browser = Browser()

    import urlparse

    def browser_url(url):
        """Create a URL for the virtual WSGI server.

        e.g context.browser_url('/'), context.browser_url(reverse('my_view'))
        """
        return urlparse.urljoin('http://%s:%d/' % (host, port), url)

    context.browser_url = browser_url

    ### BeautifulSoup is handy to have nearby. (Substitute lxml or html5lib as you see fit)
    from BeautifulSoup import BeautifulSoup

    def parse_soup():
        """Use BeautifulSoup to parse the current response and return the DOM tree.
        """
        r = context.browser.response()
        html = r.read()
        r.seek(0)
        return BeautifulSoup(html)

    context.parse_soup = parse_soup


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

def after_scenario(context, scenario):
    # Tear down the scenario test environment.
    from django.db import connection

    #connection.creation.destroy_test_db(settings.DATABASE_NAME, verbosity=True, keepdb=False)

def after_all(context):
    from django.test import utils

    utils.teardown_test_environment()
    context.browser.quit()
    context.browser = None