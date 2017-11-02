#!/usr/bin/python

#
# This program uses the python-amazon-mws python library to hit the
# MWS APIs and do some lookups of ASIN and Price
#

# https://github.com/czpython/python-amazon-mws
# pip install python-amazon-mws
from mws import mws
import pprint
import sys
import yaml

#
# Pulled all of my configuration info from a YAML file.
#

if len(sys.argv) != 2:
    print "Usage:  mwsexample.py <config>.yaml"
    exit(1)

try:
    print("Using Configuration File: " + sys.argv[1])
    with open(sys.argv[1], 'r') as f:
        yml = yaml.load(f)
        account_id = yml['mws_account_info']['account_id']
        auth_token = yml['mws_account_info']['auth_token']
        access_key = yml['mws_account_info']['access_key']
        secret_key = yml['mws_account_info']['secret_key']
        marketplace_id = yml['mws_account_info']['marketplace_id']

except IOError:
    print "Error Opening Config File: " + sys.argv[1] 
    exit(1)

pp = pprint.PrettyPrinter(indent=4)

#
# Set up my MWS object.
# The auth_token was a hack I needed to do to the python-amazon-mws library
# because pip didn't install the latest version and MWS seemed to need it
# so I just jammed it in.  YMMV
#
mws = mws.Products(access_key=access_key, secret_key=secret_key, account_id=account_id, 
                   region='US', domain='', uri='', version='', auth_token=auth_token)


#
# Easy example:  See if the service is up and running or not.
#
result = mws.get_service_status()
print("Result: {}".format(result.parsed))

#
# Next example:  Do a lookup of products matching this UPC and pull out the ASIN:
#
result = mws.list_matching_products(marketplace_id, "879020007142")

pp.pprint(result.parsed)
asin = result.parsed.Products.Product.Identifiers.MarketplaceASIN.ASIN
asins = { asin }
print("ASIN: {}".format(result.parsed.Products.Product.Identifiers.MarketplaceASIN.ASIN))

#
# Last example:  Lookup competitive pricing for the ASIN and return the list price
#
r = mws.get_competitive_pricing_for_asin(marketplace_id, asins)

pp.pprint(r.parsed)

listing_price = r.parsed.Product.CompetitivePricing.CompetitivePrices.CompetitivePrice.Price.ListingPrice.Amount

print("Listing Price: {}".format(listing_price))


