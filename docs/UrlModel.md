# UrlModel

URL schema that points to the status URL

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The URL to check the status of the resource | 
**resources** | **List[str]** | A list of URLs to generated resources, that may be GeoTiff files, vector files, ASCII files or png images | 

## Example

```python
from actinia_openapi_python_client.models.url_model import UrlModel

# TODO update the JSON string below
json = "{}"
# create an instance of UrlModel from a JSON string
url_model_instance = UrlModel.from_json(json)
# print the JSON string representation of the object
print UrlModel.to_json()

# convert the object into a dict
url_model_dict = url_model_instance.to_dict()
# create an instance of UrlModel from a dict
url_model_form_dict = url_model.from_dict(url_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


