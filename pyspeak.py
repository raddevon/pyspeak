# Gets data from the ThingSpeak API

import requests

try:
    import json
except:
    import simplejson as json


class Channel:
    def __init__(self, channel_id, url='https://api.thingspeak.com', read_key='', write_key=''):
        self.channel_id = channel_id
        self.url = url
        self.read_key = read_key
        self.write_key = write_key

    def get_channel_feed(self, last_entry=False, fmt='json', opts={}):
        # example: http://api.thingspeak.com/channels/9/feed.json
        """
        Parameters:
        last_entry (bool) - If True, only the most recent value will be returned
        fmt (str) - json, csv, or xml. Returns the data as on object of the
            given type
        opts (dict) - A dict of optional values to be passed via url params
        """
        if self.read_key != '':
            opts['key'] = self.read_key

        if last_entry: endpoint = 'feed/last.{}'.format(fmt)
        else: endpoint = 'feed.{}'.format(fmt)

        url = '{}/channels/{}/{}'.format(self.url, self.channel_id, endpoint)
        print(url)
        resp = requests.get(url, params=opts)
        if resp.status_code != requests.codes.ok:
            print("ERROR - Response was not ok", resp.status_code)
            exit()

        if fmt == 'json':
            return resp.json()

    def get_field_feed(self, field_id, last_entry=False, fmt='json', opts={}):
        """
        Parameters:
        field_id (int) - The id of the field to be retrieved
        last_entry (bool) - If True, only the most recent value will be returned
        fmt (str) - json, csv, or xml. Returns the data as on object of the
            given type
        opts (dict) - A dict of optional values to be passed via url params
        """
        if self.read_key != '':
            opts['key'] = self.read_key

        if last_entry: endpoint = '{}/last.{}'.format(field_id, fmt)
        else: endpoint = '{}.{}'.format(field_id, fmt)

        url = '{}/channels/{}/field/{}'.format(self.url, self.channel_id, endpoint)
        resp = requests.get(url, params=opts)
        if resp.status_code != requests.codes.ok:
            print("ERROR - Response was not ok", resp.status_code)
            exit()

        if fmt == 'json':
            return resp.json()

    def update_channel(self, opts):
        """
        Parameters:
        opts (dict) - A dict of values to be passed vie url params
        """
        if self.write_key != '':
            opts['key'] = self.write_key
        else:
            print("No Write Key available for channel")
            return False


        url = '{}/update'.format(self.url)
        resp = requests.post(url, data=opts)

        if resp.status_code != requests.codes.ok:
            print("ERROR - Response was not ok", resp.status_code)
            exit()

        return resp