# STRDSInfoModel

Information about a specific space-time raster dataset (STRDS)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_type** | **str** |  | [optional] 
**bottom** | **str** |  | [optional] 
**creation_time** | **str** |  | [optional] 
**creator** | **str** |  | [optional] 
**east** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**ewres_max** | **str** |  | [optional] 
**ewres_min** | **str** |  | [optional] 
**granularity** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**map_time** | **str** |  | [optional] 
**mapset** | **str** |  | [optional] 
**max_max** | **str** |  | [optional] 
**max_min** | **str** |  | [optional] 
**min_max** | **str** |  | [optional] 
**min_min** | **str** |  | [optional] 
**modification_time** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**north** | **str** |  | [optional] 
**number_of_semantic_labels** | **str** |  | [optional] 
**nsres_max** | **str** |  | [optional] 
**nsres_min** | **str** |  | [optional] 
**number_of_maps** | **str** |  | [optional] 
**raster_register** | **str** |  | [optional] 
**semantic_labels** | **str** |  | [optional] 
**semantic_type** | **str** |  | [optional] 
**south** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**temporal_type** | **str** |  | [optional] 
**top** | **str** |  | [optional] 
**west** | **str** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.strds_info_model import STRDSInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of STRDSInfoModel from a JSON string
strds_info_model_instance = STRDSInfoModel.from_json(json)
# print the JSON string representation of the object
print STRDSInfoModel.to_json()

# convert the object into a dict
strds_info_model_dict = strds_info_model_instance.to_dict()
# create an instance of STRDSInfoModel from a dict
strds_info_model_form_dict = strds_info_model.from_dict(strds_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


