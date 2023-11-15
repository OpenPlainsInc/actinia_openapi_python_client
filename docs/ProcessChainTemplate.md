# ProcessChainTemplate

Response schema for module

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the process.  | [optional] 
**description** | **str** | Detailed description to fully explain the entity. | [optional] 
**template** | [**ProcessChainTemplateTemplate**](ProcessChainTemplateTemplate.md) |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.process_chain_template import ProcessChainTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessChainTemplate from a JSON string
process_chain_template_instance = ProcessChainTemplate.from_json(json)
# print the JSON string representation of the object
print ProcessChainTemplate.to_json()

# convert the object into a dict
process_chain_template_dict = process_chain_template_instance.to_dict()
# create an instance of ProcessChainTemplate from a dict
process_chain_template_form_dict = process_chain_template.from_dict(process_chain_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


