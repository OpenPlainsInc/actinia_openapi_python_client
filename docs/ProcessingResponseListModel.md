# ProcessingResponseListModel

Response schema that represent a list of ProcessingResponseModel's

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_list** | [**List[ProcessingResponseModel]**](ProcessingResponseModel.md) | A list of ProcessingResponseModel objects | 

## Example

```python
from actinia_openapi_python_client.models.processing_response_list_model import ProcessingResponseListModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingResponseListModel from a JSON string
processing_response_list_model_instance = ProcessingResponseListModel.from_json(json)
# print the JSON string representation of the object
print ProcessingResponseListModel.to_json()

# convert the object into a dict
processing_response_list_model_dict = processing_response_list_model_instance.to_dict()
# create an instance of ProcessingResponseListModel from a dict
processing_response_list_model_form_dict = processing_response_list_model.from_dict(processing_response_list_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


