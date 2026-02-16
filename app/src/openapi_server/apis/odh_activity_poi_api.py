# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.odh_activity_poi_api_base import BaseODHActivityPoiApi
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
from openapi_server.models.odh_activity_poi_linked import ODHActivityPoiLinked
from openapi_server.models.odh_activity_poi_linked_json_result import ODHActivityPoiLinkedJsonResult
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.smg_poi_types import SmgPoiTypes
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/ODHActivityPoi",
    responses={
        200: {"model": ODHActivityPoiLinkedJsonResult, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["ODHActivityPoi"],
    summary="GET ODHActivityPoi List",
    response_model_by_alias=True,
)
async def get_odh_activity_poi_list(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")] = Query(1, description="Pagenumber", alias="pagenumber"),
    pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")] = Query(None, description="Elements per Page, (default:10)", alias="pagesize"),
    type: Annotated[Optional[StrictStr], Field(description="Type of the ODHActivityPoi ('null' = Filter disabled, possible values: BITMASK: 1 = Wellness, 2 = Winter, 4 = Summer, 8 = Culture, 16 = Other, 32 = Gastronomy, 64 = Mobility, 128 = Shops and services), (default: 255 == ALL), refers to <a href=\"https://tourism.opendatahub.com/v1/ODHActivityPoiTypes?rawfilter=eq(Type,%27Type%27)\" target=\"_blank\">ODHActivityPoi Types</a>, Type: Type")] = Query('255', description="Type of the ODHActivityPoi (&#39;null&#39; &#x3D; Filter disabled, possible values: BITMASK: 1 &#x3D; Wellness, 2 &#x3D; Winter, 4 &#x3D; Summer, 8 &#x3D; Culture, 16 &#x3D; Other, 32 &#x3D; Gastronomy, 64 &#x3D; Mobility, 128 &#x3D; Shops and services), (default: 255 &#x3D;&#x3D; ALL), refers to &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/ODHActivityPoiTypes?rawfilter&#x3D;eq(Type,%27Type%27)\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ODHActivityPoi Types&lt;/a&gt;, Type: Type", alias="type"),
    activitytype: Annotated[Optional[StrictStr], Field(description="Filtering by Activity Type defined by LTS ('null' = Filter disabled, possible values: BITMASK: 'Mountains = 1','Cycling = 2','Local tours = 4','Horses = 8','Hiking = 16','Running and fitness = 32','Cross-country ski-track = 64','Tobbogan run = 128','Slopes = 256','Lifts = 512'), (default:'1023' == ALL), , refers to <a href=\"https://tourism.opendatahub.com/v1/ActivityTypes?rawfilter=eq(Type,%27Type%27)\" target=\"_blank\">ActivityTypes</a>, Type: Type")] = Query(None, description="Filtering by Activity Type defined by LTS (&#39;null&#39; &#x3D; Filter disabled, possible values: BITMASK: &#39;Mountains &#x3D; 1&#39;,&#39;Cycling &#x3D; 2&#39;,&#39;Local tours &#x3D; 4&#39;,&#39;Horses &#x3D; 8&#39;,&#39;Hiking &#x3D; 16&#39;,&#39;Running and fitness &#x3D; 32&#39;,&#39;Cross-country ski-track &#x3D; 64&#39;,&#39;Tobbogan run &#x3D; 128&#39;,&#39;Slopes &#x3D; 256&#39;,&#39;Lifts &#x3D; 512&#39;), (default:&#39;1023&#39; &#x3D;&#x3D; ALL), , refers to &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/ActivityTypes?rawfilter&#x3D;eq(Type,%27Type%27)\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ActivityTypes&lt;/a&gt;, Type: Type", alias="activitytype"),
    poitype: Annotated[Optional[StrictStr], Field(description="Filtering by Poi Type defined by LTS ('null' = Filter disabled, possible values: BITMASK 'Doctors, Pharmacies = 1','Shops = 2','Culture and sights= 4','Nightlife and entertainment = 8','Public institutions = 16','Sports and leisure = 32','Traffic and transport = 64', 'Service providers' = 128, 'Craft' = 256, 'Associations' = 512, 'Companies' = 1024), (default:'2047' == ALL), , refers to <a href=\"https://tourism.opendatahub.com/v1/PoiTypes?rawfilter=eq(Type,%27Type%27)\" target=\"_blank\">PoiTypes</a>, Type: Type")] = Query(None, description="Filtering by Poi Type defined by LTS (&#39;null&#39; &#x3D; Filter disabled, possible values: BITMASK &#39;Doctors, Pharmacies &#x3D; 1&#39;,&#39;Shops &#x3D; 2&#39;,&#39;Culture and sights&#x3D; 4&#39;,&#39;Nightlife and entertainment &#x3D; 8&#39;,&#39;Public institutions &#x3D; 16&#39;,&#39;Sports and leisure &#x3D; 32&#39;,&#39;Traffic and transport &#x3D; 64&#39;, &#39;Service providers&#39; &#x3D; 128, &#39;Craft&#39; &#x3D; 256, &#39;Associations&#39; &#x3D; 512, &#39;Companies&#39; &#x3D; 1024), (default:&#39;2047&#39; &#x3D;&#x3D; ALL), , refers to &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/PoiTypes?rawfilter&#x3D;eq(Type,%27Type%27)\&quot; target&#x3D;\&quot;_blank\&quot;&gt;PoiTypes&lt;/a&gt;, Type: Type", alias="poitype"),
    subtype: Annotated[Optional[StrictStr], Field(description="Subtype of the ODHActivityPoi ('null' = Filter disabled, BITMASK Filter, available SubTypes depends on the selected Maintype) <a href=\"https://tourism.opendatahub.com/v1/ODHActivityPoiTypes?rawfilter=eq(Type,%27SubType%27)\" target=\"_blank\">ODHActivityPoi SubTypes</a>, or <a href=\"https://tourism.opendatahub.com/v1/ActivityTypes?rawfilter=eq(Type,%27SubType%27)\" target=\"_blank\">Activity SubTypes</a>, or <a href=\"https://tourism.opendatahub.com/v1/PoiTypes?rawfilter=eq(Type,%27SubType%27)\" target=\"_blank\">Poi SubTypes</a>, Type: SubType")] = Query(None, description="Subtype of the ODHActivityPoi (&#39;null&#39; &#x3D; Filter disabled, BITMASK Filter, available SubTypes depends on the selected Maintype) &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/ODHActivityPoiTypes?rawfilter&#x3D;eq(Type,%27SubType%27)\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ODHActivityPoi SubTypes&lt;/a&gt;, or &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/ActivityTypes?rawfilter&#x3D;eq(Type,%27SubType%27)\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Activity SubTypes&lt;/a&gt;, or &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/PoiTypes?rawfilter&#x3D;eq(Type,%27SubType%27)\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Poi SubTypes&lt;/a&gt;, Type: SubType", alias="subtype"),
    level3type: Annotated[Optional[StrictStr], Field(description="Additional Type of Level 3 the ODHActivityPoi ('null' = Filter disabled, BITMASK Filter, available SubTypes depends on the selected Maintype, SubType reference to ODHActivityPoiTypes)")] = Query(None, description="Additional Type of Level 3 the ODHActivityPoi (&#39;null&#39; &#x3D; Filter disabled, BITMASK Filter, available SubTypes depends on the selected Maintype, SubType reference to ODHActivityPoiTypes)", alias="level3type"),
    idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of ODHActivityPoi IDs), (default:'null')")] = Query(None, description="IDFilter (Separator &#39;,&#39; List of ODHActivityPoi IDs), (default:&#39;null&#39;)", alias="idlist"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")] = Query(None, description="Locfilter SPECIAL Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki locfilter&lt;/a&gt;", alias="locfilter"),
    langfilter: Annotated[Optional[StrictStr], Field(description="ODHActivityPoi Langfilter (returns only SmgPois available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")] = Query(None, description="ODHActivityPoi Langfilter (returns only SmgPois available in the selected Language, Separator &#39;,&#39; possible values: &#39;de,it,en,nl,sc,pl,fr,ru&#39;, &#39;null&#39;: Filter disabled)", alias="langfilter"),
    areafilter: Annotated[Optional[StrictStr], Field(description="AreaFilter (Alternate Locfilter, can be combined with locfilter) (Separator ',' possible values: reg + REGIONID = (Filter by Region), tvs + TOURISMASSOCIATIONID = (Filter by Tourismassociation), skr + SKIREGIONID = (Filter by Skiregion), ska + SKIAREAID = (Filter by Skiarea), are + AREAID = (Filter by LTS Area), 'null' = No Filter), (default:'null')")] = Query(None, description="AreaFilter (Alternate Locfilter, can be combined with locfilter) (Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMASSOCIATIONID &#x3D; (Filter by Tourismassociation), skr + SKIREGIONID &#x3D; (Filter by Skiregion), ska + SKIAREAID &#x3D; (Filter by Skiarea), are + AREAID &#x3D; (Filter by LTS Area), &#39;null&#39; &#x3D; No Filter), (default:&#39;null&#39;)", alias="areafilter"),
    highlight: Annotated[Optional[StrictBool], Field(description="Hightlight Filter (possible values: 'false' = only ODHActivityPoi with Highlight false, 'true' = only ODHActivityPoi with Highlight true), (default:'null')")] = Query(None, description="Hightlight Filter (possible values: &#39;false&#39; &#x3D; only ODHActivityPoi with Highlight false, &#39;true&#39; &#x3D; only ODHActivityPoi with Highlight true), (default:&#39;null&#39;)", alias="highlight"),
    source: Annotated[Optional[StrictStr], Field(description="Source Filter (possible Values: 'null' Displays all ODHActivityPoi, 'None', 'ActivityData', 'PoiData', 'GastronomicData', 'MuseumData', 'Magnolia', 'Content', 'SuedtirolWein', 'ArchApp'), (default:'null')")] = Query(None, description="Source Filter (possible Values: &#39;null&#39; Displays all ODHActivityPoi, &#39;None&#39;, &#39;ActivityData&#39;, &#39;PoiData&#39;, &#39;GastronomicData&#39;, &#39;MuseumData&#39;, &#39;Magnolia&#39;, &#39;Content&#39;, &#39;SuedtirolWein&#39;, &#39;ArchApp&#39;), (default:&#39;null&#39;)", alias="source"),
    odhtagfilter: Annotated[Optional[StrictStr], Field(description="ODH Taglist Filter (refers to Array SmgTags) (String, Separator ',' more Tags possible (OR FILTER), available Tags reference to 'v1/ODHTag?validforentity=odhactivitypoi'), (default:'null')")] = Query(None, description="ODH Taglist Filter (refers to Array SmgTags) (String, Separator &#39;,&#39; more Tags possible (OR FILTER), available Tags reference to &#39;v1/ODHTag?validforentity&#x3D;odhactivitypoi&#39;), (default:&#39;null&#39;)", alias="odhtagfilter"),
    odhtagfilter_and: Annotated[Optional[StrictStr], Field(description="ODH Taglist Filter (refers to Array SmgTags) (String, Separator ',' more Tags possible (AND FILTER), available Tags reference to 'v1/ODHTag?validforentity=odhactivitypoi'), (default:'null')")] = Query(None, description="ODH Taglist Filter (refers to Array SmgTags) (String, Separator &#39;,&#39; more Tags possible (AND FILTER), available Tags reference to &#39;v1/ODHTag?validforentity&#x3D;odhactivitypoi&#39;), (default:&#39;null&#39;)", alias="odhtagfilter_and"),
    odhactive: Annotated[Optional[StrictBool], Field(description="ODH Active (Published) ODHActivityPoi Filter (Refers to field OdhActive) (possible Values: 'true' only published ODHActivityPoi, 'false' only not published ODHActivityPoi), (default:'null')")] = Query(None, description="ODH Active (Published) ODHActivityPoi Filter (Refers to field OdhActive) (possible Values: &#39;true&#39; only published ODHActivityPoi, &#39;false&#39; only not published ODHActivityPoi), (default:&#39;null&#39;)", alias="odhactive"),
    active: Annotated[Optional[StrictBool], Field(description="Active ODHActivityPoi Filter (possible Values: 'true' only active ODHActivityPoi, 'false' only not active ODHActivityPoi), (default:'null')")] = Query(None, description="Active ODHActivityPoi Filter (possible Values: &#39;true&#39; only active ODHActivityPoi, &#39;false&#39; only not active ODHActivityPoi), (default:&#39;null&#39;)", alias="active"),
    categorycodefilter: Annotated[Optional[StrictStr], Field(description="CategoryCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes?rawfilter=eq(Type,\\\"CategoryCodes\\\")\" target=\"_blank\">GastronomyTypes</a>, Type: CategoryCodes")] = Query(None, description="CategoryCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/GastronomyTypes?rawfilter&#x3D;eq(Type,\\\&quot;CategoryCodes\\\&quot;)\&quot; target&#x3D;\&quot;_blank\&quot;&gt;GastronomyTypes&lt;/a&gt;, Type: CategoryCodes", alias="categorycodefilter"),
    dishcodefilter: Annotated[Optional[StrictStr], Field(description="DishCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes\" target=\"_blank\">GastronomyTypes</a>, Type: DishCodes")] = Query(None, description="DishCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/GastronomyTypes\&quot; target&#x3D;\&quot;_blank\&quot;&gt;GastronomyTypes&lt;/a&gt;, Type: DishCodes", alias="dishcodefilter"),
    ceremonycodefilter: Annotated[Optional[StrictStr], Field(description="CeremonyCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes\" target=\"_blank\">GastronomyTypes</a>, Type: CeremonyCodes")] = Query(None, description="CeremonyCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/GastronomyTypes\&quot; target&#x3D;\&quot;_blank\&quot;&gt;GastronomyTypes&lt;/a&gt;, Type: CeremonyCodes", alias="ceremonycodefilter"),
    facilitycodefilter: Annotated[Optional[StrictStr], Field(description="FacilityCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes\" target=\"_blank\">GastronomyTypes</a>, Type: with FacilityCodes_ prefix")] = Query(None, description="FacilityCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/GastronomyTypes\&quot; target&#x3D;\&quot;_blank\&quot;&gt;GastronomyTypes&lt;/a&gt;, Type: with FacilityCodes_ prefix", alias="facilitycodefilter"),
    cuisinecodefilter: Annotated[Optional[StrictStr], Field(description="CuisineCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes\" target=\"_blank\">GastronomyTypes</a>, Type: CuisineCodes")] = Query(None, description="CuisineCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to &lt;a href&#x3D;\&quot;https://tourism.opendatahub.com/v1/GastronomyTypes\&quot; target&#x3D;\&quot;_blank\&quot;&gt;GastronomyTypes&lt;/a&gt;, Type: CuisineCodes", alias="cuisinecodefilter"),
    difficultyfilter: Annotated[Optional[StrictStr], Field(description="Difficulty Filter (possible values: '1' = easy, '2' = medium, '3' = difficult), (default:'null')")] = Query(None, description="Difficulty Filter (possible values: &#39;1&#39; &#x3D; easy, &#39;2&#39; &#x3D; medium, &#39;3&#39; &#x3D; difficult), (default:&#39;null&#39;)", alias="difficultyfilter"),
    distancefilter: Annotated[Optional[StrictStr], Field(description="Distance Range Filter (Separator ',' example Value: 15,40 Distance from 15 up to 40 Km), (default:'null')")] = Query(None, description="Distance Range Filter (Separator &#39;,&#39; example Value: 15,40 Distance from 15 up to 40 Km), (default:&#39;null&#39;)", alias="distancefilter"),
    altitudefilter: Annotated[Optional[StrictStr], Field(description="Altitude Range Filter (Separator ',' example Value: 500,1000 Altitude from 500 up to 1000 metres), (default:'null')")] = Query(None, description="Altitude Range Filter (Separator &#39;,&#39; example Value: 500,1000 Altitude from 500 up to 1000 metres), (default:&#39;null&#39;)", alias="altitudefilter"),
    durationfilter: Annotated[Optional[StrictStr], Field(description="Duration Range Filter (Separator ',' example Value: 1,3 Duration from 1 to 3 hours), (default:'null')")] = Query(None, description="Duration Range Filter (Separator &#39;,&#39; example Value: 1,3 Duration from 1 to 3 hours), (default:&#39;null&#39;)", alias="durationfilter"),
    hasimage: Optional[StrictBool] = Query(None, description="", alias="hasimage"),
    tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")] = Query(None, description="Filter on Tags. (Endpoint on v1/Tag) Syntax &#x3D;and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: &#39;null&#39;)", alias="tagfilter"),
    publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")] = Query(None, description="Published On Filter (Separator &#39;,&#39; List of publisher IDs), (default:&#39;null&#39;)", alias="publishedon"),
    updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")] = Query(None, description="Returns data changed after this date Format (yyyy-MM-dd), (default: &#39;null&#39;)", alias="updatefrom"),
    seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, not provided disables Random Sorting, (default:'null')")] = Query(None, description="Seed &#39;1 - 10&#39; for Random Sorting, &#39;0&#39; generates a Random Seed, not provided disables Random Sorting, (default:&#39;null&#39;)", alias="seed"),
    latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Latitude Format: &#39;46.624975&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="latitude"),
    longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="GeoFilter FLOAT Longitude Format: &#39;11.369909&#39;, &#39;null&#39; &#x3D; disabled, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="longitude"),
    radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")] = Query(None, description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki geosort&lt;/a&gt;", alias="radius"),
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
) -> ODHActivityPoiLinkedJsonResult:
    if not BaseODHActivityPoiApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseODHActivityPoiApi.subclasses[0]().get_odh_activity_poi_list(language, pagenumber, pagesize, type, activitytype, poitype, subtype, level3type, idlist, locfilter, langfilter, areafilter, highlight, source, odhtagfilter, odhtagfilter_and, odhactive, active, categorycodefilter, dishcodefilter, ceremonycodefilter, facilitycodefilter, cuisinecodefilter, difficultyfilter, distancefilter, altitudefilter, durationfilter, hasimage, tagfilter, publishedon, updatefrom, seed, latitude, longitude, radius, polygon, fields, searchfilter, rawfilter, rawsort, removenullvalues, getasidarray)


@router.post(
    "/v1/ODHActivityPoi",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["ODHActivityPoi"],
    summary="POST Insert new ODHActivityPoi",
    response_model_by_alias=True,
)
async def v1_odh_activity_poi_post(
    odh_activity_poi_linked: Annotated[Optional[ODHActivityPoiLinked], Field(description="ODHActivityPoi Object")] = Body(None, description="ODHActivityPoi Object"),
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
    if not BaseODHActivityPoiApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseODHActivityPoiApi.subclasses[0]().v1_odh_activity_poi_post(odh_activity_poi_linked)


@router.get(
    "/v1/ODHActivityPoi/{id}",
    responses={
        200: {"model": ODHActivityPoiLinked, "description": "Object created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["ODHActivityPoi"],
    summary="GET ODHActivityPoi Single",
    response_model_by_alias=True,
)
async def single_odh_activity_poi(
    id: Annotated[StrictStr, Field(description="ID of the Poi")] = Path(..., description="ID of the Poi"),
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
) -> ODHActivityPoiLinked:
    if not BaseODHActivityPoiApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseODHActivityPoiApi.subclasses[0]().single_odh_activity_poi(id, language, fields, removenullvalues)


@router.put(
    "/v1/ODHActivityPoi/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["ODHActivityPoi"],
    summary="PUT Modify existing ODHActivityPoi",
    response_model_by_alias=True,
)
async def v1_odh_activity_poi_id_put(
    id: Annotated[StrictStr, Field(description="ODHActivityPoi Id")] = Path(..., description="ODHActivityPoi Id"),
    odh_activity_poi_linked: Annotated[Optional[ODHActivityPoiLinked], Field(description="ODHActivityPoi Object")] = Body(None, description="ODHActivityPoi Object"),
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
    if not BaseODHActivityPoiApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseODHActivityPoiApi.subclasses[0]().v1_odh_activity_poi_id_put(id, odh_activity_poi_linked)


@router.delete(
    "/v1/ODHActivityPoi/{id}",
    responses={
        200: {"model": PGCRUDResult, "description": "OK"},
        400: {"model": ProblemDetails, "description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
    tags=["ODHActivityPoi"],
    summary="DELETE ODHActivityPoi by Id",
    response_model_by_alias=True,
)
async def v1_odh_activity_poi_id_delete(
    id: Annotated[StrictStr, Field(description="ODHActivityPoi Id")] = Path(..., description="ODHActivityPoi Id"),
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
    if not BaseODHActivityPoiApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseODHActivityPoiApi.subclasses[0]().v1_odh_activity_poi_id_delete(id)


@router.get(
    "/v1/ODHActivityPoiTypes",
    responses={
        200: {"model": List[SmgPoiTypes], "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["ODHActivityPoi"],
    summary="GET ODHActivityPoi Types List",
    response_model_by_alias=True,
)
async def v1_odh_activity_poi_types_get(
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")] = Query(None, description="Language field selector, displays data and fields available in the selected language (default:&#39;null&#39; all languages are displayed)", alias="language"),
    pagenumber: Optional[StrictInt] = Query(None, description="", alias="pagenumber"),
    pagesize: Optional[StrictInt] = Query(None, description="", alias="pagesize"),
    idlist: Optional[StrictStr] = Query(None, description="", alias="idlist"),
    seed: Optional[StrictStr] = Query(None, description="", alias="seed"),
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
) -> List[SmgPoiTypes]:
    if not BaseODHActivityPoiApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseODHActivityPoiApi.subclasses[0]().v1_odh_activity_poi_types_get(language, pagenumber, pagesize, idlist, seed, fields, searchfilter, rawfilter, rawsort, removenullvalues)


@router.get(
    "/v1/ODHActivityPoiTypes/{id}",
    responses={
        200: {"model": SmgPoiTypes, "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["ODHActivityPoi"],
    summary="GET ODHActivityPoi Types Single",
    response_model_by_alias=True,
)
async def single_odh_activity_poi_types(
    id: Annotated[StrictStr, Field(description="ID of the ODHActivityPoi Type")] = Path(..., description="ID of the ODHActivityPoi Type"),
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
) -> SmgPoiTypes:
    if not BaseODHActivityPoiApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseODHActivityPoiApi.subclasses[0]().single_odh_activity_poi_types(id, language, fields, removenullvalues)
