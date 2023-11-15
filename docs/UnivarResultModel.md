# UnivarResultModel

Response schema for the result of univariate computations of raster layers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the raster resource | [optional] 
**cells** | **float** |  | [optional] 
**coeff_var** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**mean** | **float** |  | [optional] 
**mean_of_abs** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**n** | **float** |  | [optional] 
**null_cells** | **float** |  | [optional] 
**range** | **float** |  | [optional] 
**stddev** | **float** |  | [optional] 
**sum** | **float** |  | [optional] 
**variance** | **float** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.univar_result_model import UnivarResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of UnivarResultModel from a JSON string
univar_result_model_instance = UnivarResultModel.from_json(json)
# print the JSON string representation of the object
print UnivarResultModel.to_json()

# convert the object into a dict
univar_result_model_dict = univar_result_model_instance.to_dict()
# create an instance of UnivarResultModel from a dict
univar_result_model_form_dict = univar_result_model.from_dict(univar_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


