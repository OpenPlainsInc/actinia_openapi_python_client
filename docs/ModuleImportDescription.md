# ModuleImportDescription

Import parameters to import data for this process.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for the parameter.  | 
**description** | **str** | Detailed description to fully explain the entity. | 
**optional** | **bool** | Determines whether this parameter is mandatory.  Default: true | [optional] 
**default** | **str** | The default value for this parameter. | [optional] 
**var_schema** | [**ModuleParameterSchema**](ModuleParameterSchema.md) |  | 

## Example

```python
from actinia_openapi_python_client.models.module_import_description import ModuleImportDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleImportDescription from a JSON string
module_import_description_instance = ModuleImportDescription.from_json(json)
# print the JSON string representation of the object
print ModuleImportDescription.to_json()

# convert the object into a dict
module_import_description_dict = module_import_description_instance.to_dict()
# create an instance of ModuleImportDescription from a dict
module_import_description_form_dict = module_import_description.from_dict(module_import_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


