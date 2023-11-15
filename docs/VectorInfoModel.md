# VectorInfoModel

Description of a GRASS GIS vector map layer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[VectorAttributeModel]**](VectorAttributeModel.md) |  | [optional] 
**command** | **str** |  | [optional] 
**areas** | **str** |  | [optional] 
**bottom** | **str** |  | [optional] 
**boundaries** | **str** |  | [optional] 
**centroids** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**creator** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**digitization_threshold** | **str** |  | [optional] 
**east** | **str** |  | [optional] 
**faces** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**holes** | **str** |  | [optional] 
**islands** | **str** |  | [optional] 
**kernels** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**lines** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**map3d** | **str** |  | [optional] 
**mapset** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nodes** | **str** |  | [optional] 
**north** | **str** |  | [optional] 
**num_dblinks** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**points** | **str** |  | [optional] 
**primitives** | **str** |  | [optional] 
**projection** | **str** |  | [optional] 
**zone** | **str** |  | [optional] 
**scale** | **str** |  | [optional] 
**source_date** | **str** |  | [optional] 
**south** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**top** | **str** |  | [optional] 
**volumes** | **str** |  | [optional] 
**west** | **str** |  | [optional] 
**attribute_layer_name** | **str** |  | [optional] 
**attribute_table** | **str** |  | [optional] 
**attribute_database_driver** | **str** |  | [optional] 
**attribute_database** | **str** |  | [optional] 
**attribute_primary_key** | **str** |  | [optional] 
**attribute_layer_number** | **str** |  | [optional] 

## Example

```python
from actinia_openapi_python_client.models.vector_info_model import VectorInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of VectorInfoModel from a JSON string
vector_info_model_instance = VectorInfoModel.from_json(json)
# print the JSON string representation of the object
print VectorInfoModel.to_json()

# convert the object into a dict
vector_info_model_dict = vector_info_model_instance.to_dict()
# create an instance of VectorInfoModel from a dict
vector_info_model_form_dict = vector_info_model.from_dict(vector_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


