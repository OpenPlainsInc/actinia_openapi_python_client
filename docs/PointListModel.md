# PointListModel

This schema defines the JSON input of the vector sampling resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **List[List[str]]** | A list of coordinate points with unique ids [(id, x, y), (id, x, y), (id, x, y)] | 

## Example

```python
from actinia_openapi_python_client.models.point_list_model import PointListModel

# TODO update the JSON string below
json = "{}"
# create an instance of PointListModel from a JSON string
point_list_model_instance = PointListModel.from_json(json)
# print the JSON string representation of the object
print PointListModel.to_json()

# convert the object into a dict
point_list_model_dict = point_list_model_instance.to_dict()
# create an instance of PointListModel from a dict
point_list_model_form_dict = point_list_model.from_dict(point_list_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


