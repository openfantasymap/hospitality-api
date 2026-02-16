# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.push_response import PushResponse
from openapi_server.security_api import get_token_oauth2

class BasePushResponseApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePushResponseApi.subclasses = BasePushResponseApi.subclasses + (cls,)
    async def v1_push_response_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of IDs, 'null' = No Filter), (default:'null')")],
        publisher: Annotated[Optional[StrictStr], Field(description="publisher Filter (Separator ',' List of IDs, 'null' = No Filter), (default:'null')")],
        begindate: Annotated[Optional[StrictStr], Field(description="BeginDate of Events (Format: yyyy-MM-dd), (default: 'null')")],
        enddate: Annotated[Optional[StrictStr], Field(description="EndDate of Events (Format: yyyy-MM-dd), (default: 'null')")],
        objectidlist: Optional[StrictStr],
        objecttypelist: Optional[StrictStr],
        latest: Optional[StrictBool],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[PushResponse]:
        ...


    async def single_push_response(
        self,
        id: Annotated[StrictStr, Field(description="ID of the PushResponse")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> PushResponse:
        ...


    async def v1_push_response_search_post(
        self,
        request_body: Optional[Dict[str, Any]],
    ) -> None:
        ...
