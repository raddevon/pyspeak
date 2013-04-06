# Gets data from the ThingSpeak API

import urllib
import urllib2
try:
    import json
except:
    import simplejson as json


class ThingSpeak(self):
    def __init__(self, read_key='', write_key=''):
        self.API = 'http://api.thingspeak.com/'
        self.ready_key = read_key
        seld.write_key = write_key
    
    def get_channel(self, channel_id, last_entry=False, fmt='json', opts={}):
        '''
        Parameters:
        channel_id (int or str) - The id of the channel to be retrieved
        last_entry (bool) - If True, only the most recent value will be returned
        fmt (str) - json, csv, or xml. Returns the data as on object of the
            given type
        opts (dict) - A dict of optional values to be passed via url params
        '''
        if last entry: endpoint = 'last.{}'.format(fmt)
        else: endpoint = 'feed.{}'.format(fmt)
        
        url = '{}channels/{}/{}'.format(self.API, channel_id, endpoint)
        if opts:
            queries = urllib.urlencode(opts)
            url = '{}?{}'.format(url, queries)
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        result = response.read()
        
        if fmt == 'json':
            result = json.loads(result)
        
        return result
    
    def get_field(self, channel_id, field_id, last_entry=False, fmt='json', opts={}):
        '''
        Parameters:
        channel_id (int or str) - The id of the channel to be retrieved
        field_id (int or str) - The id of the field to be retrieved
        last_entry (bool) - If True, only the most recent value will be returned
        fmt (str) - json, csv, or xml. Returns the data as on object of the
            given type
        opts (dict) - A dict of optional values to be passed via url params
        '''
        if last entry: endpoint = '{}/last.{}'.format(field_id, fmt)
        else: endpoint = '{}.{}'.format(field_id, fmt)
        
        url = '{}channels/{}/field/{}'.format(self.API, channel_id, endpoint)
        if opts:
            queries = urllib.urlencode(opts)
            url = '{}?{}'.format(url, queries)
        
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        result = response.read()
        
        if fmt == 'json':
            result = json.loads(result)
        
        return result

    def update_channel(self, opts):
        '''
        Parameters:
        opts (dict) - A dict of values to be passed vie url params
        '''
        if not 'key' in opts:
            if not self.write_key:
                raise ValueError('A write key is required to update a channel')
            else: opts['key'] = self.write_key

        opts = urllib.encode(ops)        
        url = '{}/update?{}'.format(self.API, opts)
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        result = response.read()

        return result