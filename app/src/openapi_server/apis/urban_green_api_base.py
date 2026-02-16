# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.batch_crud_result import BatchCRUDResult
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.urban_green import UrbanGreen
from openapi_server.models.urban_green_json_result import UrbanGreenJsonResult
from openapi_server.security_api import get_token_oauth2

class BaseUrbanGreenApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUrbanGreenApi.subclasses = BaseUrbanGreenApi.subclasses + (cls,)
    async def v1_urban_green_get(
        self,
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        langfilter: Annotated[Optional[StrictStr], Field(description="Langfilter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of IDs, 'null' = No Filter), (default:'null')")],
        source: Annotated[Optional[StrictStr], Field(description="Source Filter, (default:'null')")],
        greencode: Annotated[Optional[StrictStr], Field(description="GreenCode Filter (Separator ',' List of GreenCodes), (default:'null')")],
        greencodeversion: Annotated[Optional[StrictStr], Field(description="GreenCodeVersion Filter (Separator ',' List of GreenCodeVersions), (default:'null')")],
        greencodetype: Annotated[Optional[StrictStr], Field(description="GreenCodeType Filter (Separator ',' List of GreenCodeTypes), (default:'null')")],
        greencodesubtype: Annotated[Optional[StrictStr], Field(description="GreenCodeSubtype Filter (Separator ',' List of GreenCodeSubtypes), (default:'null')")],
        activefilter: Annotated[Optional[StrictBool], Field(description="Active Filter (possible values: 'true' only Active data, 'false' only Disabled data), (default:'null')")],
        tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. Syntax =and/or(TagId,TagId,TagId) example or(urbangreen:tree,urbangreen:bush) - Combining and/or is not supported at the moment. (default: 'null')")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> UrbanGreenJsonResult:
        ...


    async def v1_urban_green_put(
        self,
        urban_green: Annotated[Optional[List[UrbanGreen]], Field(description="List of UrbanGreen Objects")],
    ) -> BatchCRUDResult:
        ...


    async def v1_urban_green_post(
        self,
        urban_green: Annotated[Optional[UrbanGreen], Field(description="UrbanGreen Object")],
    ) -> PGCRUDResult:
        ...


    async def single_urban_green(
        self,
        id: Annotated[StrictStr, Field(description="ID of the UrbanGreen")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> UrbanGreen:
        ...


    async def v1_urban_green_id_put(
        self,
        id: Annotated[StrictStr, Field(description="UrbanGreen Id")],
        urban_green: Annotated[Optional[UrbanGreen], Field(description="UrbanGreen Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_urban_green_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="UrbanGreen Id")],
    ) -> PGCRUDResult:
        ...
