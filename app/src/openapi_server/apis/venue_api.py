# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.venue_api_base import BaseVenueApi
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
from openapi_server.models.dd_venue_codes import DDVenueCodes
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.venue_v2 import VenueV2
from openapi_server.models.venue_v2_json_result import VenueV2JsonResult
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/Venue",
    responses={
        200: {"model": VenueV2JsonResult, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Venue"],
    summary="GET Venue List",
    response_model_by_alias=True,
)
async def v1_venue_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")] = Query(1, description="Pagenumber", alias="pagenumber"),
    pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page (max 1024), (default:10)")] = Query(None, description="Elements per Page (max 1024), (default:10)", alias="pagesize"),
    categoryfilter: Annotated[Optional[StrictStr], Field(description="Venue Category Filter (BITMASK) (Separator ',' List of Venuetype Bitmasks, refer to api/VenueTypes type:category), (default:'null')")] = Query(None, description="Venue Category Filter (BITMASK) (Separator &#39;,&#39; List of Venuetype Bitmasks, refer to api/VenueTypes type:category), (default:&#39;null&#39;)", alias="categoryfilter"),
    idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of Venue IDs), (default:'null')")] = Query(None, description="IDFilter (Separator &#39;,&#39; List of Venue IDs), (default:&#39;null&#39;)", alias="idlist"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")] = Query(None, description="Locfilter SPECIAL Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki locfilter&lt;/a&gt;", alias="locfilter"),
    featurefilter: Annotated[Optional[StrictStr], Field(description="Venue Features Filter (BITMASK) (Separator ',' List of Venuetype Bitmasks, refer to api/VenueTypes type:feature), (default:'null')")] = Query(None, description="Venue Features Filter (BITMASK) (Separator &#39;,&#39; List of Venuetype Bitmasks, refer to api/VenueTypes type:feature), (default:&#39;null&#39;)", alias="featurefilter"),
    setuptypefilter: Annotated[Optional[StrictStr], Field(description="Venue SetupType Filter (BITMASK) (Separator ',' List of Venuetype Bitmasks, refer to api/VenueTypes type:seatType), (default:'null')")] = Query(None, description="Venue SetupType Filter (BITMASK) (Separator &#39;,&#39; List of Venuetype Bitmasks, refer to api/VenueTypes type:seatType), (default:&#39;null&#39;)", alias="setuptypefilter"),
    odhtagfilter: Optional[StrictStr] = Query(None, description="", alias="odhtagfilter"),
    tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")] = Query(None, description="Filter on Tags. (Endpoint on v1/Tag) Syntax &#x3D;and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: &#39;null&#39;)", alias="tagfilter"),
    source: Annotated[Optional[StrictStr], Field(description="Source Filter(String, ), (default:'null')")] = Query(None, description="Source Filter(String, ), (default:&#39;null&#39;)", alias="source"),
    active: Annotated[Optional[StrictBool], Field(description="Active Venue Filter (possible Values: 'true' only Active Venues, 'false' only Disabled Venues), (default:'null')")] = Query(None, description="Active Venue Filter (possible Values: &#39;true&#39; only Active Venues, &#39;false&#39; only Disabled Venues), (default:&#39;null&#39;)", alias="active"),
    publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")] = Query(None, description="Published On Filter (Separator &#39;,&#39; List of publisher IDs), (default:&#39;null&#39;)", alias="publishedon"),
    updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")] = Query(None, description="Returns data changed after this date Format (yyyy-MM-dd), (default: &#39;null&#39;)", alias="updatefrom"),
    langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")] = Query(None, description="Language filter (returns only data available in the selected Language, Separator &#39;,&#39; possible values: &#39;de,it,en,nl,sc,pl,fr,ru&#39;, &#39;null&#39;: Filter disabled)", alias="langfilter"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, not provided disables Random Sorting, (default:'null')")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, not provided disables Random Sorting, (default:&#39;null&#39;)", alias="seed"),
    latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Latitude Format: &#39;46.624975&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="latitude"),
    longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Longitude Format: &#39;11.369909&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="longitude"),
    radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="radius"),
    polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: &#39;Bounding Box Contains&#39;, &#39;bbi&#39;: &#39;Bounding Box Intersects&#39;, followed by a List of Comma Separated Longitude Latitude Tuples, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="polygon"),
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
) -> VenueV2JsonResult:
    if not BaseVenueApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVenueApi.subclasses[0]().v1_venue_get(language, pagenumber, pagesize, categoryfilter, idlist, locfilter, featurefilter, setuptypefilter, odhtagfilter, tagfilter, source, active, publishedon, updatefrom, langfilter, seed, latitude, longitude, radius, polygon, fields, searchfilter, rawfilter, rawsort, removenullvalues, getasidarray)


@router.post(
    "/v1/Venue",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Venue"],
    summary="POST Insert new Venue",
    response_model_by_alias=True,
)
async def v1_venue_post(
    venue_v2: Annotated[Optional[VenueV2], Field(description="Venue Object")] = Body(None, description="Venue Object"),
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
    if not BaseVenueApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVenueApi.subclasses[0]().v1_venue_post(venue_v2)


@router.get(
    "/v1/Venue/{id}",
    responses={
        200: {"model": VenueV2, "description": "Object created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Venue"],
    summary="GET Venue Single",
    response_model_by_alias=True,
)
async def single_venue(
    id: Annotated[StrictStr, Field(description="ID of the Venue")] = Path(..., description="ID of the Venue"),
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
) -> VenueV2:
    if not BaseVenueApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVenueApi.subclasses[0]().single_venue(id, language, fields, removenullvalues)


@router.put(
    "/v1/Venue/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Venue"],
    summary="PUT Modify existing Venue",
    response_model_by_alias=True,
)
async def v1_venue_id_put(
    id: Annotated[StrictStr, Field(description="Venue Id")] = Path(..., description="Venue Id"),
    venue_v2: Annotated[Optional[VenueV2], Field(description="Venue Object")] = Body(None, description="Venue Object"),
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
    if not BaseVenueApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVenueApi.subclasses[0]().v1_venue_id_put(id, venue_v2)


@router.delete(
    "/v1/Venue/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Venue"],
    summary="DELETE Venue by Id",
    response_model_by_alias=True,
)
async def v1_venue_id_delete(
    id: Annotated[StrictStr, Field(description="Venue Id")] = Path(..., description="Venue Id"),
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
    if not BaseVenueApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVenueApi.subclasses[0]().v1_venue_id_delete(id)


@router.get(
    "/v1/VenueTypes",
    responses={
        200: {"model": List[DDVenueCodes], "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Venue"],
    summary="GET Venue Types List",
    response_model_by_alias=True,
)
async def v1_venue_types_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    idlist: Optional[StrictStr] = Query(None, description="", alias="idlist"),
    seed: Optional[StrictStr] = Query(None, description="", alias="seed"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null)<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null)&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
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
) -> List[DDVenueCodes]:
    if not BaseVenueApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVenueApi.subclasses[0]().v1_venue_types_get(language, pagenumber, pagesize, idlist, seed, fields, searchfilter, rawfilter, rawsort, removenullvalues)


@router.get(
    "/v1/VenueTypes/{id}",
    responses={
        200: {"model": DDVenueCodes, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Venue"],
    summary="GET Venue Types Single",
    response_model_by_alias=True,
)
async def single_venue_types(
    id: Annotated[StrictStr, Field(description="ID of the VenueType")] = Path(..., description="ID of the VenueType"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname. Select also Dictionary fields, example Detail.de.Title, or Elements of Arrays example ImageGallery[0].ImageUrl. (default:'null' all fields are displayed)")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname. Select also Dictionary fields, example Detail.de.Title, or Elements of Arrays example ImageGallery[0].ImageUrl. (default:&#39;null&#39; all fields are displayed)", alias="fields"),
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
) -> DDVenueCodes:
    if not BaseVenueApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVenueApi.subclasses[0]().single_venue_types(id, language, fields, removenullvalues)
