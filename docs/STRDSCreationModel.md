# STRDSCreationModel

Information required to create a new STRDS

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the STRDS | 
**description** | **str** | The description of the STRDS | 
**temporaltype** | **str** | The temporal type of the STRDS, which can be absolute and relative | [optional] [default to 'absolute']

## Example

```python
from actinia_openapi_python_client.models.strds_creation_model import STRDSCreationModel

# TODO update the JSON string below
json = "{}"
# create an instance of STRDSCreationModel from a JSON string
strds_creation_model_instance = STRDSCreationModel.from_json(json)
# print the JSON string representation of the object
print STRDSCreationModel.to_json()

# convert the object into a dict
strds_creation_model_dict = strds_creation_model_instance.to_dict()
# create an instance of STRDSCreationModel from a dict
strds_creation_model_form_dict = strds_creation_model.from_dict(strds_creation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


