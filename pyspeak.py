# Gets data from the ThingSpeak API

import urllib.request, simplejson as json
from urllib.error import HTTPError

API_ADDRESS = 'http://api.thingspeak.com/' # The URL of your ThingSpeak API.

def read(url, **kwargs):
    '''
    Take a URL and returns a JSON object with the response
    '''
    try:
        response =  urllib.request.urlopen(url, kwargs)
    except ValueError or HTTPError:
        response =  urllib.request.urlopen(url)
    return json.load(response)

def read_channel(channel_id, last_entry=False, **kwargs):
    '''
    Parameters:
    channel_id- the id of a ThingSpeak channel
    last_entry- Pass True to get only the most recent entry

    Returns the JSON response
    '''
    url = '{}channels/{}/feed.json'.format(API_ADDRESS, channel_id) if not last_entry\
            else '{}channels/{}/last.json'.format(API_ADDRESS, channel_id)
    return read(url, **kwargs)

def read_field(channel_id, field_id, last_entry=False, **kwargs):
    '''
    Parameters:
    channel_id- the id of a ThingSpeak channel
    field_id- the id of a field in the given channel
    last_entry- pass True to get only the most recent entry

    Returns the JSON response
    '''
    url = '{}channels/{}/field/{}.json'.format(API_ADDRESS, channel_id, field_id) if not last_entry\
    else '{}channels/{}/field/{}/last.json'.format(API_ADDRESS, channel_id, field_id)
    return read(url, **kwargs)