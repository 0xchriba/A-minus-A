from amazon.api import AmazonAPI
from datetime import datetime
import re
import requests
"""1. Find a way to create a function that given a keyword returns the respective ItemId
   2. Build out the Alibaba API side
   3. Create a function that finds the price differential between the two
   4. Build out the front-end"""

url = 'https://www.amazon.com/s?keyword=macbook'
htmltext = requests.get(url).content
pattern = re.compile(r"https://www.amazon.com/.*/dp(.*?)\"")
# final = re.findall(htmltext,pattern)


# from amazonproduct import API
access_key = 'AKIAJ5KTDL536GDNI57Q'
secret_key = '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'
assoc_tag = 'ibafeva-20'
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
