# ModuleReturns

The data that is returned from this process.

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
from actinia_openapi_python_client.models.module_returns import ModuleReturns

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleReturns from a JSON string
module_returns_instance = ModuleReturns.from_json(json)
# print the JSON string representation of the object
print ModuleReturns.to_json()

# convert the object into a dict
module_returns_dict = module_returns_instance.to_dict()
# create an instance of ModuleReturns from a dict
module_returns_form_dict = module_returns.from_dict(module_returns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


