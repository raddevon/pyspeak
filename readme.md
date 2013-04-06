#PySpeak

PySpeak is an interface to the ThingSpeak API. Before using it, change the `API_ADDRESS` to the address of your desired ThingSpeak installation. If you are using ThingSpeak.com, use the default value.

Create a new object with
```python
obj = ThingSpeak([read_key], [write_key])
```

Object methods are provided for reading a channel, reading a field, and updating.

`get_channel(self, channel_id, last_entry=False, fmt='json', opts={})`
* channel_id (int or str) - The id of the channel to be retrieved
* last_entry (bool) - If True, only the most recent value will be returned
* fmt (str) - json, csv, or xml. Returns the data as on object of the given type
* opts (dict) - A dict of optional values to be passed via url params

`get_field(self, channel_id, field_id, last_entry=False, fmt='json', opts={})`
* channel_id (int or str) - The id of the channel to be retrieved
* field_id (int or str) - The id of the field to be retrieved
* last_entry (bool) - If True, only the most recent value will be returned
* fmt (str) - json, csv, or xml. Returns the data as on object of the given type
* opts (dict) - A dict of optional values to be passed via url params

`update_channel(self, opts)`
* opts (dict) - A dict of values to be passed vie url params
