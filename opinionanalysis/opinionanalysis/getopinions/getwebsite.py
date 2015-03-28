import logging
import feedparser
from goose import Goose
from models import *
from django.db import transaction
logger = logging.getLogger(__name__)

#this is required to do single insert query rather than multiple
@transaction.commit_manually

def extract(url):
    logger.info("inside extract function")
    goose = Goose()
    article = goose.extract(url=url)
    #logger.debug(article.cleaned_text)
    return (article)


def get_feed(feed):
    logger.info("inside get_feed")

    # first get from speedparser
    feed_content = feedparser.parse(feed)
    logger.debug(feed_content.entries)
    links_in_feed = feed_content['entries'][1]['links']

    #add into the Articles tables
    for entry in feed_content['entries']:
    	article = Article()
    	article.title = entry['title']
    	article.content = entry ['summary']
    	article.link = entry['links'][0]['href']
    	article.save()
    transaction.commit()
    # return links_in_feed[0]['href']
    return feed_content['entries'][1]['links'][0]['href']
