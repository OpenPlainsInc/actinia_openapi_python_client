# LocationListResponseModel

Response schema for location lists

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the resource, values: accepted, running, finished, terminated, error | 
**locations** | **List[str]** | The list of locations in the GRASS database | 

## Example

```python
from actinia_openapi_python_client.models.location_list_response_model import LocationListResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of LocationListResponseModel from a JSON string
location_list_response_model_instance = LocationListResponseModel.from_json(json)
# print the JSON string representation of the object
print LocationListResponseModel.to_json()

# convert the object into a dict
location_list_response_model_dict = location_list_response_model_instance.to_dict()
# create an instance of LocationListResponseModel from a dict
location_list_response_model_form_dict = location_list_response_model.from_dict(location_list_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


