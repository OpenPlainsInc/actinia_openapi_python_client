# UserInfoResponseModelPermissions

The names of all users

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_limit** | **str** | The limit of number of raster cells the user is allowed to process | [optional] 
**process_num_limit** | **str** | The limit of number of processes the user is allowed to integrate into one process chain | [optional] 
**process_time_limit** | **str** | The time a process must not exceed | [optional] 
**accessible_datasets** | **object** | The persistent GRASS GIS databases the user is allowed to use. Contains one object for each location name with an array of strings containing all allowed mapset names. See example for more information. | [optional] 
**accessible_modules** | **List[str]** | The GRASS GIS modules the user is allowed to use | [optional] 

## Example

```python
from actinia_openapi_python_client.models.user_info_response_model_permissions import UserInfoResponseModelPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoResponseModelPermissions from a JSON string
user_info_response_model_permissions_instance = UserInfoResponseModelPermissions.from_json(json)
# print the JSON string representation of the object
print UserInfoResponseModelPermissions.to_json()

# convert the object into a dict
user_info_response_model_permissions_dict = user_info_response_model_permissions_instance.to_dict()
# create an instance of UserInfoResponseModelPermissions from a dict
user_info_response_model_permissions_form_dict = user_info_response_model_permissions.from_dict(user_info_response_model_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


