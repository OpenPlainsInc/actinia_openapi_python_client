# ProjectionInfoModel

Schema to define projection information as JSON input in POST requests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epsg** | **str** | The EPSG code of the projection that should be used to create a location | 

## Example

```python
from actinia_openapi_python_client.models.projection_info_model import ProjectionInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectionInfoModel from a JSON string
projection_info_model_instance = ProjectionInfoModel.from_json(json)
# print the JSON string representation of the object
print ProjectionInfoModel.to_json()

# convert the object into a dict
projection_info_model_dict = projection_info_model_instance.to_dict()
# create an instance of ProjectionInfoModel from a dict
projection_info_model_form_dict = projection_info_model.from_dict(projection_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


