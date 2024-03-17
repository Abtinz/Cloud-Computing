import requests

'''
    this function will help us to call shezam api for song recognition 
    param -> song_url: this url is our considered song file address in s3 cloud server
'''
def shezam_api(song_url):

    #this url will
    url = "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"