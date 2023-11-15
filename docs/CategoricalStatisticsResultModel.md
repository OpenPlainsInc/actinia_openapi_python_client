# CategoricalStatisticsResultModel

Response schema for the result of r.stats computations of raster layers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat** | **str** | The raster category | 
**name** | **str** | The name of raster category | 
**area** | **float** | The size of the area in square meters | 
**cell_count** | **float** | The number of cells that have the raster category | 
**percent** | **float** | The percentage of the area | 

## Example

```python
from actinia_openapi_python_client.models.categorical_statistics_result_model import CategoricalStatisticsResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of CategoricalStatisticsResultModel from a JSON string
categorical_statistics_result_model_instance = CategoricalStatisticsResultModel.from_json(json)
# print the JSON string representation of the object
print CategoricalStatisticsResultModel.to_json()

# convert the object into a dict
categorical_statistics_result_model_dict = categorical_statistics_result_model_instance.to_dict()
# create an instance of CategoricalStatisticsResultModel from a dict
categorical_statistics_result_model_form_dict = categorical_statistics_result_model.from_dict(categorical_statistics_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


