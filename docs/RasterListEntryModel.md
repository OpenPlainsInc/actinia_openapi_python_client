# RasterListEntryModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.raster_list_entry_model import RasterListEntryModel

# TODO update the JSON string below
json = "{}"
# create an instance of RasterListEntryModel from a JSON string
raster_list_entry_model_instance = RasterListEntryModel.from_json(json)
# print the JSON string representation of the object
print RasterListEntryModel.to_json()

# convert the object into a dict
raster_list_entry_model_dict = raster_list_entry_model_instance.to_dict()
# create an instance of RasterListEntryModel from a dict
raster_list_entry_model_form_dict = raster_list_entry_model.from_dict(raster_list_entry_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


