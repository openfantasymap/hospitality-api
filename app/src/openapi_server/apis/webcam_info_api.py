# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.webcam_info_api_base import BaseWebcamInfoApi
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
from openapi_server.models.webcam_info import WebcamInfo
from openapi_server.models.webcam_info_json_result import WebcamInfoJsonResult
from openapi_server.models.webcam_info_linked import WebcamInfoLinked
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/WebcamInfo",
    responses={
        200: {"model": WebcamInfoJsonResult, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["WebcamInfo"],
    summary="GET Webcam List",
    response_model_by_alias=True,
)
async def v1_webcam_info_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")] = Query(1, description="Pagenumber", alias="pagenumber"),
    pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page (default:10)")] = Query(None, description="Elements per Page (default:10)", alias="pagesize"),
    source: Annotated[Optional[StrictStr], Field(description="Source Filter (Separator ',' available sources 'lts','content'), (default:'null')")] = Query(None, description="Source Filter (Separator &#39;,&#39; available sources &#39;lts&#39;,&#39;content&#39;), (default:&#39;null&#39;)", alias="source"),
    idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of Gastronomy IDs), (default:'null')")] = Query(None, description="IDFilter (Separator &#39;,&#39; List of Gastronomy IDs), (default:&#39;null&#39;)", alias="idlist"),
    active: Annotated[Optional[StrictBool], Field(description="Active Webcam Filter (possible Values: 'true' only Active data, 'false' only Disabled data), (default:'null')")] = Query(None, description="Active Webcam Filter (possible Values: &#39;true&#39; only Active data, &#39;false&#39; only Disabled data), (default:&#39;null&#39;)", alias="active"),
    odhactive: Annotated[Optional[StrictBool], Field(description="ODH Active (Published) Webcam Filter (possible Values: 'true' only published data, 'false' only not published data), (default:'null')")] = Query(None, description="ODH Active (Published) Webcam Filter (possible Values: &#39;true&#39; only published data, &#39;false&#39; only not published data), (default:&#39;null&#39;)", alias="odhactive"),
    tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")] = Query(None, description="Filter on Tags. (Endpoint on v1/Tag) Syntax &#x3D;and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: &#39;null&#39;)", alias="tagfilter"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, not provided disables Random Sorting, (default:'null')")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, not provided disables Random Sorting, (default:&#39;null&#39;)", alias="seed"),
    latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Latitude Format: &#39;46.624975&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="latitude"),
    longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Longitude Format: &#39;11.369909&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="longitude"),
    radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="radius"),
    polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Id OR Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Id OR Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: &#39;Bounding Box Contains&#39;, &#39;bbi&#39;: &#39;Bounding Box Intersects&#39;, followed by a List of Comma Separated Longitude Latitude Tuples, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="polygon"),
    updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")] = Query(None, description="Returns data changed after this date Format (yyyy-MM-dd), (default: &#39;null&#39;)", alias="updatefrom"),
    publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")] = Query(None, description="Published On Filter (Separator &#39;,&#39; List of publisher IDs), (default:&#39;null&#39;)", alias="publishedon"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null)<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null)&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
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
) -> WebcamInfoJsonResult:
    if not BaseWebcamInfoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebcamInfoApi.subclasses[0]().v1_webcam_info_get(language, pagenumber, pagesize, source, idlist, active, odhactive, tagfilter, seed, latitude, longitude, radius, polygon, updatefrom, publishedon, fields, searchfilter, rawfilter, rawsort, removenullvalues, getasidarray)


@router.post(
    "/v1/WebcamInfo",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["WebcamInfo"],
    summary="POST Insert new WebcamInfo",
    response_model_by_alias=True,
)
async def v1_webcam_info_post(
    webcam_info_linked: Annotated[Optional[WebcamInfoLinked], Field(description="WebcamInfo Object")] = Body(None, description="WebcamInfo Object"),
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
    if not BaseWebcamInfoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebcamInfoApi.subclasses[0]().v1_webcam_info_post(webcam_info_linked)


@router.get(
    "/v1/WebcamInfo/{id}",
    responses={
        200: {"model": WebcamInfo, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["WebcamInfo"],
    summary="GET Webcam Single",
    response_model_by_alias=True,
)
async def single_webcam_info(
    id: Annotated[StrictStr, Field(description="ID of the Webcam")] = Path(..., description="ID of the Webcam"),
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
) -> WebcamInfo:
    if not BaseWebcamInfoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebcamInfoApi.subclasses[0]().single_webcam_info(id, language, fields, removenullvalues)


@router.put(
    "/v1/WebcamInfo/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["WebcamInfo"],
    summary="PUT Modify existing WebcamInfo",
    response_model_by_alias=True,
)
async def v1_webcam_info_id_put(
    id: Annotated[StrictStr, Field(description="WebcamInfo Id")] = Path(..., description="WebcamInfo Id"),
    webcam_info_linked: Annotated[Optional[WebcamInfoLinked], Field(description="WebcamInfo Object")] = Body(None, description="WebcamInfo Object"),
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
    if not BaseWebcamInfoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebcamInfoApi.subclasses[0]().v1_webcam_info_id_put(id, webcam_info_linked)


@router.delete(
    "/v1/WebcamInfo/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["WebcamInfo"],
    summary="DELETE WebcamInfo by Id",
    response_model_by_alias=True,
)
async def v1_webcam_info_id_delete(
    id: Annotated[StrictStr, Field(description="WebcamInfo Id")] = Path(..., description="WebcamInfo Id"),
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
    if not BaseWebcamInfoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebcamInfoApi.subclasses[0]().v1_webcam_info_id_delete(id)
