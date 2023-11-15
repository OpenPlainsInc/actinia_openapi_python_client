# SetRegionModel

This schema represents the computational region definition for raster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | Set current region from named region | [optional] 
**raster** | **str** | Raster layer name with mapset to set the region from | [optional] 
**align** | **str** | Raster layer name with mapset to align the region to | [optional] 
**zoom** | **str** | Raster layer name with mapset to zoom the region to | [optional] 
**vector** | **str** | Vector layer name with mapset to set the region from | [optional] 
**n** | **float** | Value for the northern edge | [optional] 
**s** | **float** | Value for the southern edge | [optional] 
**w** | **float** | Value for the western edge | [optional] 
**e** | **float** | Value for the eastern edge | [optional] 
**t** | **float** | Value for the top edge | [optional] 
**b** | **float** | Value for the bottom edge | [optional] 
**nsres** | **float** | North-south 2D grid resolution | [optional] 
**res** | **float** | 2D grid resolution (north-south and east-west) | [optional] 
**ewres** | **float** | East-west 2D grid resolution | [optional] 
**res3** | **float** | 3D grid resolution (north-south, east-west and top-bottom) | [optional] 
**tbres** | **float** | Top-bottom 3D grid resolution | [optional] 

## Example

```python
from actinia_openapi_python_client.models.set_region_model import SetRegionModel

# TODO update the JSON string below
json = "{}"
# create an instance of SetRegionModel from a JSON string
set_region_model_instance = SetRegionModel.from_json(json)
# print the JSON string representation of the object
print SetRegionModel.to_json()

# convert the object into a dict
set_region_model_dict = set_region_model_instance.to_dict()
# create an instance of SetRegionModel from a dict
set_region_model_form_dict = set_region_model.from_dict(set_region_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


