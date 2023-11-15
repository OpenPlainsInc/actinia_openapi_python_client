# Sentinel2ASceneEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The id of the Sentinel2A scene | 
**tiles** | [**List[Sentinel2ATileEntry]**](Sentinel2ATileEntry.md) | A list of sentinel2A scenes | 

## Example

```python
from actinia_openapi_python_client.models.sentinel2_a_scene_entry import Sentinel2ASceneEntry

# TODO update the JSON string below
json = "{}"
# create an instance of Sentinel2ASceneEntry from a JSON string
sentinel2_a_scene_entry_instance = Sentinel2ASceneEntry.from_json(json)
# print the JSON string representation of the object
print Sentinel2ASceneEntry.to_json()

# convert the object into a dict
sentinel2_a_scene_entry_dict = sentinel2_a_scene_entry_instance.to_dict()
# create an instance of Sentinel2ASceneEntry from a dict
sentinel2_a_scene_entry_form_dict = sentinel2_a_scene_entry.from_dict(sentinel2_a_scene_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


