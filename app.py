#import urllib 
#use urllib.request to get the data from the url
# write a function that takes the url and returns a response

import urllib.request as urllib


def main(url):
    print('Checking connectivity...')

    response = urllib.urlopen(url)
    print('Connected to', url, 'succesfully')
    print('The response code was:', response.getcode())


print('This a site connectivity cheker program')
input_url = input('Input the url of the site: ')

main(input_url)