# InputParameterImportDescr

Definition of sources to be imported as raster or vector map layer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the input that should be downloaded and imported. In case of raster or vector types a download URL must be provided as source using http, https or ftp protocols. In case of sentinel2  scenes the scene name and the band must be provided. The Landsat approach is different. &lt;br&gt;&lt;br&gt;In case a Landsat scene is requested, all bands will be download, in the target location imported and an atmospheric correction is applied. The atmospheric correction must be specified. The resulting raster map layers have a specific name scheme, that is independent from the provided map name in the process description. The name scheme is always: &lt;p&gt;\\&lt;landsat scene id\\&gt;_\\&lt;atcor\\&gt;.\\&lt;band\\&gt;&lt;/p&gt;For example, if the scene &lt;p&gt;LT52170762005240COA00&lt;/p&gt; was requested, the resulting name for the DOS1 atmospheric corrected band 1 would be: &lt;p&gt;LT52170762005240COA00_dos1.1&lt;/p&gt;.For the DOS1 atmospheric corrected band 2 it would be: &lt;p&gt;LT52170762005240COA00_dos1.2&lt;/p&gt; and so on. All other process steps must use these raster map layer names to refer to the imported Landsat bands. Use the file option to download any kind of files that should be processed by a grass gis module.  | [optional] 
**sentinel_band** | **str** | The band of the sentinel2 scene that should be imported | [optional] 
**landsat_atcor** | **str** | The atmospheric correction that should be applied to the landsat scene | [optional] 
**vector_layer** | **str** | The name of the layer that should be imported from the vector file or postGIS database | [optional] 
**source** | **str** | The input source that may be a landsat scene name, a sentinel2 scene name, a postGIS database string,a stac collection ID or an URL that points to an accessible raster or vector file. A HTTP, HTTPS or FTP connection must be specified in case of raster or vector types. In this case the source string must contain the protocol that will used for connection: http:// or https:// or ftp://. PostGIS vector layer can be imported by defining a database string as source and a layer name. | [optional] 
**semantic_label** | **str** | Refers to the common names used tocall the bands of an image,for example: red, blue, nir, swirHowever, this property also accepts the band namesuch as B1, B8 etc. The semantic labeling should matchthe labels register in the stac collection. | [optional] 
**extent** | **str** | Spatio-temporal constraint defined by the userthroughout bbox and interval concept. | [optional] 
**filter** | **str** | Constrain in any other propertyor metadata. | [optional] 
**resample** | **str** | Resampling method to use for reprojection of raster map (default: nearest). | [optional] 
**resolution** | **str** | Resolution of output raster map. Estimated, user-specified or current region resolution (default: estimated). | [optional] 
**resolution_value** | **str** | Resolution of output raster map (use with option \&quot;resolution\&quot;: \&quot;value\&quot;) in units of the target coordinate reference system, not in map units. Must be convertible to float. | [optional] 
**basic_auth** | **str** | User name and password for basic HTTP, HTTPS and FTP authentication of the source connection. The user name and password must be separated by a colon: username:password | [optional] 

## Example

```python
from actinia_openapi_python_client.models.input_parameter_import_descr import InputParameterImportDescr

# TODO update the JSON string below
json = "{}"
# create an instance of InputParameterImportDescr from a JSON string
input_parameter_import_descr_instance = InputParameterImportDescr.from_json(json)
# print the JSON string representation of the object
print InputParameterImportDescr.to_json()

# convert the object into a dict
input_parameter_import_descr_dict = input_parameter_import_descr_instance.to_dict()
# create an instance of InputParameterImportDescr from a dict
input_parameter_import_descr_form_dict = input_parameter_import_descr.from_dict(input_parameter_import_descr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


