# STRDSRasterListEntryModel

A single raster map layer information entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**min** | **str** |  | [optional] 
**max** | **str** |  | [optional] 
**north** | **str** |  | [optional] 
**south** | **str** |  | [optional] 
**east** | **str** |  | [optional] 
**west** | **str** |  | [optional] 
**rows** | **str** |  | [optional] 
**cols** | **str** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.strds_raster_list_entry_model import STRDSRasterListEntryModel

# TODO update the JSON string below
json = "{}"
# create an instance of STRDSRasterListEntryModel from a JSON string
strds_raster_list_entry_model_instance = STRDSRasterListEntryModel.from_json(json)
# print the JSON string representation of the object
print STRDSRasterListEntryModel.to_json()

# convert the object into a dict
strds_raster_list_entry_model_dict = strds_raster_list_entry_model_instance.to_dict()
# create an instance of STRDSRasterListEntryModel from a dict
strds_raster_list_entry_model_form_dict = strds_raster_list_entry_model.from_dict(strds_raster_list_entry_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


