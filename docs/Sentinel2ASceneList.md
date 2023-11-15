# Sentinel2ASceneList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiles** | [**List[Sentinel2ASceneEntry]**](Sentinel2ASceneEntry.md) | A list of sentinel2A scenes | [optional] 

## Example

```python
from actinia_openapi_python_client.models.sentinel2_a_scene_list import Sentinel2ASceneList

# TODO update the JSON string below
json = "{}"
# create an instance of Sentinel2ASceneList from a JSON string
sentinel2_a_scene_list_instance = Sentinel2ASceneList.from_json(json)
# print the JSON string representation of the object
print Sentinel2ASceneList.to_json()

# convert the object into a dict
sentinel2_a_scene_list_dict = sentinel2_a_scene_list_instance.to_dict()
# create an instance of Sentinel2ASceneList from a dict
sentinel2_a_scene_list_form_dict = sentinel2_a_scene_list.from_dict(sentinel2_a_scene_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


