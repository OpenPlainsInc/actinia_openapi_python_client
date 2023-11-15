# ProcessLogModel

This class defines the model for Unix process information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the executable | [optional] 
**executable** | **str** | The name of the executable | 
**parameter** | **List[str]** | The parameter of the executable | 
**stdout** | **str** | The stdout output of the executable | 
**stderr** | **List[str]** | The stderr output of the executable as list of strings | 
**return_code** | **float** | The return code of the executable | 
**run_time** | **float** | The runtime of the executable in seconds | [optional] 
**mapset_size** | **float** | The size of the mapset in bytes | [optional] 

## Example

```python
from actinia_openapi_python_client.models.process_log_model import ProcessLogModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessLogModel from a JSON string
process_log_model_instance = ProcessLogModel.from_json(json)
# print the JSON string representation of the object
print ProcessLogModel.to_json()

# convert the object into a dict
process_log_model_dict = process_log_model_instance.to_dict()
# create an instance of ProcessLogModel from a dict
process_log_model_form_dict = process_log_model.from_dict(process_log_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


