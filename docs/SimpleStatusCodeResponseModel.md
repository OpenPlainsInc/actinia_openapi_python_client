# SimpleStatusCodeResponseModel

Simple response schema to inform about status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **float** | The status code of the request. | 
**message** | **str** | A short message to describes the status | 

## Example

```python
from actinia_openapi_python_client.models.simple_status_code_response_model import SimpleStatusCodeResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleStatusCodeResponseModel from a JSON string
simple_status_code_response_model_instance = SimpleStatusCodeResponseModel.from_json(json)
# print the JSON string representation of the object
print SimpleStatusCodeResponseModel.to_json()

# convert the object into a dict
simple_status_code_response_model_dict = simple_status_code_response_model_instance.to_dict()
# create an instance of SimpleStatusCodeResponseModel from a dict
simple_status_code_response_model_form_dict = simple_status_code_response_model.from_dict(simple_status_code_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


