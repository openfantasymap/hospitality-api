# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.publisher_linked import PublisherLinked
from openapi_server.security_api import get_token_oauth2

class BasePublisherApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePublisherApi.subclasses = BasePublisherApi.subclasses + (cls,)
    async def v1_publisher_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of IDs, 'null' = No Filter), (default:'null')")],
        source: Annotated[Optional[StrictStr], Field(description="Source Filter (possible Values: 'lts','idm'), (default:'null')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[PublisherLinked]:
        ...


    async def v1_publisher_post(
        self,
        publisher_linked: Annotated[Optional[PublisherLinked], Field(description="PublisherLinked Object")],
    ) -> PGCRUDResult:
        ...


    async def single_publisher(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Publisher")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        localizationlanguage: Optional[StrictStr],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> PublisherLinked:
        ...


    async def v1_publisher_id_put(
        self,
        id: Annotated[StrictStr, Field(description="Publisher Id")],
        publisher_linked: Annotated[Optional[PublisherLinked], Field(description="Publisher Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_publisher_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="Publisher Id")],
    ) -> PGCRUDResult:
        ...
