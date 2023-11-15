# BandInformationEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The suggested file name of this band from the requested satellite scene | 
**map_name** | **str** | The suggested GRASS GIS raster map name of this band from the requested satellite scene | 
**public_url** | **str** | The download URl of the band from requested satellite scene | 

## Example

```python
from actinia_openapi_python_client.models.band_information_entry import BandInformationEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BandInformationEntry from a JSON string
band_information_entry_instance = BandInformationEntry.from_json(json)
# print the JSON string representation of the object
print BandInformationEntry.to_json()

# convert the object into a dict
band_information_entry_dict = band_information_entry_instance.to_dict()
# create an instance of BandInformationEntry from a dict
band_information_entry_form_dict = band_information_entry.from_dict(band_information_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


