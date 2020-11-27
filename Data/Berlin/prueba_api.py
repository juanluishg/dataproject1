# This is how you can use your own personal access token using requests_oauthlib library to access data from the protected resource  
from requests_oauthlib import OAuth1Session
immoscout_api = OAuth1Session('client_key',
                            client_secret='2eSzSYHrKp1z08e7',
                            resource_owner_key='DataProject 1Key',
                            resource_owner_secret='62ja8yqMaMEmZMBP')  
url = 'https://rest.sandbox-immobilienscout24.de/restapi/api/offer/v1.0/user/me/realestate/'  
r = immoscout_api.get(url)
print(r)