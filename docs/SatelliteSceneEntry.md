# SatelliteSceneEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scene_id** | **str** | The id of the satellite scene | 
**sensing_time** | **str** | The sensing time of the scene | 
**cloud_cover** | **float** | Cloud cover of the scene 0-100 | [optional] 
**east_lon** | **float** | Eastern border of the scene | [optional] 
**west_lon** | **float** | Western border of the scene | [optional] 
**north_lat** | **float** | Northern border of the scene | [optional] 
**south_lat** | **float** | Southern border of the scene | [optional] 
**total_size** | **float** | Total size of the scene | [optional] 

## Example

```python
from actinia_openapi_python_client.models.satellite_scene_entry import SatelliteSceneEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SatelliteSceneEntry from a JSON string
satellite_scene_entry_instance = SatelliteSceneEntry.from_json(json)
# print the JSON string representation of the object
print SatelliteSceneEntry.to_json()

# convert the object into a dict
satellite_scene_entry_dict = satellite_scene_entry_instance.to_dict()
# create an instance of SatelliteSceneEntry from a dict
satellite_scene_entry_form_dict = satellite_scene_entry.from_dict(satellite_scene_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


