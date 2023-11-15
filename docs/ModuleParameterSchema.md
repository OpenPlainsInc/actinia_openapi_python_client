# ModuleParameterSchema

A schema object according to the specification of JSON 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**enum** | **List[str]** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.module_parameter_schema import ModuleParameterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleParameterSchema from a JSON string
module_parameter_schema_instance = ModuleParameterSchema.from_json(json)
# print the JSON string representation of the object
print ModuleParameterSchema.to_json()

# convert the object into a dict
module_parameter_schema_dict = module_parameter_schema_instance.to_dict()
# create an instance of ModuleParameterSchema from a dict
module_parameter_schema_form_dict = module_parameter_schema.from_dict(module_parameter_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


