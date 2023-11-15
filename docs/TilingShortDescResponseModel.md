# TilingShortDescResponseModel

Response schema for short description of tiling processes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Categories of the process. | 
**description** | **str** | Description of the process. | 
**id** | **str** | ID of the process. | 

## Example

```python
from actinia_openapi_python_client.models.tiling_short_desc_response_model import TilingShortDescResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TilingShortDescResponseModel from a JSON string
tiling_short_desc_response_model_instance = TilingShortDescResponseModel.from_json(json)
# print the JSON string representation of the object
print TilingShortDescResponseModel.to_json()

# convert the object into a dict
tiling_short_desc_response_model_dict = tiling_short_desc_response_model_instance.to_dict()
# create an instance of TilingShortDescResponseModel from a dict
tiling_short_desc_response_model_form_dict = tiling_short_desc_response_model.from_dict(tiling_short_desc_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


