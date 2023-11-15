# ApiLogEntryModel

Response schema for a single API log entry that is used to track all API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_stamp** | **str** | The time stamp of the API call | 
**node** | **str** | The node that executed the API call | 
**endpoint** | **str** | The endpoint of the API call | 
**method** | **str** | The HTTP method of the request | 
**path** | **str** | The path of the REST API call | 
**url** | **str** | The request URL | 
**request_str** | **str** | The request string | 

## Example

```python
from actinia_openapi_python_client.models.api_log_entry_model import ApiLogEntryModel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLogEntryModel from a JSON string
api_log_entry_model_instance = ApiLogEntryModel.from_json(json)
# print the JSON string representation of the object
print ApiLogEntryModel.to_json()

# convert the object into a dict
api_log_entry_model_dict = api_log_entry_model_instance.to_dict()
# create an instance of ApiLogEntryModel from a dict
api_log_entry_model_form_dict = api_log_entry_model.from_dict(api_log_entry_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


