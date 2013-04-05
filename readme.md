#PySpeak

PySpeak is an interface to the ThingSpeak API. Before using it, change the `API_ADDRESS` to the address of your desired ThingSpeak installation. If you are using ThingSpeak.com, use the default value.

PySpeak provides two functions:

```python read_channel(channel_id, last_entry=False, **kwargs)```
Parameters:
'channel_id'- the id of a ThingSpeak channel
'last_entry'- Pass True to get only the most recent entry

Returns the JSON response

```python read_channel(channel_id, field_id, last_entry=False, **kwargs)```
Parameters:
'channel_id'- the id of a ThingSpeak channel
'field_id'- the id of a field in the given channel
'last_entry'- pass True to get only the most recent entry

Returns the JSON response