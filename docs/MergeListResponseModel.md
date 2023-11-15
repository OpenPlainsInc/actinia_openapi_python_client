# MergeListResponseModel

Merge process list reponse schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_processes** | [**List[MergeShortDescResponseModel]**](MergeShortDescResponseModel.md) | The list of all available merge processes. | 

## Example

```python
from actinia_openapi_python_client.models.merge_list_response_model import MergeListResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of MergeListResponseModel from a JSON string
merge_list_response_model_instance = MergeListResponseModel.from_json(json)
# print the JSON string representation of the object
print MergeListResponseModel.to_json()

# convert the object into a dict
merge_list_response_model_dict = merge_list_response_model_instance.to_dict()
# create an instance of MergeListResponseModel from a dict
merge_list_response_model_form_dict = merge_list_response_model.from_dict(merge_list_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


