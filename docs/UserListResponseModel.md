# UserListResponseModel

Response schema that is used to list all users.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the request | 
**user_list** | **List[str]** | The names of all users | 

## Example

```python
from actinia_openapi_python_client.models.user_list_response_model import UserListResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserListResponseModel from a JSON string
user_list_response_model_instance = UserListResponseModel.from_json(json)
# print the JSON string representation of the object
print UserListResponseModel.to_json()

# convert the object into a dict
user_list_response_model_dict = user_list_response_model_instance.to_dict()
# create an instance of UserListResponseModel from a dict
user_list_response_model_form_dict = user_list_response_model.from_dict(user_list_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


