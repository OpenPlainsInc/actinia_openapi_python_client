# ModuleList

Response schema for module lists

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the resource, values: accepted, running, finished, terminated, error | 
**processes** | [**List[Module]**](Module.md) | The list of modules in GRASS GIS | 

## Example

```python
from actinia_openapi_python_client.models.module_list import ModuleList

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleList from a JSON string
module_list_instance = ModuleList.from_json(json)
# print the JSON string representation of the object
print ModuleList.to_json()

# convert the object into a dict
module_list_dict = module_list_instance.to_dict()
# create an instance of ModuleList from a dict
module_list_form_dict = module_list.from_dict(module_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


