# LockedMapsetListResponseModel

Response schema that is used to list all locked mapsets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the request | 
**locked_mapsets_list** | **List[str]** | The names of all locked mapsets | 
**message** | **str** | A simple message to describes the status of the resource | 

## Example

```python
from actinia_openapi_python_client.models.locked_mapset_list_response_model import LockedMapsetListResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of LockedMapsetListResponseModel from a JSON string
locked_mapset_list_response_model_instance = LockedMapsetListResponseModel.from_json(json)
# print the JSON string representation of the object
print LockedMapsetListResponseModel.to_json()

# convert the object into a dict
locked_mapset_list_response_model_dict = locked_mapset_list_response_model_instance.to_dict()
# create an instance of LockedMapsetListResponseModel from a dict
locked_mapset_list_response_model_form_dict = locked_mapset_list_response_model.from_dict(locked_mapset_list_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


