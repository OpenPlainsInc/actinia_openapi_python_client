# SatelliteSceneList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_list** | [**List[SatelliteSceneEntry]**](SatelliteSceneEntry.md) | A list of satellite scenes | 

## Example

```python
from actinia_openapi_python_client.models.satellite_scene_list import SatelliteSceneList

# TODO update the JSON string below
json = "{}"
# create an instance of SatelliteSceneList from a JSON string
satellite_scene_list_instance = SatelliteSceneList.from_json(json)
# print the JSON string representation of the object
print SatelliteSceneList.to_json()

# convert the object into a dict
satellite_scene_list_dict = satellite_scene_list_instance.to_dict()
# create an instance of SatelliteSceneList from a dict
satellite_scene_list_form_dict = satellite_scene_list.from_dict(satellite_scene_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


