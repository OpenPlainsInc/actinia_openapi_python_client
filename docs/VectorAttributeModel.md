# VectorAttributeModel

Description of a vector map layer attribute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.vector_attribute_model import VectorAttributeModel

# TODO update the JSON string below
json = "{}"
# create an instance of VectorAttributeModel from a JSON string
vector_attribute_model_instance = VectorAttributeModel.from_json(json)
# print the JSON string representation of the object
print VectorAttributeModel.to_json()

# convert the object into a dict
vector_attribute_model_dict = vector_attribute_model_instance.to_dict()
# create an instance of VectorAttributeModel from a dict
vector_attribute_model_form_dict = vector_attribute_model.from_dict(vector_attribute_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


