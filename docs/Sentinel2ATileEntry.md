# Sentinel2ATileEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b01** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b02** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b03** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b04** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b05** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b06** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b07** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b08** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b09** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b10** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b11** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**b12** | [**BandInformationEntry**](BandInformationEntry.md) |  | [optional] 
**info** | **str** | The url to Sentinel2A scene information | 
**metadata** | **str** | The url to Sentinel2A scene XML metadata | 
**preview** | **str** | The url to Sentinel2A scene preview image | 
**url** | **str** | The url to Sentinel2A scene root directory that contains all informations about the scene | 
**timestamp** | **str** | The sensing time of the scene | 

## Example

```python
from actinia_openapi_python_client.models.sentinel2_a_tile_entry import Sentinel2ATileEntry

# TODO update the JSON string below
json = "{}"
# create an instance of Sentinel2ATileEntry from a JSON string
sentinel2_a_tile_entry_instance = Sentinel2ATileEntry.from_json(json)
# print the JSON string representation of the object
print Sentinel2ATileEntry.to_json()

# convert the object into a dict
sentinel2_a_tile_entry_dict = sentinel2_a_tile_entry_instance.to_dict()
# create an instance of Sentinel2ATileEntry from a dict
sentinel2_a_tile_entry_form_dict = sentinel2_a_tile_entry.from_dict(sentinel2_a_tile_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


