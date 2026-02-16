# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.deprecated_api_base import BaseDeprecatedApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/Deprecated",
    responses={
        200: {"model": List[str], "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Deprecated"],
    summary="GET Generic Deprecated search of fields",
    response_model_by_alias=True,
)
async def v1_deprecated_get(
    pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")] = Query(None, description="Pagenumber", alias="pagenumber"),
    pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")] = Query(None, description="Elements per Page, (default:10)", alias="pagesize"),
    odhtype: Optional[StrictStr] = Query(None, description="", alias="odhtype"),
    type: Annotated[Optional[StrictStr], Field(description="Mandatory search trough Entities (metadata, accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... null = search trough all entities) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\" target=\"_blank\">Wiki Dataset Type</a>")] = Query(None, description="Mandatory search trough Entities (metadata, accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... null &#x3D; search trough all entities) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki Dataset Type&lt;/a&gt;", alias="type"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Mandatory Select a field for the Distinct Query, example fields=Source, arrays are selected with a [*] example HasLanguage[*] / Features[*].Id  (Only one field supported). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Mandatory Select a field for the Distinct Query, example fields&#x3D;Source, arrays are selected with a [*] example HasLanguage[*] / Features[*].Id  (Only one field supported). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, &#39;null&#39; disables Random Sorting, (default:null)", alias="seed"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
    getasarray: Annotated[Optional[StrictBool], Field(description="Get only first selected field as simple string Array")] = Query(False, description="Get only first selected field as simple string Array", alias="getasarray"),
    excludenulloremptyvalues: Annotated[Optional[StrictBool], Field(description="Exclude empty and null values from output")] = Query(False, description="Exclude empty and null values from output", alias="excludenulloremptyvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[str]:
    if not BaseDeprecatedApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDeprecatedApi.subclasses[0]().v1_deprecated_get(pagenumber, pagesize, odhtype, type, fields, seed, rawfilter, rawsort, getasarray, excludenulloremptyvalues)
