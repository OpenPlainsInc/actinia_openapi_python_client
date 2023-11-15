# RegionModel

Output of GRASS GIS module g.region -gu3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projection** | **float** |  | [optional] 
**zone** | **float** |  | [optional] 
**n** | **float** |  | [optional] 
**s** | **float** |  | [optional] 
**w** | **float** |  | [optional] 
**e** | **float** |  | [optional] 
**t** | **float** |  | [optional] 
**b** | **float** |  | [optional] 
**nsres** | **float** |  | [optional] 
**nsres3** | **float** |  | [optional] 
**ewres** | **float** |  | [optional] 
**ewres3** | **float** |  | [optional] 
**tbres** | **float** |  | [optional] 
**rows** | **float** |  | [optional] 
**rows3** | **float** |  | [optional] 
**cols** | **float** |  | [optional] 
**cols3** | **float** |  | [optional] 
**depths** | **float** |  | [optional] 
**cells** | **float** |  | [optional] 
**cells3** | **float** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.region_model import RegionModel

# TODO update the JSON string below
json = "{}"
# create an instance of RegionModel from a JSON string
region_model_instance = RegionModel.from_json(json)
# print the JSON string representation of the object
print RegionModel.to_json()

# convert the object into a dict
region_model_dict = region_model_instance.to_dict()
# create an instance of RegionModel from a dict
region_model_form_dict = region_model.from_dict(region_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


