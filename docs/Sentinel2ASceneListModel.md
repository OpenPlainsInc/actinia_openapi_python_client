# Sentinel2ASceneListModel

This schema defines the JSON input of the sentinel time series creator resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bands** | **List[str]** | A list of band names that should be downloaded and imported for each Sentinel-2 scene.Available are the following band names: \&quot;B01\&quot;, \&quot;B02\&quot;, \&quot;B03\&quot;, \&quot;B04\&quot;, \&quot;B05\&quot;, \&quot;B06\&quot;, \&quot;B07\&quot;,\&quot;B08\&quot;, \&quot;B8A\&quot;, \&quot;B09\&quot; \&quot;B10\&quot;, \&quot;B11\&quot;, \&quot;B12\&quot; | 
**product_ids** | **List[str]** | A list of Sentinel-2 scene names of which the tile download urls and metadata infor urls should be provided. | 

## Example

```python
from actinia_openapi_python_client.models.sentinel2_a_scene_list_model import Sentinel2ASceneListModel

# TODO update the JSON string below
json = "{}"
# create an instance of Sentinel2ASceneListModel from a JSON string
sentinel2_a_scene_list_model_instance = Sentinel2ASceneListModel.from_json(json)
# print the JSON string representation of the object
print Sentinel2ASceneListModel.to_json()

# convert the object into a dict
sentinel2_a_scene_list_model_dict = sentinel2_a_scene_list_model_instance.to_dict()
# create an instance of Sentinel2ASceneListModel from a dict
sentinel2_a_scene_list_model_form_dict = sentinel2_a_scene_list_model.from_dict(sentinel2_a_scene_list_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


