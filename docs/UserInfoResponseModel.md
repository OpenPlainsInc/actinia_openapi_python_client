# UserInfoResponseModel

Response schema that is used to show information about a user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the request | 
**permissions** | [**UserInfoResponseModelPermissions**](UserInfoResponseModelPermissions.md) |  | [optional] 
**user_id** | **str** | The identifier of the user | [optional] 
**user_role** | **str** | The role of the user | [optional] 
**user_group** | **str** | The group of the user | [optional] 

## Example

```python
from actinia_openapi_python_client.models.user_info_response_model import UserInfoResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoResponseModel from a JSON string
user_info_response_model_instance = UserInfoResponseModel.from_json(json)
# print the JSON string representation of the object
print UserInfoResponseModel.to_json()

# convert the object into a dict
user_info_response_model_dict = user_info_response_model_instance.to_dict()
# create an instance of UserInfoResponseModel from a dict
user_info_response_model_form_dict = user_info_response_model.from_dict(user_info_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


