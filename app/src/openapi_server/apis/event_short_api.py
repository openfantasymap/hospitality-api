# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.event_short_api_base import BaseEventShortApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.event_short import EventShort
from openapi_server.models.event_short_by_room import EventShortByRoom
from openapi_server.models.event_short_linked import EventShortLinked
from openapi_server.models.event_short_result import EventShortResult
from openapi_server.models.event_short_types import EventShortTypes
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/EventShort",
    responses={
        200: {"model": EventShortResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    summary="GET EventShort List",
    response_model_by_alias=True,
)
async def v1_event_short_get(
    pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber (Integer)")] = Query(1, description="Pagenumber (Integer)", alias="pagenumber"),
    pagesize: Annotated[Optional[StrictInt], Field(description="Pagesize (Integer), (default: 'null')")] = Query(None, description="Pagesize (Integer), (default: &#39;null&#39;)", alias="pagesize"),
    startdate: Annotated[Optional[StrictStr], Field(description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp")] = Query(None, description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp", alias="startdate"),
    enddate: Annotated[Optional[StrictStr], Field(description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp")] = Query(None, description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp", alias="enddate"),
    datetimeformat: Annotated[Optional[StrictStr], Field(description="not provided, use default format, for unix timestamp pass \"uxtimestamp\"")] = Query(None, description="not provided, use default format, for unix timestamp pass \&quot;uxtimestamp\&quot;", alias="datetimeformat"),
    source: Annotated[Optional[StrictStr], Field(description="Source of the data, (possible values 'Content' or 'EBMS')")] = Query(None, description="Source of the data, (possible values &#39;Content&#39; or &#39;EBMS&#39;)", alias="source"),
    eventlocation: Annotated[Optional[StrictStr], Field(description="<p>Members:</p><ul><li><i>NOI</i> - NOI Techpark</li> <li><i>EC</i> - Eurac</li> <li><i>VV</i> - Virtual Village</li> <li><i>OUT</i> - Other Location</li> </ul>")] = Query(None, description="&lt;p&gt;Members:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;&lt;i&gt;NOI&lt;/i&gt; - NOI Techpark&lt;/li&gt; &lt;li&gt;&lt;i&gt;EC&lt;/i&gt; - Eurac&lt;/li&gt; &lt;li&gt;&lt;i&gt;VV&lt;/i&gt; - Virtual Village&lt;/li&gt; &lt;li&gt;&lt;i&gt;OUT&lt;/i&gt; - Other Location&lt;/li&gt; &lt;/ul&gt;", alias="eventlocation"),
    onlyactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for today.noi.bz.it should be returned")] = Query(None, description="&#39;true&#39; if only Events marked as Active for today.noi.bz.it should be returned", alias="onlyactive"),
    websiteactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for noi.bz.it should be returned")] = Query(None, description="&#39;true&#39; if only Events marked as Active for noi.bz.it should be returned", alias="websiteactive"),
    communityactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for Noi community should be returned")] = Query(None, description="&#39;true&#39; if only Events marked as Active for Noi community should be returned", alias="communityactive"),
    active: Annotated[Optional[StrictBool], Field(description="Active Events Filter (possible Values: 'true' only Active Events, 'false' only Disabled Events), (default:'true')")] = Query(True, description="Active Events Filter (possible Values: &#39;true&#39; only Active Events, &#39;false&#39; only Disabled Events), (default:&#39;true&#39;)", alias="active"),
    eventids: Annotated[Optional[StrictStr], Field(description="comma separated list of event ids")] = Query(None, description="comma separated list of event ids", alias="eventids"),
    webaddress: Annotated[Optional[StrictStr], Field(description="Searches the webaddress")] = Query(None, description="Searches the webaddress", alias="webaddress"),
    tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")] = Query(None, description="Filter on Tags. (Endpoint on v1/Tag) Syntax &#x3D;and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: &#39;null&#39;)", alias="tagfilter"),
    sortorder: Annotated[Optional[StrictStr], Field(description="ASC or DESC by StartDate")] = Query('ASC', description="ASC or DESC by StartDate", alias="sortorder"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, &#39;null&#39; disables Random Sorting, (default:null)", alias="seed"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")] = Query(None, description="Language filter (returns only data available in the selected Language, Separator &#39;,&#39; possible values: &#39;de,it,en,nl,sc,pl,fr,ru&#39;, &#39;null&#39;: Filter disabled)", alias="langfilter"),
    optimizedates: Annotated[Optional[StrictBool], Field(description="Optimizes dates, cuts out all Rooms with Comment \"x\", revisits and corrects start + enddate")] = Query(False, description="Optimizes dates, cuts out all Rooms with Comment \&quot;x\&quot;, revisits and corrects start + enddate", alias="optimizedates"),
    latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Latitude Format: &#39;46.624975&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="latitude"),
    longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Longitude Format: &#39;11.369909&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="longitude"),
    radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="radius"),
    polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: &#39;Bounding Box Contains&#39;, &#39;bbi&#39;: &#39;Bounding Box Intersects&#39;, followed by a List of Comma Separated Longitude Latitude Tuples, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="polygon"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    lastchange: Optional[StrictStr] = Query(None, description="", alias="lastchange"),
    publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")] = Query(None, description="Published On Filter (Separator &#39;,&#39; List of publisher IDs), (default:&#39;null&#39;)", alias="publishedon"),
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
) -> EventShortResult:
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().v1_event_short_get(pagenumber, pagesize, startdate, enddate, datetimeformat, source, eventlocation, onlyactive, websiteactive, communityactive, active, eventids, webaddress, tagfilter, sortorder, seed, language, langfilter, optimizedates, latitude, longitude, radius, polygon, fields, lastchange, publishedon, searchfilter, rawfilter, rawsort, removenullvalues, getasidarray)


@router.post(
    "/v1/EventShort",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    response_model_by_alias=True,
)
async def v1_event_short_post(
    event_short_linked: Optional[EventShortLinked] = Body(None, description=""),
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
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().v1_event_short_post(event_short_linked)


@router.get(
    "/v1/EventShort/Detail/{id}",
    responses={
        200: {"model": EventShort, "description": "Object created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    summary="GET EventShort Single",
    response_model_by_alias=True,
)
async def v1_event_short_detail_id_get(
    id: Annotated[StrictStr, Field(description="Id of the Event")] = Path(..., description="Id of the Event"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    optimizedates: Annotated[Optional[StrictBool], Field(description="Optimizes dates, cuts out all Rooms with Comment \"x\", revisits and corrects start + enddate")] = Query(False, description="Optimizes dates, cuts out all Rooms with Comment \&quot;x\&quot;, revisits and corrects start + enddate", alias="optimizedates"),
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
) -> EventShort:
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().v1_event_short_detail_id_get(id, language, optimizedates, fields, removenullvalues)


@router.get(
    "/v1/EventShort/{id}",
    responses={
        200: {"model": EventShort, "description": "Object created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    summary="GET EventShort Single",
    response_model_by_alias=True,
)
async def single_event_short(
    id: Annotated[StrictStr, Field(description="Id of the Event")] = Path(..., description="Id of the Event"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    optimizedates: Annotated[Optional[StrictBool], Field(description="Optimizes dates, cuts out all Rooms with Comment \"x\", revisits and corrects start + enddate")] = Query(False, description="Optimizes dates, cuts out all Rooms with Comment \&quot;x\&quot;, revisits and corrects start + enddate", alias="optimizedates"),
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
) -> EventShort:
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().single_event_short(id, language, optimizedates, fields, removenullvalues)


@router.put(
    "/v1/EventShort/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    response_model_by_alias=True,
)
async def v1_event_short_id_put(
    id: StrictStr = Path(..., description=""),
    event_short_linked: Optional[EventShortLinked] = Body(None, description=""),
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
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().v1_event_short_id_put(id, event_short_linked)


@router.delete(
    "/v1/EventShort/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    response_model_by_alias=True,
)
async def v1_event_short_id_delete(
    id: StrictStr = Path(..., description=""),
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
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().v1_event_short_id_delete(id)


@router.get(
    "/v1/EventShort/GetbyRoomBooked",
    responses={
        200: {"model": List[EventShortByRoom], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    summary="GET EventShort List by Room Occupation",
    response_model_by_alias=True,
)
async def v1_event_short_getby_room_booked_get(
    startdate: Annotated[Optional[StrictStr], Field(description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp")] = Query(None, description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp", alias="startdate"),
    enddate: Annotated[Optional[StrictStr], Field(description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp")] = Query(None, description="Format (yyyy-MM-dd HH:mm) default or Unix Timestamp", alias="enddate"),
    datetimeformat: Annotated[Optional[StrictStr], Field(description="not provided, use default format, for unix timestamp pass \"uxtimestamp\"")] = Query(None, description="not provided, use default format, for unix timestamp pass \&quot;uxtimestamp\&quot;", alias="datetimeformat"),
    source: Annotated[Optional[StrictStr], Field(description="Source of the data, (possible values 'Content' or 'EBMS')")] = Query(None, description="Source of the data, (possible values &#39;Content&#39; or &#39;EBMS&#39;)", alias="source"),
    eventlocation: Annotated[Optional[StrictStr], Field(description="<p>Members:</p><ul><li><i>NOI</i> - NOI Techpark</li> <li><i>EC</i> - Eurac</li> <li><i>VV</i> - Virtual Village</li> <li><i>OUT</i> - Other Location</li> </ul>")] = Query(None, description="&lt;p&gt;Members:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;&lt;i&gt;NOI&lt;/i&gt; - NOI Techpark&lt;/li&gt; &lt;li&gt;&lt;i&gt;EC&lt;/i&gt; - Eurac&lt;/li&gt; &lt;li&gt;&lt;i&gt;VV&lt;/i&gt; - Virtual Village&lt;/li&gt; &lt;li&gt;&lt;i&gt;OUT&lt;/i&gt; - Other Location&lt;/li&gt; &lt;/ul&gt;", alias="eventlocation"),
    onlyactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for today.noi.bz.it should be returned")] = Query(None, description="&#39;true&#39; if only Events marked as Active for today.noi.bz.it should be returned", alias="onlyactive"),
    websiteactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for noi.bz.it should be returned")] = Query(None, description="&#39;true&#39; if only Events marked as Active for noi.bz.it should be returned", alias="websiteactive"),
    communityactive: Annotated[Optional[StrictBool], Field(description="'true' if only Events marked as Active for Noi community should be returned")] = Query(None, description="&#39;true&#39; if only Events marked as Active for Noi community should be returned", alias="communityactive"),
    active: Annotated[Optional[StrictBool], Field(description="Active Events Filter (possible Values: 'true' only Active Events, 'false' only Disabled Events), (default:'true')")] = Query(True, description="Active Events Filter (possible Values: &#39;true&#39; only Active Events, &#39;false&#39; only Disabled Events), (default:&#39;true&#39;)", alias="active"),
    tagfilter: Optional[StrictStr] = Query(None, description="", alias="tagfilter"),
    eventids: Annotated[Optional[StrictStr], Field(description="comma separated list of event ids")] = Query(None, description="comma separated list of event ids", alias="eventids"),
    webaddress: Annotated[Optional[StrictStr], Field(description="Filter by WebAddress Field")] = Query(None, description="Filter by WebAddress Field", alias="webaddress"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    langfilter: Annotated[Optional[StrictStr], Field(description="Language filter (returns only data available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")] = Query(None, description="Language filter (returns only data available in the selected Language, Separator &#39;,&#39; possible values: &#39;de,it,en,nl,sc,pl,fr,ru&#39;, &#39;null&#39;: Filter disabled)", alias="langfilter"),
    lastchange: Optional[StrictStr] = Query(None, description="", alias="lastchange"),
    updatefrom: Optional[StrictStr] = Query(None, description="", alias="updatefrom"),
    publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")] = Query(None, description="Published On Filter (Separator &#39;,&#39; List of publisher IDs), (default:&#39;null&#39;)", alias="publishedon"),
    eventgrouping: Annotated[Optional[StrictBool], Field(description="Groups Events with the Same Date/Id/Name and adds all Rooms to the SpaceDesc List")] = Query(True, description="Groups Events with the Same Date/Id/Name and adds all Rooms to the SpaceDesc List", alias="eventgrouping"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
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
) -> List[EventShortByRoom]:
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().v1_event_short_getby_room_booked_get(startdate, enddate, datetimeformat, source, eventlocation, onlyactive, websiteactive, communityactive, active, tagfilter, eventids, webaddress, language, langfilter, lastchange, updatefrom, publishedon, eventgrouping, fields, searchfilter, rawfilter, rawsort, removenullvalues)


@router.get(
    "/v1/EventShortTypes",
    responses={
        200: {"model": List[EventShortTypes], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    summary="GET EventShort Types",
    response_model_by_alias=True,
)
async def v1_event_short_types_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    idlist: Optional[StrictStr] = Query(None, description="", alias="idlist"),
    seed: Optional[StrictStr] = Query(None, description="", alias="seed"),
    type: Annotated[Optional[StrictStr], Field(description="Type to filter for ('TechnologyFields','CustomTagging')")] = Query(None, description="Type to filter for (&#39;TechnologyFields&#39;,&#39;CustomTagging&#39;)", alias="type"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
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
) -> List[EventShortTypes]:
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().v1_event_short_types_get(language, pagenumber, pagesize, idlist, seed, type, fields, searchfilter, rawfilter, rawsort, removenullvalues)


@router.get(
    "/v1/EventShortTypes/{id}",
    responses={
        200: {"model": EventShortTypes, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["EventShort"],
    summary="GET EventShort Type Single",
    response_model_by_alias=True,
)
async def single_event_short_types(
    id: Annotated[StrictStr, Field(description="ID of the EventShort Type")] = Path(..., description="ID of the EventShort Type"),
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
) -> EventShortTypes:
    if not BaseEventShortApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventShortApi.subclasses[0]().single_event_short_types(id, language, fields, removenullvalues)
