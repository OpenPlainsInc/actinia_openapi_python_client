# AreaUnivarResultModel

Response schema for the result of univariate computations of raster layers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fid** | **str** | Field id from the polygon of the vector map layer used for area stats computation | [optional] 
**cat** | **str** | The category id from the polygon of the vector map layer used for area stats computation | [optional] 
**raster_number** | **float** |  | [optional] 
**raster_minimum** | **float** |  | [optional] 
**raster_maximum** | **float** |  | [optional] 
**raster_range** | **float** |  | [optional] 
**raster_average** | **float** |  | [optional] 
**raster_median** | **float** |  | [optional] 
**raster_stddev** | **float** |  | [optional] 
**raster_sum** | **float** |  | [optional] 
**raster_variance** | **float** |  | [optional] 
**raster_coeff_var** | **float** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.area_univar_result_model import AreaUnivarResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of AreaUnivarResultModel from a JSON string
area_univar_result_model_instance = AreaUnivarResultModel.from_json(json)
# print the JSON string representation of the object
print AreaUnivarResultModel.to_json()

# convert the object into a dict
area_univar_result_model_dict = area_univar_result_model_instance.to_dict()
# create an instance of AreaUnivarResultModel from a dict
area_univar_result_model_form_dict = area_univar_result_model.from_dict(area_univar_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


