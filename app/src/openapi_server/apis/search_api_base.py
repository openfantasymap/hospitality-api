# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.json_raw import JsonRaw
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

class BaseSearchApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSearchApi.subclasses = BaseSearchApi.subclasses + (cls,)
    async def v1_find_get(
        self,
        term: Annotated[Optional[StrictStr], Field(description="Term to Search for <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Search-over-all-Entities-in-ODH-Tourism-api\" target=\"_blank\">Wiki</a>")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language ('null' all languages are displayed)")],
        odhtype: Optional[StrictStr],
        type: Annotated[Optional[StrictStr], Field(description="Restrict search to Entities (accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... ) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\" target=\"_blank\">Wiki Dataset Type</a>")],
        searchbasetext: Annotated[Optional[StrictBool], Field(description="Search also trough base text (true/false), caution can slow down the search significantly")],
        filteronfields: Annotated[Optional[List[StrictStr]], Field(description="Search also on this fields, syntax analog to the fields filter")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")],
        limitto: Annotated[Optional[StrictInt], Field(description="Limit search to n items per entity")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[JsonRaw]:
        ...


    async def v1_filter_get(
        self,
        term: Annotated[Optional[StrictStr], Field(description="Term to Search for <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Search-over-all-Entities-in-ODH-Tourism-api\" target=\"_blank\">Wiki</a>")],
        language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language ('null' all languages are displayed)")],
        odhtype: Optional[StrictStr],
        type: Annotated[Optional[StrictStr], Field(description="Restrict search to Entities (accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... ) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\" target=\"_blank\">Wiki Dataset Type</a>")],
        searchbasetext: Annotated[Optional[StrictBool], Field(description="Search also trough base text (true/false), caution can slow down the search significantly")],
        filteronfields: Annotated[Optional[List[StrictStr]], Field(description="Search also on this fields, syntax analog to the fields filter")],
        locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")],
        fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")],
        rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")],
        rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")],
        limitto: Annotated[Optional[StrictInt], Field(description="Limit search to n items per entity")],
        removenullvalues: Annotated[Optional[StrictBool], Field(description="Remove all Null values from json output. Useful for reducing json size. By default set to false. Documentation on <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters,-fields,-language,-searchfilter,-removenullvalues,-updatefrom#removenullvalues\" target=\"_blank\">Opendatahub Wiki</a>")],
    ) -> List[JsonRaw]:
        ...
