# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.urban_green_api_base import BaseUrbanGreenApi
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
from openapi_server.models.batch_crud_result import BatchCRUDResult
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.urban_green import UrbanGreen
from openapi_server.models.urban_green_json_result import UrbanGreenJsonResult
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/UrbanGreen",
    responses={
        200: {"model": UrbanGreenJsonResult, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["UrbanGreen"],
    summary="GET UrbanGreen List",
    response_model_by_alias=True,
)
async def v1_urban_green_get(
    pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")] = Query(1, description="Pagenumber", alias="pagenumber"),
    pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")] = Query(None, description="Elements per Page, (default:10)", alias="pagesize"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    langfilter: Annotated[Optional[StrictStr], Field(description="Langfilter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")] = Query(None, description="Langfilter (returns only data available in the selected Language, Separator &#39;,&#39; possible values: &#39;de,it,en,nl,sc,pl,fr,ru&#39;, &#39;null&#39;: Filter disabled)", alias="langfilter"),
    idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of IDs, 'null' = No Filter), (default:'null')")] = Query(None, description="IDFilter (Separator &#39;,&#39; List of IDs, &#39;null&#39; &#x3D; No Filter), (default:&#39;null&#39;)", alias="idlist"),
    source: Annotated[Optional[StrictStr], Field(description="Source Filter, (default:'null')")] = Query(None, description="Source Filter, (default:&#39;null&#39;)", alias="source"),
    greencode: Annotated[Optional[StrictStr], Field(description="GreenCode Filter (Separator ',' List of GreenCodes), (default:'null')")] = Query(None, description="GreenCode Filter (Separator &#39;,&#39; List of GreenCodes), (default:&#39;null&#39;)", alias="greencode"),
    greencodeversion: Annotated[Optional[StrictStr], Field(description="GreenCodeVersion Filter (Separator ',' List of GreenCodeVersions), (default:'null')")] = Query(None, description="GreenCodeVersion Filter (Separator &#39;,&#39; List of GreenCodeVersions), (default:&#39;null&#39;)", alias="greencodeversion"),
    greencodetype: Annotated[Optional[StrictStr], Field(description="GreenCodeType Filter (Separator ',' List of GreenCodeTypes), (default:'null')")] = Query(None, description="GreenCodeType Filter (Separator &#39;,&#39; List of GreenCodeTypes), (default:&#39;null&#39;)", alias="greencodetype"),
    greencodesubtype: Annotated[Optional[StrictStr], Field(description="GreenCodeSubtype Filter (Separator ',' List of GreenCodeSubtypes), (default:'null')")] = Query(None, description="GreenCodeSubtype Filter (Separator &#39;,&#39; List of GreenCodeSubtypes), (default:&#39;null&#39;)", alias="greencodesubtype"),
    activefilter: Annotated[Optional[StrictBool], Field(description="Active Filter (possible values: 'true' only Active data, 'false' only Disabled data), (default:'null')")] = Query(None, description="Active Filter (possible values: &#39;true&#39; only Active data, &#39;false&#39; only Disabled data), (default:&#39;null&#39;)", alias="activefilter"),
    tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. Syntax =and/or(TagId,TagId,TagId) example or(urbangreen:tree,urbangreen:bush) - Combining and/or is not supported at the moment. (default: 'null')")] = Query(None, description="Filter on Tags. Syntax &#x3D;and/or(TagId,TagId,TagId) example or(urbangreen:tree,urbangreen:bush) - Combining and/or is not supported at the moment. (default: &#39;null&#39;)", alias="tagfilter"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, &#39;null&#39; disables Random Sorting, (default:null)", alias="seed"),
    polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: &#39;Bounding Box Contains&#39;, &#39;bbi&#39;: &#39;Bounding Box Intersects&#39;, followed by a List of Comma Separated Longitude Latitude Tuples, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="polygon"),
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
) -> UrbanGreenJsonResult:
    if not BaseUrbanGreenApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUrbanGreenApi.subclasses[0]().v1_urban_green_get(pagenumber, pagesize, language, langfilter, idlist, source, greencode, greencodeversion, greencodetype, greencodesubtype, activefilter, tagfilter, seed, polygon, fields, searchfilter, rawfilter, rawsort, removenullvalues, getasidarray)


@router.put(
    "/v1/UrbanGreen",
    responses={
        200: {"model": BatchCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        403: {"model": ProblemDetails, "description": "Forbidden"},
        500: {"description": "Internal Server Error"},
    },
    tags=["UrbanGreen"],
    summary="PUT Upsert array of UrbanGreens with well known ids",
    response_model_by_alias=True,
)
async def v1_urban_green_put(
    urban_green: Annotated[Optional[List[UrbanGreen]], Field(description="List of UrbanGreen Objects")] = Body(None, description="List of UrbanGreen Objects"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> BatchCRUDResult:
    if not BaseUrbanGreenApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUrbanGreenApi.subclasses[0]().v1_urban_green_put(urban_green)


@router.post(
    "/v1/UrbanGreen",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["UrbanGreen"],
    summary="POST Insert new UrbanGreen",
    response_model_by_alias=True,
)
async def v1_urban_green_post(
    urban_green: Annotated[Optional[UrbanGreen], Field(description="UrbanGreen Object")] = Body(None, description="UrbanGreen Object"),
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
    if not BaseUrbanGreenApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUrbanGreenApi.subclasses[0]().v1_urban_green_post(urban_green)


@router.get(
    "/v1/UrbanGreen/{id}",
    responses={
        200: {"model": UrbanGreen, "description": "Object created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["UrbanGreen"],
    summary="GET UrbanGreen Single",
    response_model_by_alias=True,
)
async def single_urban_green(
    id: Annotated[StrictStr, Field(description="ID of the UrbanGreen")] = Path(..., description="ID of the UrbanGreen"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
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
) -> UrbanGreen:
    if not BaseUrbanGreenApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUrbanGreenApi.subclasses[0]().single_urban_green(id, language, fields, removenullvalues)


@router.put(
    "/v1/UrbanGreen/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["UrbanGreen"],
    summary="PUT Modify existing UrbanGreen",
    response_model_by_alias=True,
)
async def v1_urban_green_id_put(
    id: Annotated[StrictStr, Field(description="UrbanGreen Id")] = Path(..., description="UrbanGreen Id"),
    urban_green: Annotated[Optional[UrbanGreen], Field(description="UrbanGreen Object")] = Body(None, description="UrbanGreen Object"),
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
    if not BaseUrbanGreenApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUrbanGreenApi.subclasses[0]().v1_urban_green_id_put(id, urban_green)


@router.delete(
    "/v1/UrbanGreen/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["UrbanGreen"],
    summary="DELETE UrbanGreen by Id",
    response_model_by_alias=True,
)
async def v1_urban_green_id_delete(
    id: Annotated[StrictStr, Field(description="UrbanGreen Id")] = Path(..., description="UrbanGreen Id"),
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
    if not BaseUrbanGreenApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUrbanGreenApi.subclasses[0]().v1_urban_green_id_delete(id)
