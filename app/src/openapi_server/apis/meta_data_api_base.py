# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.tourism_meta_data import TourismMetaData
from openapi_server.models.tourism_meta_data_json_result import TourismMetaDataJsonResult
from openapi_server.security_api import get_token_oauth2

class BaseMetaDataApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMetaDataApi.subclasses = BaseMetaDataApi.subclasses + (cls,)
    async def tourism_api(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="[not implemented] Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Shortname and ApiDescription in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> TourismMetaDataJsonResult:
        ...


    async def tourism_api_meta_data(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="[not implemented] Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Shortname and ApiDescription in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> TourismMetaDataJsonResult:
        ...


    async def v1_meta_data_post(
        self,
        tourism_meta_data: Annotated[Optional[TourismMetaData], Field(description="TourismMetaData Object")],
    ) -> PGCRUDResult:
        ...


    async def single_meta_data(
        self,
        id: Annotated[StrictStr, Field(description="ID of the MetaData")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> TourismMetaData:
        ...


    async def v1_meta_data_id_put(
        self,
        id: Annotated[StrictStr, Field(description="MetaData Id")],
        tourism_meta_data: Annotated[Optional[TourismMetaData], Field(description="TourismMetaData Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_meta_data_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="MetaData Id")],
    ) -> PGCRUDResult:
        ...
