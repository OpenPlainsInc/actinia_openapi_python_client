# StdoutParser

Use this parameter to automatically parse the output of GRASS GIS modules and convert the output into tables, lists or key/value pairs in the result section of the response.If the property type is set to *table*, *list* or *kv* then the stdout of the current command will be parsed and the result of the parse operation will be added to the result dictionary using the provided id as key. GRASS GIS modules produce regular output. Many modules have the flag *-g* to create key value pairs as stdout output. Other create a list of values or a table with/without header.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id that is used to identify the parsed output in the result dictionary. | 
**format** | **str** | The stdout format to be parsed. | 
**delimiter** | **str** | The delimiter that should be used to parse table, list and key/value module output. Many GRASS GIS  modules use by default \&quot;|\&quot; in tables and \&quot;&#x3D;\&quot; in key/value pairs. A new line \&quot;\\n\&quot; is always the delimiter between rows in the output. | 

## Example

```python
from actinia_openapi_python_client.models.stdout_parser import StdoutParser

# TODO update the JSON string below
json = "{}"
# create an instance of StdoutParser from a JSON string
stdout_parser_instance = StdoutParser.from_json(json)
# print the JSON string representation of the object
print StdoutParser.to_json()

# convert the object into a dict
stdout_parser_dict = stdout_parser_instance.to_dict()
# create an instance of StdoutParser from a dict
stdout_parser_form_dict = stdout_parser.from_dict(stdout_parser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


