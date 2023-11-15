# ModuleParameter

A list of parameters that are applicable for this process.

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
from actinia_openapi_python_client.models.module_parameter import ModuleParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleParameter from a JSON string
module_parameter_instance = ModuleParameter.from_json(json)
# print the JSON string representation of the object
print ModuleParameter.to_json()

# convert the object into a dict
module_parameter_dict = module_parameter_instance.to_dict()
# create an instance of ModuleParameter from a dict
module_parameter_form_dict = module_parameter.from_dict(module_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


