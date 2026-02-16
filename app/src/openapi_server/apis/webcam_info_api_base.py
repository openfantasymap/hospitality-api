# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.webcam_info import WebcamInfo
from openapi_server.models.webcam_info_json_result import WebcamInfoJsonResult
from openapi_server.models.webcam_info_linked import WebcamInfoLinked
from openapi_server.security_api import get_token_oauth2

class BaseWebcamInfoApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseWebcamInfoApi.subclasses = BaseWebcamInfoApi.subclasses + (cls,)
    async def v1_webcam_info_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page (default:10)")],
        source: Annotated[Optional[StrictStr], Field(description="Source Filter (Separator ',' available sources 'lts','content'), (default:'null')")],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of Gastronomy IDs), (default:'null')")],
        active: Annotated[Optional[StrictBool], Field(description="Active Webcam Filter (possible Values: 'true' only Active data, 'false' only Disabled data), (default:'null')")],
        odhactive: Annotated[Optional[StrictBool], Field(description="ODH Active (Published) Webcam Filter (possible Values: 'true' only published data, 'false' only not published data), (default:'null')")],
        tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, not provided disables Random Sorting, (default:'null')")],
        latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Id OR Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null)<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> WebcamInfoJsonResult:
        ...


    async def v1_webcam_info_post(
        self,
        webcam_info_linked: Annotated[Optional[WebcamInfoLinked], Field(description="WebcamInfo Object")],
    ) -> PGCRUDResult:
        ...


    async def single_webcam_info(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Webcam")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> WebcamInfo:
        ...


    async def v1_webcam_info_id_put(
        self,
        id: Annotated[StrictStr, Field(description="WebcamInfo Id")],
        webcam_info_linked: Annotated[Optional[WebcamInfoLinked], Field(description="WebcamInfo Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_webcam_info_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="WebcamInfo Id")],
    ) -> PGCRUDResult:
        ...
