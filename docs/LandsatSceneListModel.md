# LandsatSceneListModel

This schema defines the JSON input of the Landsat time series creator resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atcor_method** | **str** | The method for atmospheric correction | 
**strds** | **str** | The basename of the new space-time raster datasets (strds). One for each band will be created and the basename will be extended by a band specific suffix. | 
**scene_ids** | **List[str]** | A list of Landsat scene names that should be downloaded and imported. Only scenes from a specific satelleite can be imported and represented as strds. Mixing of different satellites is not permitted. All bands will be imported and atmospherically corrected | 

## Example

```python
from actinia_openapi_python_client.models.landsat_scene_list_model import LandsatSceneListModel

# TODO update the JSON string below
json = "{}"
# create an instance of LandsatSceneListModel from a JSON string
landsat_scene_list_model_instance = LandsatSceneListModel.from_json(json)
# print the JSON string representation of the object
print LandsatSceneListModel.to_json()

# convert the object into a dict
landsat_scene_list_model_dict = landsat_scene_list_model_instance.to_dict()
# create an instance of LandsatSceneListModel from a dict
landsat_scene_list_model_form_dict = landsat_scene_list_model.from_dict(landsat_scene_list_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


