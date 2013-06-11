#PySpeak

PySpeak is an interface to the ThingSpeak API.

Create a new object with
```python
obj = pyspeak.Channel(id, [dest_url], [url], [read_key], [write_key])
```
* `dest_url` is the URL for posting. If you don't want to post, just don't set it when you instantiate your variable.
* The default url for a new channel is api.thingspeak.com

Object methods are provided for reading a channel, reading a field, updating, and submitting the retrieved JSON data via HTTP POST.

`get_channel_feed(self, last_entry=False, fmt='json', opts={})`
Fetches the feed for the entire channel.
* last_entry (bool) - If True, only the most recent value will be returned
* fmt (str) - json, csv, or xml. Returns the data as on object of the given type
* opts (dict) - A dict of optional values to be passed via url params

`get_field_feed(self, field_id, last_entry=False, fmt='json', opts={})`
Fetches the field specified in field_id.
* field_id (int or str) - The id of the field to be retrieved
* last_entry (bool) - If True, only the most recent value will be returned
* fmt (str) - json, csv, or xml. Returns the data as on object of the given type
* opts (dict) - A dict of optional values to be passed via url params

`update_channel(self, opts)`
Submits an update to the channel.
* opts (dict) - A dict of values to be passed via url params
 
`post_data(self)`
Submits the data retrieved using `get_channel_feed` via HTTP POST to the URL specified as the `dest_url` parameter to the Channel constructor.

##Testing
If you want to run the test for PySpeak, be sure to run `pip install -r requirements.txt` to download the requirements first. You'll also need to take a look at the config.sample.py file, fill it with your channel info, and rename it to `config.py`. Make sure you create a channel __for testing only__ or else these tests will store trash data in your channel.
