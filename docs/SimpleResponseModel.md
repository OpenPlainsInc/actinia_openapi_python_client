# SimpleResponseModel

Response schema that is used in cases that no asynchronous run was

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the resource, values: accepted, running, finished, terminated, error | 
**message** | **str** | A simple message to describes the status of the resource | 

## Example

```python
from actinia_openapi_python_client.models.simple_response_model import SimpleResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleResponseModel from a JSON string
simple_response_model_instance = SimpleResponseModel.from_json(json)
# print the JSON string representation of the object
print SimpleResponseModel.to_json()

# convert the object into a dict
simple_response_model_dict = simple_response_model_instance.to_dict()
# create an instance of SimpleResponseModel from a dict
simple_response_model_form_dict = simple_response_model.from_dict(simple_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


