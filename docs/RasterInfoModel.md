# RasterInfoModel

Schema that contains raster map layer information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cells** | **str** |  | [optional] 
**cols** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**creator** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**datatype** | **str** |  | [optional] 
**maptype** | **str** |  | [optional] 
**east** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ewres** | **str** |  | [optional] 
**max** | **str** |  | [optional] 
**min** | **str** |  | [optional] 
**ncats** | **str** |  | [optional] 
**nsres** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**map** | **str** |  | [optional] 
**mapset** | **str** |  | [optional] 
**rows** | **str** |  | [optional] 
**source1** | **str** |  | [optional] 
**north** | **str** |  | [optional] 
**source2** | **str** |  | [optional] 
**units** | **str** |  | [optional] 
**vdatum** | **str** |  | [optional] 
**south** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**west** | **str** |  | [optional] 
**semantic_label** | **str** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.raster_info_model import RasterInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of RasterInfoModel from a JSON string
raster_info_model_instance = RasterInfoModel.from_json(json)
# print the JSON string representation of the object
print RasterInfoModel.to_json()

# convert the object into a dict
raster_info_model_dict = raster_info_model_instance.to_dict()
# create an instance of RasterInfoModel from a dict
raster_info_model_form_dict = raster_info_model.from_dict(raster_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


