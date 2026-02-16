# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.tag_api_base import BaseTagApi
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
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.tag_linked import TagLinked
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/Tag",
    responses={
        200: {"model": List[TagLinked], "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Tag"],
    summary="GET Tag List",
    response_model_by_alias=True,
)
async def v1_tag_get(
    pagenumber: Optional[StrictInt] = Query(1, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of IDs, 'null' = No Filter), (default:'null')")] = Query(None, description="IDFilter (Separator &#39;,&#39; List of IDs, &#39;null&#39; &#x3D; No Filter), (default:&#39;null&#39;)", alias="idlist"),
    validforentity: Annotated[Optional[StrictStr], Field(description="Filter on Tags valid on Entities (accommodation, activity, poi, odhactivitypoi, package, gastronomy, event, article, common .. etc..),(Separator ',' List of odhtypes) (default:'null')")] = Query(None, description="Filter on Tags valid on Entities (accommodation, activity, poi, odhactivitypoi, package, gastronomy, event, article, common .. etc..),(Separator &#39;,&#39; List of odhtypes) (default:&#39;null&#39;)", alias="validforentity"),
    types: Annotated[Optional[StrictStr], Field(description="Filter on Tags with this Types (Separator ',' List of types), (default:'null')")] = Query(None, description="Filter on Tags with this Types (Separator &#39;,&#39; List of types), (default:&#39;null&#39;)", alias="types"),
    displayascategory: Annotated[Optional[StrictBool], Field(description="true = returns only Tags which are marked as DisplayAsCategory true")] = Query(None, description="true &#x3D; returns only Tags which are marked as DisplayAsCategory true", alias="displayascategory"),
    publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")] = Query(None, description="Published On Filter (Separator &#39;,&#39; List of publisher IDs), (default:&#39;null&#39;)", alias="publishedon"),
    source: Annotated[Optional[StrictStr], Field(description="Source Filter (possible Values: 'lts','idm), (default:'null')")] = Query(None, description="Source Filter (possible Values: &#39;lts&#39;,&#39;idm), (default:&#39;null&#39;)", alias="source"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Get result only as Array of Ids, (default:false)  Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="getasidarray"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[TagLinked]:
    if not BaseTagApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTagApi.subclasses[0]().v1_tag_get(pagenumber, pagesize, language, idlist, validforentity, types, displayascategory, publishedon, source, fields, searchfilter, rawfilter, rawsort, removenullvalues, getasidarray)


@router.post(
    "/v1/Tag",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Tag"],
    summary="POST Insert new Tag",
    response_model_by_alias=True,
)
async def v1_tag_post(
    generateid: Optional[StrictBool] = Query(True, description="", alias="generateid"),
    tag_linked: Annotated[Optional[TagLinked], Field(description="Tag Object")] = Body(None, description="Tag Object"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> PGCRUDResult:
    if not BaseTagApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTagApi.subclasses[0]().v1_tag_post(generateid, tag_linked)


@router.get(
    "/v1/Tag/{id}",
    responses={
        200: {"model": TagLinked, "description": "Object created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Tag"],
    summary="GET Tag Single",
    response_model_by_alias=True,
)
async def single_tag(
    id: Annotated[StrictStr, Field(description="ID of the Tag")] = Path(..., description="ID of the Tag"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    localizationlanguage: Optional[StrictStr] = Query(None, description="", alias="localizationlanguage"),
    removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")] = Query(False, description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Opendatahub Wiki&lt;/a&gt;", alias="removenullvalues"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> TagLinked:
    if not BaseTagApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTagApi.subclasses[0]().single_tag(id, language, fields, localizationlanguage, removenullvalues)


@router.put(
    "/v1/Tag/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Tag"],
    summary="PUT Modify existing Tag",
    response_model_by_alias=True,
)
async def v1_tag_id_put(
    id: Annotated[StrictStr, Field(description="Tag Id")] = Path(..., description="Tag Id"),
    tag_linked: Annotated[Optional[TagLinked], Field(description="Tag Object")] = Body(None, description="Tag Object"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> PGCRUDResult:
    if not BaseTagApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTagApi.subclasses[0]().v1_tag_id_put(id, tag_linked)


@router.delete(
    "/v1/Tag/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Tag"],
    summary="DELETE Tag by Id",
    response_model_by_alias=True,
)
async def v1_tag_id_delete(
    id: Annotated[StrictStr, Field(description="Tag Id")] = Path(..., description="Tag Id"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> PGCRUDResult:
    if not BaseTagApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTagApi.subclasses[0]().v1_tag_id_delete(id)
