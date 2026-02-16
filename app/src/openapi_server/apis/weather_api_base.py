# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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

class BaseWeatherApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseWeatherApi.subclasses = BaseWeatherApi.subclasses + (cls,)
    async def v1_weather_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (possible values: filter by StationData 1 = Schlanders, 2 = Meran, 3 = Bozen, 4 = Sterzing, 5 = Brixen, 6 = Bruneck | filter nearest Station to Region,TV,Municipality,Fraction reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), '' = No Filter). IF a Locfilter is set, only Stationdata is provided.")],
        extended: Optional[StrictBool],
        source: Optional[StrictStr],
        fields: Optional[List[StrictStr]],
    ) -> Weather:
        ...


    async def single_weather(
        self,
        id: Annotated[StrictStr, Field(description="ID")],
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        source: Optional[StrictStr],
        fields: Optional[List[StrictStr]],
    ) -> Weather:
        ...


    async def v1_weather_history_get(
        self,
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")],
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        idlist: Optional[StrictStr],
        locfilter: Optional[StrictStr],
        datefrom: Optional[StrictStr],
        dateto: Optional[StrictStr],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, 'null' disables Random Sorting, (default:null)")],
        latitude: Optional[StrictStr],
        longitude: Optional[StrictStr],
        radius: Optional[StrictStr],
        polygon: Optional[StrictStr],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null)<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        lastchange: Optional[StrictStr],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> WeatherHistory:
        ...


    async def single_weather_history(
        self,
        id: Annotated[StrictStr, Field(description="ID")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> WeatherHistory:
        ...


    async def v1_weather_district_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (possible values: filter by District 1 = Etschtal/Überetsch/Unterland, 2 = Burggrafenamt, 3 = Vinschgau, 4 = Eisacktal und Sarntal, 5 = Wipptal, 6 = Pustertal/Dolomiten, 7 = Ladinien-Dolomiten | filter nearest DistrictWeather to Region,TV,Municipality,Fraction reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction))")],
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        source: Optional[StrictStr],
        fields: Optional[List[StrictStr]],
    ) -> BezirksWeather:
        ...


    async def single_weather_district(
        self,
        id: Annotated[StrictStr, Field(description="ID")],
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        source: Optional[StrictStr],
        fields: Optional[List[StrictStr]],
    ) -> BezirksWeather:
        ...


    async def v1_weather_realtime_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        latitude: Optional[StrictStr],
        longitude: Optional[StrictStr],
        radius: Optional[StrictStr],
        fields: Optional[List[StrictStr]],
    ) -> List[WeatherRealTime]:
        ...


    async def single_weather_realtime(
        self,
        id: Annotated[StrictStr, Field(description="id")],
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        fields: Optional[List[StrictStr]],
    ) -> List[WeatherRealTime]:
        ...


    async def v1_weather_forecast_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (possible values: filter on reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction))")],
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        fields: Optional[List[StrictStr]],
        latitude: Optional[StrictStr],
        longitude: Optional[StrictStr],
        radius: Optional[StrictStr],
        polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")],
    ) -> List[WeatherForecastLinked]:
        ...


    async def single_weather_forecast(
        self,
        id: StrictStr,
        language: Annotated[Optional[StrictStr], Field(description="Language")],
        fields: Optional[List[StrictStr]],
    ) -> WeatherForecastLinked:
        ...


    async def v1_weather_measuringpoint_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of Gastronomy IDs), (default:'null')")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter (Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null')")],
        tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")],
        areafilter: Annotated[Optional[StrictStr], Field(description="Area ID (multiple IDs possible, separated by \",\")")],
        skiareafilter: Annotated[Optional[StrictStr], Field(description="Skiarea ID")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        source: Optional[StrictStr],
        active: Annotated[Optional[StrictBool], Field(description="Active Filter (possible Values: 'true' only Active Measuringpoints, 'false' only Disabled Measuringpoints), (default:'null')")],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki geosort</a>")],
        longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki geosort</a>")],
        radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki geosort</a>")],
        polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, not provided disables Random Sorting, (default:'null')")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[MeasuringpointV2]:
        ...


    async def single_weather_measuringpoint(
        self,
        id: Annotated[StrictStr, Field(description="Measuringpoint ID")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> MeasuringpointV2:
        ...


    async def v1_weather_snow_report_get(
        self,
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        skiareaid: Annotated[Optional[StrictStr], Field(description="Skiarea ID")],
        lang: Annotated[Optional[StrictStr], Field(description="Language")],
    ) -> SnowReportBaseData:
        ...


    async def single_weather_snow_report(
        self,
        id: Annotated[StrictStr, Field(description="Skiarea ID")],
        lang: Annotated[Optional[StrictStr], Field(description="Language")],
    ) -> SnowReportBaseData:
        ...
