# ProcessChainModel

Definition of the actinia process chain that includes GRASS GIS modules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version string of the process chain | [default to '1']
**list** | [**List[GrassModule]**](GrassModule.md) | A list of process definitions that should be executed in the order provided by the list. | 
**webhooks** | [**Webhooks**](Webhooks.md) |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.process_chain_model import ProcessChainModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessChainModel from a JSON string
process_chain_model_instance = ProcessChainModel.from_json(json)
# print the JSON string representation of the object
print ProcessChainModel.to_json()

# convert the object into a dict
process_chain_model_dict = process_chain_model_instance.to_dict()
# create an instance of ProcessChainModel from a dict
process_chain_model_form_dict = process_chain_model.from_dict(process_chain_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


