# MapsetInfoModel

Schema for projection and region information from a specific mapset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projection** | **str** | The location projection WKT string | 
**region** | [**RegionModel**](RegionModel.md) |  | 

## Example

```python
from actinia_openapi_python_client.models.mapset_info_model import MapsetInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of MapsetInfoModel from a JSON string
mapset_info_model_instance = MapsetInfoModel.from_json(json)
# print the JSON string representation of the object
print MapsetInfoModel.to_json()

# convert the object into a dict
mapset_info_model_dict = mapset_info_model_instance.to_dict()
# create an instance of MapsetInfoModel from a dict
mapset_info_model_form_dict = mapset_info_model.from_dict(mapset_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


