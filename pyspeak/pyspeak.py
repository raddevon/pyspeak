# Gets data from the ThingSpeak API

import requests
import json
from time import sleep


class Channel:
    def __init__(self, channel_id, dest_url=None,
                 url='https://api.thingspeak.com', read_key='', write_key=''):
        self.channel_id = channel_id
        self.url = url.rstrip('/')
        self.read_key = read_key
        self.write_key = write_key
        self.dest_url = dest_url

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
        else:
            return resp.text

    def get_field_feed(self, field_id, last_entry=False, fmt='json', opts={}):
        """
        Parameters:
        field_id (int or string) - The id or name of the field to be retrieved
        last_entry (bool) - If True, only the most recent value will be returned
        fmt (str) - json, csv, or xml. Returns the data as on object of the
            given type
        opts (dict) - A dict of optional values to be passed via url params
        """
        if self.read_key != '':
            opts['key'] = self.read_key

        if isinstance(field_id, str) and field_id[-1].isdigit():
            field_id = field_id[-1]
        elif isinstance(field_id, str):
            raise TypeError('Unable to derive a numerical field ID from the string argument.')

        if last_entry: endpoint = '{}/last.{}'.format(field_id, fmt)
        else: endpoint = '{}.{}'.format(field_id, fmt)

        url = '{}/channels/{}/field/{}'.format(self.url, self.channel_id, endpoint)
        resp = requests.get(url, params=opts)
        if resp.status_code != requests.codes.ok:
            print("ERROR - Response was not ok", resp.status_code)
            exit()

        if fmt == 'json':
            return resp.json()
        else:
            return resp.text

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

    def post_data(self, interval):
        while not sleep(interval):
            channel_data = json.dumps(self.get_channel_feed())
            payload = {'json_data': channel_data}
            r = requests.post(self.dest_url, data=payload)
            print(r.json())
