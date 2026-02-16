# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.odh_activity_poi_linked import ODHActivityPoiLinked
from openapi_server.models.odh_activity_poi_linked_json_result import ODHActivityPoiLinkedJsonResult
from openapi_server.models.pgcrud_result import PGCRUDResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.smg_poi_types import SmgPoiTypes
from openapi_server.security_api import get_token_oauth2

class BaseODHActivityPoiApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseODHActivityPoiApi.subclasses = BaseODHActivityPoiApi.subclasses + (cls,)
    async def get_odh_activity_poi_list(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Annotated[Optional[StrictInt], Field(description="Pagenumber")],
        pagesize: Annotated[Optional[StrictInt], Field(description="Elements per Page, (default:10)")],
        type: Annotated[Optional[StrictStr], Field(description="Type of the ODHActivityPoi ('null' = Filter disabled, possible values: BITMASK: 1 = Wellness, 2 = Winter, 4 = Summer, 8 = Culture, 16 = Other, 32 = Gastronomy, 64 = Mobility, 128 = Shops and services), (default: 255 == ALL), refers to <a href=\"https://tourism.opendatahub.com/v1/ODHActivityPoiTypes?rawfilter=eq(Type,%27Type%27)\" target=\"_blank\">ODHActivityPoi Types</a>, Type: Type")],
        activitytype: Annotated[Optional[StrictStr], Field(description="Filtering by Activity Type defined by LTS ('null' = Filter disabled, possible values: BITMASK: 'Mountains = 1','Cycling = 2','Local tours = 4','Horses = 8','Hiking = 16','Running and fitness = 32','Cross-country ski-track = 64','Tobbogan run = 128','Slopes = 256','Lifts = 512'), (default:'1023' == ALL), , refers to <a href=\"https://tourism.opendatahub.com/v1/ActivityTypes?rawfilter=eq(Type,%27Type%27)\" target=\"_blank\">ActivityTypes</a>, Type: Type")],
        poitype: Annotated[Optional[StrictStr], Field(description="Filtering by Poi Type defined by LTS ('null' = Filter disabled, possible values: BITMASK 'Doctors, Pharmacies = 1','Shops = 2','Culture and sights= 4','Nightlife and entertainment = 8','Public institutions = 16','Sports and leisure = 32','Traffic and transport = 64', 'Service providers' = 128, 'Craft' = 256, 'Associations' = 512, 'Companies' = 1024), (default:'2047' == ALL), , refers to <a href=\"https://tourism.opendatahub.com/v1/PoiTypes?rawfilter=eq(Type,%27Type%27)\" target=\"_blank\">PoiTypes</a>, Type: Type")],
        subtype: Annotated[Optional[StrictStr], Field(description="Subtype of the ODHActivityPoi ('null' = Filter disabled, BITMASK Filter, available SubTypes depends on the selected Maintype) <a href=\"https://tourism.opendatahub.com/v1/ODHActivityPoiTypes?rawfilter=eq(Type,%27SubType%27)\" target=\"_blank\">ODHActivityPoi SubTypes</a>, or <a href=\"https://tourism.opendatahub.com/v1/ActivityTypes?rawfilter=eq(Type,%27SubType%27)\" target=\"_blank\">Activity SubTypes</a>, or <a href=\"https://tourism.opendatahub.com/v1/PoiTypes?rawfilter=eq(Type,%27SubType%27)\" target=\"_blank\">Poi SubTypes</a>, Type: SubType")],
        level3type: Annotated[Optional[StrictStr], Field(description="Additional Type of Level 3 the ODHActivityPoi ('null' = Filter disabled, BITMASK Filter, available SubTypes depends on the selected Maintype, SubType reference to ODHActivityPoiTypes)")],
        idlist: Annotated[Optional[StrictStr], Field(description="IDFilter (Separator ',' List of ODHActivityPoi IDs), (default:'null')")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")],
        langfilter: Annotated[Optional[StrictStr], Field(description="ODHActivityPoi Langfilter (returns only SmgPois available in the selected Language, Separator ',' possible values: 'de,it,en,nl,sc,pl,fr,ru', 'null': Filter disabled)")],
        areafilter: Annotated[Optional[StrictStr], Field(description="AreaFilter (Alternate Locfilter, can be combined with locfilter) (Separator ',' possible values: reg + REGIONID = (Filter by Region), tvs + TOURISMASSOCIATIONID = (Filter by Tourismassociation), skr + SKIREGIONID = (Filter by Skiregion), ska + SKIAREAID = (Filter by Skiarea), are + AREAID = (Filter by LTS Area), 'null' = No Filter), (default:'null')")],
        highlight: Annotated[Optional[StrictBool], Field(description="Hightlight Filter (possible values: 'false' = only ODHActivityPoi with Highlight false, 'true' = only ODHActivityPoi with Highlight true), (default:'null')")],
        source: Annotated[Optional[StrictStr], Field(description="Source Filter (possible Values: 'null' Displays all ODHActivityPoi, 'None', 'ActivityData', 'PoiData', 'GastronomicData', 'MuseumData', 'Magnolia', 'Content', 'SuedtirolWein', 'ArchApp'), (default:'null')")],
        odhtagfilter: Annotated[Optional[StrictStr], Field(description="ODH Taglist Filter (refers to Array SmgTags) (String, Separator ',' more Tags possible (OR FILTER), available Tags reference to 'v1/ODHTag?validforentity=odhactivitypoi'), (default:'null')")],
        odhtagfilter_and: Annotated[Optional[StrictStr], Field(description="ODH Taglist Filter (refers to Array SmgTags) (String, Separator ',' more Tags possible (AND FILTER), available Tags reference to 'v1/ODHTag?validforentity=odhactivitypoi'), (default:'null')")],
        odhactive: Annotated[Optional[StrictBool], Field(description="ODH Active (Published) ODHActivityPoi Filter (Refers to field OdhActive) (possible Values: 'true' only published ODHActivityPoi, 'false' only not published ODHActivityPoi), (default:'null')")],
        active: Annotated[Optional[StrictBool], Field(description="Active ODHActivityPoi Filter (possible Values: 'true' only active ODHActivityPoi, 'false' only not active ODHActivityPoi), (default:'null')")],
        categorycodefilter: Annotated[Optional[StrictStr], Field(description="CategoryCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes?rawfilter=eq(Type,\\\"CategoryCodes\\\")\" target=\"_blank\">GastronomyTypes</a>, Type: CategoryCodes")],
        dishcodefilter: Annotated[Optional[StrictStr], Field(description="DishCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes\" target=\"_blank\">GastronomyTypes</a>, Type: DishCodes")],
        ceremonycodefilter: Annotated[Optional[StrictStr], Field(description="CeremonyCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes\" target=\"_blank\">GastronomyTypes</a>, Type: CeremonyCodes")],
        facilitycodefilter: Annotated[Optional[StrictStr], Field(description="FacilityCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes\" target=\"_blank\">GastronomyTypes</a>, Type: with FacilityCodes_ prefix")],
        cuisinecodefilter: Annotated[Optional[StrictStr], Field(description="CuisineCode Filter (Only for ODHActivityTypes of type Gastronomy) (BITMASK) refers to <a href=\"https://tourism.opendatahub.com/v1/GastronomyTypes\" target=\"_blank\">GastronomyTypes</a>, Type: CuisineCodes")],
        difficultyfilter: Annotated[Optional[StrictStr], Field(description="Difficulty Filter (possible values: '1' = easy, '2' = medium, '3' = difficult), (default:'null')")],
        distancefilter: Annotated[Optional[StrictStr], Field(description="Distance Range Filter (Separator ',' example Value: 15,40 Distance from 15 up to 40 Km), (default:'null')")],
        altitudefilter: Annotated[Optional[StrictStr], Field(description="Altitude Range Filter (Separator ',' example Value: 500,1000 Altitude from 500 up to 1000 metres), (default:'null')")],
        durationfilter: Annotated[Optional[StrictStr], Field(description="Duration Range Filter (Separator ',' example Value: 1,3 Duration from 1 to 3 hours), (default:'null')")],
        hasimage: Optional[StrictBool],
        tagfilter: Annotated[Optional[StrictStr], Field(description="Filter on Tags. (Endpoint on v1/Tag) Syntax =and/or(Tag.Id,Tag.Id,Tag.Id) example or(summer,hiking) - and(themed hikes,family hikings) - or(hiking) - and(summer) - Combining and/or is not supported at the moment, default: 'null')")],
        publishedon: Annotated[Optional[StrictStr], Field(description="Published On Filter (Separator ',' List of publisher IDs), (default:'null')")],
        updatefrom: Annotated[Optional[StrictStr], Field(description="Returns data changed after this date Format (yyyy-MM-dd), (default: 'null')")],
        seed: Annotated[Optional[StrictStr], Field(description="Seed '1 - 10' for Random Sorting, '0' generates a Random Seed, not provided disables Random Sorting, (default:'null')")],
        latitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Latitude Format: '46.624975', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        longitude: Annotated[Optional[StrictStr], Field(description="GeoFilter FLOAT Longitude Format: '11.369909', 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        radius: Annotated[Optional[StrictStr], Field(description="Radius INTEGER to Search in Meters. Only Object withhin the given point and radius are returned and sorted by distance. Random Sorting is disabled if the GeoFilter Informations are provided, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#geosorting-functionality\" target=\"_blank\">Wiki geosort</a>")],
        polygon: Annotated[Optional[StrictStr], Field(description="valid WKT (Well-known text representation of geometry) Format, Examples (POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))) / By Using the GeoShapes Api (v1/GeoShapes) and passing Country.Type.Id OR Country.Type.Name Example (it.municipality.3066) / Bounding Box Filter bbc: 'Bounding Box Contains', 'bbi': 'Bounding Box Intersects', followed by a List of Comma Separated Longitude Latitude Tuples, 'null' = disabled, (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#polygon-filter-functionality\" target=\"_blank\">Wiki geosort</a>")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
        getasidarray: Annotated[Optional[StrictBool], Field(description="Get result only as Array of Ids, (default:false)  Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> ODHActivityPoiLinkedJsonResult:
        ...


    async def v1_odh_activity_poi_post(
        self,
        odh_activity_poi_linked: Annotated[Optional[ODHActivityPoiLinked], Field(description="ODHActivityPoi Object")],
    ) -> PGCRUDResult:
        ...


    async def single_odh_activity_poi(
        self,
        id: Annotated[StrictStr, Field(description="ID of the Poi")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> ODHActivityPoiLinked:
        ...


    async def v1_odh_activity_poi_id_put(
        self,
        id: Annotated[StrictStr, Field(description="ODHActivityPoi Id")],
        odh_activity_poi_linked: Annotated[Optional[ODHActivityPoiLinked], Field(description="ODHActivityPoi Object")],
    ) -> PGCRUDResult:
        ...


    async def v1_odh_activity_poi_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="ODHActivityPoi Id")],
    ) -> PGCRUDResult:
        ...


    async def v1_odh_activity_poi_types_get(
        self,
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        pagenumber: Optional[StrictInt],
        pagesize: Optional[StrictInt],
        idlist: Optional[StrictStr],
        seed: Optional[StrictStr],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        searchfilter: Annotated[Optional[StrictStr], Field(description="String to search for, Title in all languages are searched, (default: null) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#searchfilter\" target=\"_blank\">Wiki searchfilter</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawsort\" target=\"_blank\">Wiki rawsort</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[SmgPoiTypes]:
        ...


    async def single_odh_activity_poi_types(
        self,
        id: Annotated[StrictStr, Field(description="ID of the ODHActivityPoi Type")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language (default:'null' all languages are displayed)")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> SmgPoiTypes:
        ...
