import pyspeak

class TestPySpeak:

    def setup(self):
        self.test_channel = pyspeak.Channel(9)

    def test_get_channel_feed_is_dictionary(self):
        test_channel_feed = self.test_channel.get_channel_feed()
        assert ( ( type(test_channel_feed) == dict ) & ( len(test_channel_feed) > 0 ) )

    def test_get_field_feed_is_dictionary(self):
        test_field_feed = self.test_channel.get_field_feed('field2')
        assert ( ( type(test_field_feed) == dict ) & ( len(test_field_feed) > 0 ) )