# ProcessChainTemplateTemplate

The full process chain template.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[GrassModule]**](GrassModule.md) | The list of GRASS GIS or actinia modules or executables of which the template consists. | [optional] 

## Example

```python
from actinia_openapi_python_client.models.process_chain_template_template import ProcessChainTemplateTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessChainTemplateTemplate from a JSON string
process_chain_template_template_instance = ProcessChainTemplateTemplate.from_json(json)
# print the JSON string representation of the object
print ProcessChainTemplateTemplate.to_json()

# convert the object into a dict
process_chain_template_template_dict = process_chain_template_template_instance.to_dict()
# create an instance of ProcessChainTemplateTemplate from a dict
process_chain_template_template_form_dict = process_chain_template_template.from_dict(process_chain_template_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


