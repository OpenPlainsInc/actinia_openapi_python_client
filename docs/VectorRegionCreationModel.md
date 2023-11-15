# VectorRegionCreationModel

Schema for random vector generation in a specific region

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | [**SetRegionModel**](SetRegionModel.md) |  | [optional] 
**parameter** | [**VectorCreationModel**](VectorCreationModel.md) |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.vector_region_creation_model import VectorRegionCreationModel

# TODO update the JSON string below
json = "{}"
# create an instance of VectorRegionCreationModel from a JSON string
vector_region_creation_model_instance = VectorRegionCreationModel.from_json(json)
# print the JSON string representation of the object
print VectorRegionCreationModel.to_json()

# convert the object into a dict
vector_region_creation_model_dict = vector_region_creation_model_instance.to_dict()
# create an instance of VectorRegionCreationModel from a dict
vector_region_creation_model_form_dict = vector_region_creation_model.from_dict(vector_region_creation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


