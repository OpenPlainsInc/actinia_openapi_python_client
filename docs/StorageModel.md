# StorageModel

This class defines the model to inform about available storage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **float** | The used storage in bytes | 
**free** | **float** | The free storage in bytes | 
**quota** | **float** | The current quota in bytes | 
**free_percent** | **float** | The free storage in percent | 

## Example

```python
from actinia_openapi_python_client.models.storage_model import StorageModel

# TODO update the JSON string below
json = "{}"
# create an instance of StorageModel from a JSON string
storage_model_instance = StorageModel.from_json(json)
# print the JSON string representation of the object
print StorageModel.to_json()

# convert the object into a dict
storage_model_dict = storage_model_instance.to_dict()
# create an instance of StorageModel from a dict
storage_model_form_dict = storage_model.from_dict(storage_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


