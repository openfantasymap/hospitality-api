# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.tag_linked import TagLinked
from openapi_server.security_api import get_token_oauth2

class BaseTagApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTagApi.subclasses = BaseTagApi.subclasses + (cls,)
    async def v1_tag_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of IDs, 'null' = No Filter), (default:'null')")],
        validforentity: Annotated[Optional[StrictStr], Field(description="Filter on Tags valid on Entities (accommodation, activity, poi, odhactivitypoi, package, gastronomy, event, article, common .. etc..),(Separator ',' List of odhtypes) (default:'null')")],
        types: Annotated[Optional[StrictStr], Field(description="Filter on Tags with this Types (Separator ',' List of types), (default:'null')")],
        displayascategory: Annotated[Optional[StrictBool], Field(description="true = returns only Tags which are marked as DisplayAsCategory true")],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        source: Annotated[Optional[StrictStr], Field(description="Source Filter (possible Values: 'lts','idm), (default:'null')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[TagLinked]:
        ...


    async def v1_tag_post(
        self,
        generateid: Optional[StrictBool],
        tag_linked: Annotated[Optional[TagLinked], Field(description="Tag Object")],
    ) -> PGCRUDResult:
        ...


    async def single_tag(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Tag")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        localizationlanguage: Optional[StrictStr],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> TagLinked:
        ...


    async def v1_tag_id_put(
        self,
        id: Annotated[StrictStr, Field(description="Tag Id")],
        tag_linked: Annotated[Optional[TagLinked], Field(description="Tag Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_tag_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="Tag Id")],
    ) -> PGCRUDResult:
        ...
