# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.search_api_base import BaseSearchApi
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
from openapi_server.models.json_raw import JsonRaw
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/Find",
    responses={
        200: {"model": List[JsonRaw], "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Search"],
    summary="GET Search over all Entities",
    response_model_by_alias=True,
)
async def v1_find_get(
    term: Annotated[Optional[StrictStr], Field(description="Term to Search for <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Search-over-all-Entities-in-ODH-Tourism-api\" target=\"_blank\">Wiki</a>")] = Query(None, description="Term to Search for &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Search-over-all-Entities-in-ODH-Tourism-api\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki&lt;/a&gt;", alias="term"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language ('null' all languages are displayed)")] = Query('en', description="Language field selector, displays data and fields available in the selected language (&#39;null&#39; all languages are displayed)", alias="language"),
    odhtype: Optional[StrictStr] = Query(None, description="", alias="odhtype"),
    type: Annotated[Optional[StrictStr], Field(description="Restrict search to Entities (accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... ) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\" target=\"_blank\">Wiki Dataset Type</a>")] = Query(None, description="Restrict search to Entities (accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... ) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki Dataset Type&lt;/a&gt;", alias="type"),
    searchbasetext: Annotated[Optional[StrictBool], Field(description="Search also trough base text (true/false), caution can slow down the search significantly")] = Query(False, description="Search also trough base text (true/false), caution can slow down the search significantly", alias="searchbasetext"),
    filteronfields: Annotated[Optional[List[StrictStr]], Field(description="Search also on this fields, syntax analog to the fields filter")] = Query(None, description="Search also on this fields, syntax analog to the fields filter", alias="filteronfields"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")] = Query(None, description="Locfilter SPECIAL Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki locfilter&lt;/a&gt;", alias="locfilter"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
    limitto: Annotated[Optional[StrictInt], Field(description="Limit search to n items per entity")] = Query(5, description="Limit search to n items per entity", alias="limitto"),
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
) -> List[JsonRaw]:
    if not BaseSearchApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchApi.subclasses[0]().v1_find_get(term, language, odhtype, type, searchbasetext, filteronfields, locfilter, fields, rawfilter, rawsort, limitto, removenullvalues)


@router.get(
    "/v1/Filter",
    responses={
        200: {"model": List[JsonRaw], "description": "List created"},
        400: {"model": ProblemDetails, "description": "Request Error"},
        500: {"description": "Internal Server Error"},
    },
    tags=["Search"],
    summary="GET Search over all Entities",
    response_model_by_alias=True,
)
async def v1_filter_get(
    term: Annotated[Optional[StrictStr], Field(description="Term to Search for <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Search-over-all-Entities-in-ODH-Tourism-api\" target=\"_blank\">Wiki</a>")] = Query(None, description="Term to Search for &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Search-over-all-Entities-in-ODH-Tourism-api\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki&lt;/a&gt;", alias="term"),
    language: Annotated[Optional[StrictStr], Field(description="Language field selector, displays data and fields available in the selected language ('null' all languages are displayed)")] = Query('en', description="Language field selector, displays data and fields available in the selected language (&#39;null&#39; all languages are displayed)", alias="language"),
    odhtype: Optional[StrictStr] = Query(None, description="", alias="odhtype"),
    type: Annotated[Optional[StrictStr], Field(description="Restrict search to Entities (accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... ) <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\" target=\"_blank\">Wiki Dataset Type</a>")] = Query(None, description="Restrict search to Entities (accommodation, odhactivitypoi, event, webcam, measuringpoint, ltsactivity, ltspoi, ltsgastronomy, article ..... ) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki Dataset Type&lt;/a&gt;", alias="type"),
    searchbasetext: Annotated[Optional[StrictBool], Field(description="Search also trough base text (true/false), caution can slow down the search significantly")] = Query(False, description="Search also trough base text (true/false), caution can slow down the search significantly", alias="searchbasetext"),
    filteronfields: Annotated[Optional[List[StrictStr]], Field(description="Search also on this fields, syntax analog to the fields filter")] = Query(None, description="Search also on this fields, syntax analog to the fields filter", alias="filteronfields"),
    locfilter: Annotated[Optional[StrictStr], Field(description="Locfilter SPECIAL Separator ',' possible values: reg + REGIONID = (Filter by Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID = (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by Municipality), fra + FRACTIONID = (Filter by Fraction), 'null' = (No Filter), (default:'null') <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\" target=\"_blank\">Wiki locfilter</a>")] = Query(None, description="Locfilter SPECIAL Separator &#39;,&#39; possible values: reg + REGIONID &#x3D; (Filter by Region), reg + REGIONID &#x3D; (Filter by Region), tvs + TOURISMVEREINID &#x3D; (Filter by Tourismverein), mun + MUNICIPALITYID &#x3D; (Filter by Municipality), fra + FRACTIONID &#x3D; (Filter by Fraction), &#39;null&#39; &#x3D; (No Filter), (default:&#39;null&#39;) &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Geosorting-and-Locationfilter-usage#location-filter-locfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki locfilter&lt;/a&gt;", alias="locfilter"),
    fields: Annotated[Optional[List[StrictStr]], Field(description="Select fields to display, More fields are indicated by separator ',' example fields=Id,Active,Shortname (default:'null' all fields are displayed). <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\" target=\"_blank\">Wiki fields</a>")] = Query(None, description="Select fields to display, More fields are indicated by separator &#39;,&#39; example fields&#x3D;Id,Active,Shortname (default:&#39;null&#39; all fields are displayed). &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Common-parameters%2C-fields%2C-language%2C-searchfilter%2C-removenullvalues%2C-updatefrom#fields\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki fields&lt;/a&gt;", alias="fields"),
    rawfilter: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawfilter</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawfilter&lt;/a&gt;", alias="rawfilter"),
    rawsort: Annotated[Optional[StrictStr], Field(description="<a href=\"https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\" target=\"_blank\">Wiki rawsort</a>")] = Query(None, description="&lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Using-rawfilter-and-rawsort-on-the-Tourism-Api#rawfilter\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki rawsort&lt;/a&gt;", alias="rawsort"),
    limitto: Annotated[Optional[StrictInt], Field(description="Limit search to n items per entity")] = Query(5, description="Limit search to n items per entity", alias="limitto"),
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
) -> List[JsonRaw]:
    if not BaseSearchApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchApi.subclasses[0]().v1_filter_get(term, language, odhtype, type, searchbasetext, filteronfields, locfilter, fields, rawfilter, rawsort, limitto, removenullvalues)
