from .. import Channel
from .config import API, CHANNEL, READ_KEY, WRITE_KEY, FIELDS, DEST_URL
import simplejson as json
import random


class TestPySpeak:

    def setup(self):
        self.test_channel = Channel(
            CHANNEL, DEST_URL, API, READ_KEY, WRITE_KEY)
        self.updates = dict()

    def generate_random_update_values(self):
        for field in FIELDS:
            self.updates[field] = random.randint(1, 100)

    def test_get_channel_feed_is_dictionary(self):
        test_channel_feed = self.test_channel.get_channel_feed()
        assert ((type(test_channel_feed) == dict)
                & (len(test_channel_feed) > 0))

    def test_get_field_feed_is_dictionary(self):
        test_field_feed = self.test_channel.get_field_feed('field2')
        assert ((type(test_field_feed) == dict)
                & (len(test_field_feed) > 0))

    def test_update_and_read_channel(self):
        self.generate_random_update_values()
        self.test_channel.update_channel(self.updates)
        test_json = self.test_channel.get_channel_feed(last_entry=True)

        for field in FIELDS:
            assert(int(test_json[field]) == self.updates[field])

    def test_update_and_read_field(self):
        self.generate_random_update_values()
        self.test_channel.update_channel(self.updates)
        for field in FIELDS:
            test_json = self.test_channel.get_field_feed(
                field, last_entry=True)
            assert(int(test_json[field]) == self.updates[field])

    def test_post_pyspeak_data(self):
        self.generate_random_update_values()
        self.test_channel.update_channel(self.updates)
        source_response = json.dumps(self.test_channel.get_channel_feed())
        dest_response = self.test_channel.post_data()
        assert(dest_response.json()['form']['json_data'] == source_response)
