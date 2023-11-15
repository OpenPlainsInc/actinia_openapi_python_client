# coding: utf-8

"""
    Actinia

     ================================ Actinia - The GRASS GIS REST API ================================  **Actinia** is an open source REST API for scalable, distributed, high performance processing of geographical data that uses GRASS GIS for computational tasks.  It provides a REST API to process satellite images, time series of satellite images, arbitrary raster data with geographical relations and vector data.  The REST interface allows to access, manage and manipulate the GRASS GIS database via HTTP GET,PUT,POST and DELETE requests and to process raster, vector and time series data located in a persistent GRASS GIS database. **Actinia** allows the processing of cloud based data, for example all Landsat 4-8 scenes as well as all Sentinel2A scenes in an ephemeral databases. The computational results of ephemeral processing are available via object storage as GeoTIFF files.  The full API documentation is available here: https://redocly.github.io/redoc/?url=https://actinia.mundialis.de/latest/ swagger.json   Examples: ---------  To execute the examples, first setup login information, IP address and port:      export ACTINIA_URL=https://actinia.mundialis.de/latest     export AUTH='-u demouser:gu3st!pa55w0rd'  **Data management**  - List all locations that are available in the actinia persistent database:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations\"  - List all mapsets in the location latlong_wgs84:      curl ${AUTH} -X GET \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets\"  - List all raster layers in location latlong_wgs84 and mapset Sentinel2A      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/latlong_wgs84/mapsets/Sentinel2A/raster_layers\"  - List all space-time raster datasets (STRDS) in location ECAD and mapset   PERMANENT:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/raster_layers\"  - List all raster map layers of the STRDS precipitation_1950_2013_yearly_mm:      curl ${AUTH} -X GET     \"${ACTINIA_URL}/locations/ECAD/mapsets/PERMANENT/strds/precipitation_    1950_2013_yearly_mm/raster_layers\"  **Landsat and Sentinel2A NDVI computation**  This API call will compute the NDVI of the top of atmosphere (TOAR) corrected Landsat4 scene LC80440342016259LGN00:      curl ${AUTH} -X POST \"${ACTINIA_URL}/landsat_process/    LC80440342016259LGN00/TOAR/NDVI\"  NDVI computation of Sentinel2A scene S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138:      curl ${AUTH} -X POST \"${ACTINIA_URL}/sentinel2_process/ndvi/    S2A_MSIL1C_20170212T104141_N0204_R008_T31TGJ_20170212T104138\"  The results of the asynchronous computations are available as GeoTIFF file in a cloud storage for download. 

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from actinia_openapi_python_client.models.vector_attribute_model import VectorAttributeModel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VectorInfoModel(BaseModel):
    """
    Description of a GRASS GIS vector map layer
    """ # noqa: E501
    attributes: Optional[List[VectorAttributeModel]] = Field(default=None, alias="Attributes")
    command: Optional[StrictStr] = Field(default=None, alias="COMMAND")
    areas: Optional[StrictStr] = None
    bottom: Optional[StrictStr] = None
    boundaries: Optional[StrictStr] = None
    centroids: Optional[StrictStr] = None
    comment: Optional[StrictStr] = None
    creator: Optional[StrictStr] = None
    database: Optional[StrictStr] = None
    digitization_threshold: Optional[StrictStr] = None
    east: Optional[StrictStr] = None
    faces: Optional[StrictStr] = None
    format: Optional[StrictStr] = None
    holes: Optional[StrictStr] = None
    islands: Optional[StrictStr] = None
    kernels: Optional[StrictStr] = None
    level: Optional[StrictStr] = None
    lines: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    map3d: Optional[StrictStr] = None
    mapset: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    nodes: Optional[StrictStr] = None
    north: Optional[StrictStr] = None
    num_dblinks: Optional[StrictStr] = None
    organization: Optional[StrictStr] = None
    points: Optional[StrictStr] = None
    primitives: Optional[StrictStr] = None
    projection: Optional[StrictStr] = None
    zone: Optional[StrictStr] = None
    scale: Optional[StrictStr] = None
    source_date: Optional[StrictStr] = None
    south: Optional[StrictStr] = None
    timestamp: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    top: Optional[StrictStr] = None
    volumes: Optional[StrictStr] = None
    west: Optional[StrictStr] = None
    attribute_layer_name: Optional[StrictStr] = None
    attribute_table: Optional[StrictStr] = None
    attribute_database_driver: Optional[StrictStr] = None
    attribute_database: Optional[StrictStr] = None
    attribute_primary_key: Optional[StrictStr] = None
    attribute_layer_number: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["Attributes", "COMMAND", "areas", "bottom", "boundaries", "centroids", "comment", "creator", "database", "digitization_threshold", "east", "faces", "format", "holes", "islands", "kernels", "level", "lines", "location", "map3d", "mapset", "name", "nodes", "north", "num_dblinks", "organization", "points", "primitives", "projection", "zone", "scale", "source_date", "south", "timestamp", "title", "top", "volumes", "west", "attribute_layer_name", "attribute_table", "attribute_database_driver", "attribute_database", "attribute_primary_key", "attribute_layer_number"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VectorInfoModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Attributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of VectorInfoModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Attributes": [VectorAttributeModel.from_dict(_item) for _item in obj.get("Attributes")] if obj.get("Attributes") is not None else None,
            "COMMAND": obj.get("COMMAND"),
            "areas": obj.get("areas"),
            "bottom": obj.get("bottom"),
            "boundaries": obj.get("boundaries"),
            "centroids": obj.get("centroids"),
            "comment": obj.get("comment"),
            "creator": obj.get("creator"),
            "database": obj.get("database"),
            "digitization_threshold": obj.get("digitization_threshold"),
            "east": obj.get("east"),
            "faces": obj.get("faces"),
            "format": obj.get("format"),
            "holes": obj.get("holes"),
            "islands": obj.get("islands"),
            "kernels": obj.get("kernels"),
            "level": obj.get("level"),
            "lines": obj.get("lines"),
            "location": obj.get("location"),
            "map3d": obj.get("map3d"),
            "mapset": obj.get("mapset"),
            "name": obj.get("name"),
            "nodes": obj.get("nodes"),
            "north": obj.get("north"),
            "num_dblinks": obj.get("num_dblinks"),
            "organization": obj.get("organization"),
            "points": obj.get("points"),
            "primitives": obj.get("primitives"),
            "projection": obj.get("projection"),
            "zone": obj.get("zone"),
            "scale": obj.get("scale"),
            "source_date": obj.get("source_date"),
            "south": obj.get("south"),
            "timestamp": obj.get("timestamp"),
            "title": obj.get("title"),
            "top": obj.get("top"),
            "volumes": obj.get("volumes"),
            "west": obj.get("west"),
            "attribute_layer_name": obj.get("attribute_layer_name"),
            "attribute_table": obj.get("attribute_table"),
            "attribute_database_driver": obj.get("attribute_database_driver"),
            "attribute_database": obj.get("attribute_database"),
            "attribute_primary_key": obj.get("attribute_primary_key"),
            "attribute_layer_number": obj.get("attribute_layer_number")
        })
        return _obj

