from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import logging
from goose import Goose
logger = logging.getLogger(__name__)

def extract(url):
	logger.info ("inside extract function")
	goose = Goose()
	article = goose.extract(url=url)
	logger.debug (article.cleaned_text)
	return (article)

def clean_post(post):
	return ("nothing")

if __name__ == '__main__':
	url = "http://www.team-bhp.com/forum/test-drives-initial-ownership-reports/148583-2014-fiat-linea-facelift-test-drive-review.html"

	soup = make_soup(url)
	f = open('workfile.tmp', 'a')

 	post = get_soup(url)
