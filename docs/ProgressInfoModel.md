# ProgressInfoModel

This class defines the model for progress information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step** | **int** | The current processing step | 
**num_of_steps** | **int** | The total number of processing steps | 
**sub_step** | **int** | The current sub step of the current processing step | [optional] 
**num_of_sub_steps** | **int** | The total number of sub steps of the current processing step | [optional] 

## Example

```python
from actinia_openapi_python_client.models.progress_info_model import ProgressInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressInfoModel from a JSON string
progress_info_model_instance = ProgressInfoModel.from_json(json)
# print the JSON string representation of the object
print ProgressInfoModel.to_json()

# convert the object into a dict
progress_info_model_dict = progress_info_model_instance.to_dict()
# create an instance of ProgressInfoModel from a dict
progress_info_model_form_dict = progress_info_model.from_dict(progress_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


