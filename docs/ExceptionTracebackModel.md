# ExceptionTracebackModel

Response schema that contains python3 exception information of the called

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message that was send with the exception | 
**type** | **str** | The type of the exception | 
**traceback** | **List[str]** | The full traceback of the exception | 

## Example

```python
from actinia_openapi_python_client.models.exception_traceback_model import ExceptionTracebackModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionTracebackModel from a JSON string
exception_traceback_model_instance = ExceptionTracebackModel.from_json(json)
# print the JSON string representation of the object
print ExceptionTracebackModel.to_json()

# convert the object into a dict
exception_traceback_model_dict = exception_traceback_model_instance.to_dict()
# create an instance of ExceptionTracebackModel from a dict
exception_traceback_model_form_dict = exception_traceback_model.from_dict(exception_traceback_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


