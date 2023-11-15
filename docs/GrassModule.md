# GrassModule

The definition of a single GRASS GIS module and its inputs, outputs and flags. This module will be run in a location/mapset environment and is part of a process chain. The stdout and stderr output of modules that were run before this module in the process chain can be used as stdin for this module. The stdout of a module can be automatically transformed in list, table or key/value JSON representations in the HTTP response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique id to identify the module call in the process chain to reference its stdout and stderr output as stdin in other modules. | 
**module** | **str** | The name of the GRASS GIS module (r.univar, r.slope.aspect, v.select, ...) that should be executed. Use as module names \&quot;importer\&quot; or \&quot;exporter\&quot; to import or export raster layer, vector layer or other file based data without calling a GRASS GIS module. | 
**inputs** | [**List[InputParameter]**](InputParameter.md) | A list of input parameters of a GRASS GIS module. | [optional] 
**outputs** | [**List[OutputParameter]**](OutputParameter.md) | A list of output parameters of a GRASS GIS module. | [optional] 
**flags** | **str** | The flags that should be set for the GRASS GIS module. | [optional] 
**stdin** | **str** | Use the stdout output of a GRASS GIS module or executable of the process chain as input for this module. Refer to the module/executable output as *id::stderr* or *id::stdout*, the \&quot;id\&quot; is the unique identifier of a GRASS GIS module definition. | [optional] 
**stdout** | [**StdoutParser**](StdoutParser.md) |  | [optional] 
**overwrite** | **bool** | Set True to overwrite existing data. | [optional] 
**verbose** | **bool** | Set True to activate verbosity output of the module. | [optional] 
**superquiet** | **bool** | Set True to silence the output of the module. | [optional] 
**interface_description** | **bool** | Set True to print interface description and exit. | [optional] 

## Example

```python
from actinia_openapi_python_client.models.grass_module import GrassModule

# TODO update the JSON string below
json = "{}"
# create an instance of GrassModule from a JSON string
grass_module_instance = GrassModule.from_json(json)
# print the JSON string representation of the object
print GrassModule.to_json()

# convert the object into a dict
grass_module_dict = grass_module_instance.to_dict()
# create an instance of GrassModule from a dict
grass_module_form_dict = grass_module.from_dict(grass_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


