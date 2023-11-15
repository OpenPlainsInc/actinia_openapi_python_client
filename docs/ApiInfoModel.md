# ApiInfoModel

Response schema that contains API information of the called endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | The endpoint of the API call | 
**method** | **str** | The HTTP method of the request | 
**path** | **str** | The path of the REST API call | 
**request_url** | **str** | The request URL | 
**post_url** | **str** | The post URL | [optional] 

## Example

```python
from actinia_openapi_python_client.models.api_info_model import ApiInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfoModel from a JSON string
api_info_model_instance = ApiInfoModel.from_json(json)
# print the JSON string representation of the object
print ApiInfoModel.to_json()

# convert the object into a dict
api_info_model_dict = api_info_model_instance.to_dict()
# create an instance of ApiInfoModel from a dict
api_info_model_form_dict = api_info_model.from_dict(api_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


