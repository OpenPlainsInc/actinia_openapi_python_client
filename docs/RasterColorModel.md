# RasterColorModel

Set the color table for an existing raster map layer with a set of rules, a specific color or an other raster map layer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | **List[str]** | A list of rules to set the color table of a raster map layer | [optional] 
**color** | **str** | The name of a color to be set for a raster map layer | [optional] 
**raster** | **str** | The name of an existing raster map layer to copy the color table from | [optional] 

## Example

```python
from actinia_openapi_python_client.models.raster_color_model import RasterColorModel

# TODO update the JSON string below
json = "{}"
# create an instance of RasterColorModel from a JSON string
raster_color_model_instance = RasterColorModel.from_json(json)
# print the JSON string representation of the object
print RasterColorModel.to_json()

# convert the object into a dict
raster_color_model_dict = raster_color_model_instance.to_dict()
# create an instance of RasterColorModel from a dict
raster_color_model_form_dict = raster_color_model.from_dict(raster_color_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


