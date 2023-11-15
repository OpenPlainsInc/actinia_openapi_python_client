# GeodataResponseModel

Model for object for geodata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The Geonetwork uuid. | 
**bbox** | **List[float]** | The bounding box of the result. | 
**crs** | **str** | The coordinate reference system of the result. | [optional] 
**table** | **str** | The db connection string of the result source. | [optional] 

## Example

```python
from actinia_openapi_python_client.models.geodata_response_model import GeodataResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GeodataResponseModel from a JSON string
geodata_response_model_instance = GeodataResponseModel.from_json(json)
# print the JSON string representation of the object
print GeodataResponseModel.to_json()

# convert the object into a dict
geodata_response_model_dict = geodata_response_model_instance.to_dict()
# create an instance of GeodataResponseModel from a dict
geodata_response_model_form_dict = geodata_response_model.from_dict(geodata_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


