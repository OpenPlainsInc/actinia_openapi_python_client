# TokenResponseModel

Response schema that is used for authentication token generation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the resource, values: success, error | 
**token** | **str** | The generated token for authentication | 
**message** | **str** | The message of the token generation | [optional] 

## Example

```python
from actinia_openapi_python_client.models.token_response_model import TokenResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponseModel from a JSON string
token_response_model_instance = TokenResponseModel.from_json(json)
# print the JSON string representation of the object
print TokenResponseModel.to_json()

# convert the object into a dict
token_response_model_dict = token_response_model_instance.to_dict()
# create an instance of TokenResponseModel from a dict
token_response_model_form_dict = token_response_model.from_dict(token_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


