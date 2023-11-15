# VectorCreationModel

Schema for input parameters to generate a random point vector map layer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**npoints** | **float** | Number of points to be created | [optional] 
**seed** | **float** | The seed to initialize the random generator. If not set the process ID is used | [optional] 
**zmin** | **float** | Minimum z height | [optional] [default to 0.0]
**zmax** | **float** | Maximum z height | [optional] [default to 100.0]

## Example

```python
from actinia_openapi_python_client.models.vector_creation_model import VectorCreationModel

# TODO update the JSON string below
json = "{}"
# create an instance of VectorCreationModel from a JSON string
vector_creation_model_instance = VectorCreationModel.from_json(json)
# print the JSON string representation of the object
print VectorCreationModel.to_json()

# convert the object into a dict
vector_creation_model_dict = vector_creation_model_instance.to_dict()
# create an instance of VectorCreationModel from a dict
vector_creation_model_form_dict = vector_creation_model.from_dict(vector_creation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


