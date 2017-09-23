from amazon.api import AmazonAPI
from datetime import datetime
import re
import requests
"""1. Find a way to get url of first search result
   2. Build out the Alibaba API side
   3. Create a function that finds the price differential between the two
   4. Build out the front-end"""
url = "https://www.amazon.com/Amazon-Echo-Dot-Portable-Bluetooth-Speaker-with-Alexa-Black/dp/B01DFKC2SO/ref=sr_1_1?ie=UTF8&qid=1506151336&sr=8-1&keywords=echo"
def get_asin(url):
    asin_scraper = r'/([A-Z0-9]{10})'
    result = re.search(asin_scraper,url).group(1)
    return result


# from amazonproduct import API

amazon = AmazonAPI(access_key,secret_key, assoc_tag)
def find_price():
    product = amazon.lookup(ItemId='B01G1XH46M')
    title = product.title
    price = product.price_and_currency
    if price[1] == 'USD':
        print(title)
        # return price[0]
# find_price()
# time = datetime.now()
# print(time)

# 'http://webservices.amazon.com/onca/xml?%20Service=AWSECommerceService%20&Operation=ItemSearch%20&ResponseGroup=Small%20&SearchIndex=All%20&Keywords=' + keyword + '&AWSAccessKeyId=AKIAJ5KTDL536GDNI57Q&AssociateTag=ibafeva-20&Timestamp=' + '2017-09-23T00:57:26-05:00' + '&Signature=AKIAJ5KTDL536GDNI57Q+U4kMqptyqXQ2bFvPfqr8LRymwIletYCQk5f7lbY'
