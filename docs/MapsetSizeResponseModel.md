# MapsetSizeResponseModel

Response schema for mapset sizes of a resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the resource, values: success, error | 
**mapset_sizes** | **List[int]** | The list of mapset sizes of a resource in bytes | 

## Example

```python
from actinia_openapi_python_client.models.mapset_size_response_model import MapsetSizeResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of MapsetSizeResponseModel from a JSON string
mapset_size_response_model_instance = MapsetSizeResponseModel.from_json(json)
# print the JSON string representation of the object
print MapsetSizeResponseModel.to_json()

# convert the object into a dict
mapset_size_response_model_dict = mapset_size_response_model_instance.to_dict()
# create an instance of MapsetSizeResponseModel from a dict
mapset_size_response_model_form_dict = mapset_size_response_model.from_dict(mapset_size_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


