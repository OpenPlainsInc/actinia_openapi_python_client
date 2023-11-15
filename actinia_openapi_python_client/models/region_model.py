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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RegionModel(BaseModel):
    """
    Output of GRASS GIS module g.region -gu3
    """ # noqa: E501
    projection: Optional[Union[StrictFloat, StrictInt]] = None
    zone: Optional[Union[StrictFloat, StrictInt]] = None
    n: Optional[Union[StrictFloat, StrictInt]] = None
    s: Optional[Union[StrictFloat, StrictInt]] = None
    w: Optional[Union[StrictFloat, StrictInt]] = None
    e: Optional[Union[StrictFloat, StrictInt]] = None
    t: Optional[Union[StrictFloat, StrictInt]] = None
    b: Optional[Union[StrictFloat, StrictInt]] = None
    nsres: Optional[Union[StrictFloat, StrictInt]] = None
    nsres3: Optional[Union[StrictFloat, StrictInt]] = None
    ewres: Optional[Union[StrictFloat, StrictInt]] = None
    ewres3: Optional[Union[StrictFloat, StrictInt]] = None
    tbres: Optional[Union[StrictFloat, StrictInt]] = None
    rows: Optional[Union[StrictFloat, StrictInt]] = None
    rows3: Optional[Union[StrictFloat, StrictInt]] = None
    cols: Optional[Union[StrictFloat, StrictInt]] = None
    cols3: Optional[Union[StrictFloat, StrictInt]] = None
    depths: Optional[Union[StrictFloat, StrictInt]] = None
    cells: Optional[Union[StrictFloat, StrictInt]] = None
    cells3: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["projection", "zone", "n", "s", "w", "e", "t", "b", "nsres", "nsres3", "ewres", "ewres3", "tbres", "rows", "rows3", "cols", "cols3", "depths", "cells", "cells3"]

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
        """Create an instance of RegionModel from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RegionModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "projection": obj.get("projection"),
            "zone": obj.get("zone"),
            "n": obj.get("n"),
            "s": obj.get("s"),
            "w": obj.get("w"),
            "e": obj.get("e"),
            "t": obj.get("t"),
            "b": obj.get("b"),
            "nsres": obj.get("nsres"),
            "nsres3": obj.get("nsres3"),
            "ewres": obj.get("ewres"),
            "ewres3": obj.get("ewres3"),
            "tbres": obj.get("tbres"),
            "rows": obj.get("rows"),
            "rows3": obj.get("rows3"),
            "cols": obj.get("cols"),
            "cols3": obj.get("cols3"),
            "depths": obj.get("depths"),
            "cells": obj.get("cells"),
            "cells3": obj.get("cells3")
        })
        return _obj


