# A program to Fetch data from server
"""
Created by @Hrishikesh Salunkhe
"""
import urllib.request 
webUrl= urllib.request.urlopen("http://www.google.com")
print("Result code:", webUrl.getcode())