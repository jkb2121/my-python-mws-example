# my-python-mws-example
My example of using python-amazon-mws to hit the MWS API

Look at the image called mws-credentials.png.  That's where all of the MWS Credentials inputs come from.  Use your SellerCentral "Owner" account and check it out.
![Credentials](https://github.com/jkb2121/my-python-mws-example/blob/master/mws-credentials.png "Example Credentials")

Enter that information in the appropriate field in the example.yaml file.
```
# Example File - All the codes (except Amazon Marketplace ID's)
# are made up to match the screenshot, you'll need to generate your own
mws_account_info:
    # Seller Account:
    account_id: 'A9CBH13C138MXJ'

    # Developer Account Specific:
    auth_token: '1234-4567-8901'
    access_key: 'ALKKJSDLFJKLKLJSLKJL'
    secret_key: 'GFOofwqvFLKJEOomosfoeOJSDFKJkjFKJOSjkb'

    # Amazon Marketplace ID
    marketplace_id: 'ATVPDKIKX0DER'  # Amazon.com
    # marketplace_id: A2EUQ1WTGCTBG2 # (Amazon.ca)
    # marketplace_id: A1AM78C64UM0Y8 # (Amazon.com.mx)
```

Run the mwsexample.py program, passing in the .yaml file.
```
$ python mwsexample.py example.yaml
```
Then, the program will do a service status check, an ASIN lookup, and then a pricing lookup.
