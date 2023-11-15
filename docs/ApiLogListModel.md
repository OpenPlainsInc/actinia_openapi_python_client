# ApiLogListModel

Response schema that represents a list of API log entries.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_log_list** | [**List[ApiLogEntryModel]**](ApiLogEntryModel.md) | A list of ApiLogEntryModel objects | 

## Example

```python
from actinia_openapi_python_client.models.api_log_list_model import ApiLogListModel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLogListModel from a JSON string
api_log_list_model_instance = ApiLogListModel.from_json(json)
# print the JSON string representation of the object
print ApiLogListModel.to_json()

# convert the object into a dict
api_log_list_model_dict = api_log_list_model_instance.to_dict()
# create an instance of ApiLogListModel from a dict
api_log_list_model_form_dict = api_log_list_model.from_dict(api_log_list_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


