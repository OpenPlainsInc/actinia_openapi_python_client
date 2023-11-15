# MaxMapsetSizeResponseModel

Response schema for maximum mapset size of a resoucre

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the resource, values: success, error | 
**max_mapset_size** | **int** | The maximum mapset size of a resource in bytes | 

## Example

```python
from actinia_openapi_python_client.models.max_mapset_size_response_model import MaxMapsetSizeResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of MaxMapsetSizeResponseModel from a JSON string
max_mapset_size_response_model_instance = MaxMapsetSizeResponseModel.from_json(json)
# print the JSON string representation of the object
print MaxMapsetSizeResponseModel.to_json()

# convert the object into a dict
max_mapset_size_response_model_dict = max_mapset_size_response_model_instance.to_dict()
# create an instance of MaxMapsetSizeResponseModel from a dict
max_mapset_size_response_model_form_dict = max_mapset_size_response_model.from_dict(max_mapset_size_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


