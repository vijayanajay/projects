import logging
import feedparser
import speedparser
from goose import Goose
logger = logging.getLogger(__name__)


def extract(url):
    logger.info("inside extract function")
    goose = Goose()
    article = goose.extract(url=url)
    logger.debug(article.cleaned_text)
    return (article)


def get_feed(feed):
    logger.info("inside get_feed")
    feed_content = feedparser.parse(feed)
    feed_content2 = speedparser.parse(feed)
    logger.debug(feed_content2.keys())
    links_in_feed = feed_content['entries'][1]['links']
    # return links_in_feed[0]['href']
    return feed_content['entries'][1]['links'][0]['href']
