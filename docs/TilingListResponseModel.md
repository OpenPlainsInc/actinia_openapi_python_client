# TilingListResponseModel

Tiling process list reponse schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiling_processes** | [**List[TilingShortDescResponseModel]**](TilingShortDescResponseModel.md) | The list of all available tiling processes. | 

## Example

```python
from actinia_openapi_python_client.models.tiling_list_response_model import TilingListResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TilingListResponseModel from a JSON string
tiling_list_response_model_instance = TilingListResponseModel.from_json(json)
# print the JSON string representation of the object
print TilingListResponseModel.to_json()

# convert the object into a dict
tiling_list_response_model_dict = tiling_list_response_model_instance.to_dict()
# create an instance of TilingListResponseModel from a dict
tiling_list_response_model_form_dict = tiling_list_response_model.from_dict(tiling_list_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


