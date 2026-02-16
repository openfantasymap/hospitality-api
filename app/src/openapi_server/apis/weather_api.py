# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.weather_api_base import BaseWeatherApi
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
from openapi_server.models.bezirks_weather import BezirksWeather
from openapi_server.models.measuringpoint_v2 import MeasuringpointV2
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.snow_report_base_data import SnowReportBaseData
from openapi_server.models.weather import Weather
from openapi_server.models.weather_forecast_linked import WeatherForecastLinked
from openapi_server.models.weather_history import WeatherHistory
from openapi_server.models.weather_real_time import WeatherRealTime
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/Weather",
    responses={
        200: {"model": Weather, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Current Suedtirol Weather LIVE",
    response_model_by_alias=True,
)
async def v1_weather_get(
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="language"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (possible values: filter by StationData 1 = Schlanders, 2 = Meran, 3 = Bozen, 4 = Sterzing, 5 = Brixen, 6 = Bruneck | filter nearest Station to Region,TV,Municipality,Fraction reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), '' = No Filter). IF a Locfilter is set, only Stationdata is provided.")] = Query(None, description="Locfilter (possible values: filter by StationData 1 &#x3D; Schlanders, 2 &#x3D; Meran, 3 &#x3D; Bozen, 4 &#x3D; Sterzing, 5 &#x3D; Brixen, 6 &#x3D; Bruneck | filter nearest Station to Region,TV,Municipality,Fraction reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;&#39; &#x3D; No Filter). IF a Locfilter is set, only Stationdata is provided.", alias="locfilter"),
    extended: Optional[StrictBool] = Query(True, description="", alias="extended"),
    source: Optional[StrictStr] = Query(None, description="", alias="source"),
    fields: Optional[List[StrictStr]] = Query(None, description="", alias="fields"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> Weather:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().v1_weather_get(pagenumber, pagesize, language, locfilter, extended, source, fields)


@router.get(
    "/v1/Weather/{id}",
    responses={
        200: {"model": Weather, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Current Suedtirol Weather LIVE Single",
    response_model_by_alias=True,
)
async def single_weather(
    id: Annotated[StrictStr, Field(description="ID")] = Path(..., description="ID"),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="language"),
    source: Optional[StrictStr] = Query(None, description="", alias="source"),
    fields: Optional[List[StrictStr]] = Query(None, description="", alias="fields"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> Weather:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().single_weather(id, language, source, fields)


@router.get(
    "/v1/WeatherHistory",
    responses={
        200: {"model": WeatherHistory, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Suedtirol Weather HISTORY",
    response_model_by_alias=True,
)
async def v1_weather_history_get(
    pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")] = Query(1, description="Pagenumber", alias="pagenumber"),
    pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")] = Query(None, description="Elements per Page, (default:10)", alias="pagesize"),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query(None, description="Language", alias="language"),
    idlist: Optional[StrictStr] = Query(None, description="", alias="idlist"),
    locfilter: Optional[StrictStr] = Query(None, description="", alias="locfilter"),
    datefrom: Optional[StrictStr] = Query(None, description="", alias="datefrom"),
    dateto: Optional[StrictStr] = Query(None, description="", alias="dateto"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, &#39;null&#39; disables Random Sorting, (default:null)", alias="seed"),
    latitude: Optional[StrictStr] = Query(None, description="", alias="latitude"),
    longitude: Optional[StrictStr] = Query(None, description="", alias="longitude"),
    radius: Optional[StrictStr] = Query(None, description="", alias="radius"),
    polygon: Optional[StrictStr] = Query(None, description="", alias="polygon"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null)<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")] = Query(None, description="String to search for, Title in all languages are searched, (default: null)&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki searchfilter&lt;/a&gt;", alias="searchfilter"),
    lastchange: Optional[StrictStr] = Query(None, description="", alias="lastchange"),
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
) -> WeatherHistory:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().v1_weather_history_get(pagenumber, pagesize, language, idlist, locfilter, datefrom, dateto, seed, latitude, longitude, radius, polygon, fields, searchfilter, lastchange, rawfilter, rawsort, removenullvalues, getasidarray)


@router.get(
    "/v1/WeatherHistory/{id}",
    responses={
        200: {"model": WeatherHistory, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Suedtirol Weather HISTORY SINGLE",
    response_model_by_alias=True,
)
async def single_weather_history(
    id: Annotated[StrictStr, Field(description="ID")] = Path(..., description="ID"),
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
) -> WeatherHistory:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().single_weather_history(id, language, fields, removenullvalues)


@router.get(
    "/v1/Weather/District",
    responses={
        200: {"model": BezirksWeather, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET District Weather LIVE",
    response_model_by_alias=True,
)
async def v1_weather_district_get(
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (possible values: filter by District 1 = Etschtal/Überetsch/Unterland, 2 = Burggrafenamt, 3 = Vinschgau, 4 = Eisacktal und Sarntal, 5 = Wipptal, 6 = Pustertal/Dolomiten, 7 = Ladinien-Dolomiten | filter nearest DistrictWeather to Region,TV,Municipality,Fraction reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction))")] = Query(None, description="Locfilter (possible values: filter by District 1 &#x3D; Etschtal/Überetsch/Unterland, 2 &#x3D; Burggrafenamt, 3 &#x3D; Vinschgau, 4 &#x3D; Eisacktal und Sarntal, 5 &#x3D; Wipptal, 6 &#x3D; Pustertal/Dolomiten, 7 &#x3D; Ladinien-Dolomiten | filter nearest DistrictWeather to Region,TV,Municipality,Fraction reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction))", alias="locfilter"),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="language"),
    source: Optional[StrictStr] = Query(None, description="", alias="source"),
    fields: Optional[List[StrictStr]] = Query(None, description="", alias="fields"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> BezirksWeather:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().v1_weather_district_get(pagenumber, pagesize, locfilter, language, source, fields)


@router.get(
    "/v1/Weather/District/{id}",
    responses={
        200: {"model": BezirksWeather, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET District Weather LIVE SINGLE",
    response_model_by_alias=True,
)
async def single_weather_district(
    id: Annotated[StrictStr, Field(description="ID")] = Path(..., description="ID"),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="language"),
    source: Optional[StrictStr] = Query(None, description="", alias="source"),
    fields: Optional[List[StrictStr]] = Query(None, description="", alias="fields"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> BezirksWeather:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().single_weather_district(id, language, source, fields)


@router.get(
    "/v1/Weather/Realtime",
    responses={
        200: {"model": List[WeatherRealTime], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Current Realtime Weather LIVE",
    response_model_by_alias=True,
)
async def v1_weather_realtime_get(
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="language"),
    latitude: Optional[StrictStr] = Query(None, description="", alias="latitude"),
    longitude: Optional[StrictStr] = Query(None, description="", alias="longitude"),
    radius: Optional[StrictStr] = Query(None, description="", alias="radius"),
    fields: Optional[List[StrictStr]] = Query(None, description="", alias="fields"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[WeatherRealTime]:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().v1_weather_realtime_get(pagenumber, pagesize, language, latitude, longitude, radius, fields)


@router.get(
    "/v1/Weather/Realtime/{id}",
    responses={
        200: {"model": List[WeatherRealTime], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Current Realtime Weather LIVE Single",
    response_model_by_alias=True,
)
async def single_weather_realtime(
    id: Annotated[StrictStr, Field(description="id")] = Path(..., description="id"),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="language"),
    fields: Optional[List[StrictStr]] = Query(None, description="", alias="fields"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[WeatherRealTime]:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().single_weather_realtime(id, language, fields)


@router.get(
    "/v1/Weather/Forecast",
    responses={
        200: {"model": List[WeatherForecastLinked], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Weather Forecast",
    response_model_by_alias=True,
)
async def v1_weather_forecast_get(
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (possible values: filter on reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction))")] = Query(None, description="Locfilter (possible values: filter on reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction))", alias="locfilter"),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="language"),
    fields: Optional[List[StrictStr]] = Query(None, description="", alias="fields"),
    latitude: Optional[StrictStr] = Query(None, description="", alias="latitude"),
    longitude: Optional[StrictStr] = Query(None, description="", alias="longitude"),
    radius: Optional[StrictStr] = Query(None, description="", alias="radius"),
    polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: &#39;Bounding Box Contains&#39;, &#39;bbi&#39;: &#39;Bounding Box Intersects&#39;, followed by a List of Comma Separated Longitude Latitude Tuples, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="polygon"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> List[WeatherForecastLinked]:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().v1_weather_forecast_get(pagenumber, pagesize, locfilter, language, fields, latitude, longitude, radius, polygon)


@router.get(
    "/v1/Weather/Forecast/{id}",
    responses={
        200: {"model": WeatherForecastLinked, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Weather Forecast Single",
    response_model_by_alias=True,
)
async def single_weather_forecast(
    id: StrictStr = Path(..., description=""),
    language: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="language"),
    fields: Optional[List[StrictStr]] = Query(None, description="", alias="fields"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> WeatherForecastLinked:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().single_weather_forecast(id, language, fields)


@router.get(
    "/v1/Weather/Measuringpoint",
    responses={
        200: {"model": List[MeasuringpointV2], "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Measuringpoint LIST",
    response_model_by_alias=True,
)
async def v1_weather_measuringpoint_get(
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of Gastronomy IDs), (default:'null')")] = Query(None, description="IDFilter (Separator &#39;,&#39; List of Gastronomy IDs), (default:&#39;null&#39;)", alias="idlist"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null')")] = Query(None, description="Locfilter (Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;)", alias="locfilter"),
    tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")] = Query(None, description="Filter on Tags. (Endpoint on v1/Tag) Syntax &#x3D;and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: &#39;null&#39;)", alias="tagfilter"),
    areafilter: Annotated[Optional[StrictStr], Field(description="Area ID (multiple IDs possible, separated by \",\")")] = Query(None, description="Area ID (multiple IDs possible, separated by \&quot;,\&quot;)", alias="areafilter"),
    skiareafilter: Annotated[Optional[StrictStr], Field(description="Skiarea ID")] = Query(None, description="Skiarea ID", alias="skiareafilter"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    source: Optional[StrictStr] = Query(None, description="", alias="source"),
    active: Annotated[Optional[StrictBool], Field(description="Active Filter (possible Values: 'true' only Active Measuringpoints, 'false' only Disabled Measuringpoints), (default:'null')")] = Query(None, description="Active Filter (possible Values: &#39;true&#39; only Active Measuringpoints, &#39;false&#39; only Disabled Measuringpoints), (default:&#39;null&#39;)", alias="active"),
    publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")] = Query(None, description="Published On Filter (Separator &#39;,&#39; List of publisher IDs), (default:&#39;null&#39;)", alias="publishedon"),
    updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")] = Query(None, description="Returns data changed after this date Format (yyyy-MM-dd), (default: &#39;null&#39;)", alias="updatefrom"),
    latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Latitude Format: &#39;46.624975&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="latitude"),
    longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Longitude Format: &#39;11.369909&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="longitude"),
    radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="radius"),
    polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: &#39;Bounding Box Contains&#39;, &#39;bbi&#39;: &#39;Bounding Box Intersects&#39;, followed by a List of Comma Separated Longitude Latitude Tuples, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="polygon"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, not provided disables Random Sorting, (default:'null')")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, not provided disables Random Sorting, (default:&#39;null&#39;)", alias="seed"),
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
) -> List[MeasuringpointV2]:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().v1_weather_measuringpoint_get(pagenumber, pagesize, idlist, locfilter, tagfilter, areafilter, skiareafilter, language, source, active, publishedon, updatefrom, latitude, longitude, radius, polygon, seed, fields, searchfilter, rawfilter, rawsort, removenullvalues, getasidarray)


@router.get(
    "/v1/Weather/Measuringpoint/{id}",
    responses={
        200: {"model": MeasuringpointV2, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Measuringpoint SINGLE",
    response_model_by_alias=True,
)
async def single_weather_measuringpoint(
    id: Annotated[StrictStr, Field(description="Measuringpoint ID")] = Path(..., description="Measuringpoint ID"),
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
) -> MeasuringpointV2:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().single_weather_measuringpoint(id, language, fields, removenullvalues)


@router.get(
    "/v1/Weather/SnowReport",
    responses={
        200: {"model": SnowReportBaseData, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Snowreport Data LIVE",
    response_model_by_alias=True,
)
async def v1_weather_snow_report_get(
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    skiareaid: Annotated[Optional[StrictStr], Field(description="Skiarea ID")] = Query(None, description="Skiarea ID", alias="skiareaid"),
    lang: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="lang"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> SnowReportBaseData:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().v1_weather_snow_report_get(pagenumber, pagesize, skiareaid, lang)


@router.get(
    "/v1/Weather/SnowReport/{id}",
    responses={
        200: {"model": SnowReportBaseData, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Weather"],
    summary="GET Snowreport Data LIVE Single",
    response_model_by_alias=True,
)
async def single_weather_snow_report(
    id: Annotated[StrictStr, Field(description="Skiarea ID")] = Path(..., description="Skiarea ID"),
    lang: Annotated[Optional[StrictStr], Field(description="Language")] = Query('en', description="Language", alias="lang"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> SnowReportBaseData:
    if not BaseWeatherApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWeatherApi.subclasses[0]().single_weather_snow_report(id, lang)
