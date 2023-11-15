# IOParameterBase

Parameter definition of a GRASS GIS module that should be executed in the actinia environment. Parameters can be of type input or output. A GRASS GIS module will be usually called like: <p>g.region raster=elevation30m@PERMANENT</p> The GRASS GIS module *g.region* parameter *raster* has the value *elevation30m@PERMANENT*. This is reflected by the *param* and *value* properties that can specify input and output parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**param** | **str** | The name of a GRASS GIS module parameter like *map* or *elevation*.  | 
**value** | **str** | The value of the GRASS GIS module parameter. Raster, vector and STDS inputs must contain the mapset name in their id: *slope@PERMANENT*, if they are not located in the working mapset. Do not contain the mapset name in map names that are processed, since the mapsets are generated on demand using random names. Outputs are not allowed to contain mapset names.Files that are created in the process chain to exchange data can be specified using the *$file::unique_id* identifier. The **unique_id** will be replaced with a temporary file name, that is available in the whole process chain at runtime. The **unique_id**  is the identifier that can be used by different modules in a process chain to access the same temporary file or to prepare it for export. | 

## Example

```python
from actinia_openapi_python_client.models.io_parameter_base import IOParameterBase

# TODO update the JSON string below
json = "{}"
# create an instance of IOParameterBase from a JSON string
io_parameter_base_instance = IOParameterBase.from_json(json)
# print the JSON string representation of the object
print IOParameterBase.to_json()

# convert the object into a dict
io_parameter_base_dict = io_parameter_base_instance.to_dict()
# create an instance of IOParameterBase from a dict
io_parameter_base_form_dict = io_parameter_base.from_dict(io_parameter_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


