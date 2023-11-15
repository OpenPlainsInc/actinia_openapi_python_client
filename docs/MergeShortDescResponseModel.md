# MergeShortDescResponseModel

Response schema for short description of merge processes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Categories of the process. | 
**description** | **str** | Description of the process. | 
**id** | **str** | ID of the process. | 

## Example

```python
from actinia_openapi_python_client.models.merge_short_desc_response_model import MergeShortDescResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of MergeShortDescResponseModel from a JSON string
merge_short_desc_response_model_instance = MergeShortDescResponseModel.from_json(json)
# print the JSON string representation of the object
print MergeShortDescResponseModel.to_json()

# convert the object into a dict
merge_short_desc_response_model_dict = merge_short_desc_response_model_instance.to_dict()
# create an instance of MergeShortDescResponseModel from a dict
merge_short_desc_response_model_form_dict = merge_short_desc_response_model.from_dict(merge_short_desc_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


