import json   #used to load a dictionary
import codecs #used to load the data file with the proper encoding
import string #used to remove punctuation
import requests
import zillow
import locale
from bs4 import BeautifulSoup
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults






address = "1600 Pennsylvania Ave NW, Washington, DC"
zipcode = 20006

key = "X1-ZWz1hui29fa3uz_3l8b3"
api = zillow.ValuationApi()
zillow_data = api.GetSearchResults(key,address,zipcode)
deep_search_response = api.GetDeepSearchResults(key,address,zipcode)
result = deep_search_response.get_dict()
print(result.zillow_id + "\n")
print("Initia test completed\n")
#soup = BeautifulSoup(page.content,'html.parser')

