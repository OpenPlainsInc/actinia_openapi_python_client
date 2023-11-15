# OutputParameterMetadata

The STAC file export parameter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Format of the metadata file. Only STAC is supported. The STAC item builder works just on raster export file.These files are accessible through a STAC Catalogand each export is stored as STAC Item | 

## Example

```python
from actinia_openapi_python_client.models.output_parameter_metadata import OutputParameterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OutputParameterMetadata from a JSON string
output_parameter_metadata_instance = OutputParameterMetadata.from_json(json)
# print the JSON string representation of the object
print OutputParameterMetadata.to_json()

# convert the object into a dict
output_parameter_metadata_dict = output_parameter_metadata_instance.to_dict()
# create an instance of OutputParameterMetadata from a dict
output_parameter_metadata_form_dict = output_parameter_metadata.from_dict(output_parameter_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


