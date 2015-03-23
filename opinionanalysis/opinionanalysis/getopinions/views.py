from django.shortcuts import render
import getwebsite
import logging
logger = logging.getLogger(__name__)


def index(request):
    url = "http://www.topgear.com/india/our-car-reviews/linea?id=2833"
    rssfeed = "http://www.livemint.com/rss/opinion"

# get feed contents from rssfeed
    feed_content = getwebsite.get_feed(rssfeed)

# post_text = get the results from soup based on the url above
    article = getwebsite.extract(url)

# the return from get_soup is a ResultSet (list).
# That needs to be converted to dictionary to send to the html
    context = {'post_text': feed_content}

#    context = {'post_text': article.cleaned_text}

# return the dictionary to the html
    return render(request, 'getopinions/index.html', context)
