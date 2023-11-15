# Module

Response schema for module

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the process.  | 
**summary** | **str** | A short summary of what the process does. | [optional] 
**description** | **str** | Detailed description to fully explain the entity. | 
**categories** | **List[str]** | A list of categories. GRASS GIS addons have the category \&quot;grass-module\&quot; and the actinia core modules are identified with \&quot;actinia-module\&quot; | [optional] 
**parameters** | [**ModuleParameter**](ModuleParameter.md) |  | [optional] 
**returns** | [**ModuleReturns**](ModuleReturns.md) |  | [optional] 
**import_descr** | [**ModuleImportDescription**](ModuleImportDescription.md) |  | [optional] 
**export** | [**ModuleExportDescription**](ModuleExportDescription.md) |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.module import Module

# TODO update the JSON string below
json = "{}"
# create an instance of Module from a JSON string
module_instance = Module.from_json(json)
# print the JSON string representation of the object
print Module.to_json()

# convert the object into a dict
module_dict = module_instance.to_dict()
# create an instance of Module from a dict
module_form_dict = module.from_dict(module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


