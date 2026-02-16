# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.json_ld_api_base import BaseJsonLDApi
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
from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.security_api import get_token_oauth2

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/v1/JsonLD/DetailInLD",
    responses={
        200: {"description": "OK"},
    },
    tags=["JsonLD"],
    summary="GET Detail Data in JSON LD Format (Schema.org Datatypes as output)",
    response_model_by_alias=True,
)
async def v1_json_ld_detail_in_ld_get(
    type: Annotated[Optional[StrictStr], Field(description="Type to transform currently available: ('accommodation', 'gastronomy', 'event', 'recipe', 'poi', 'region', 'tv', 'municipality', 'district', 'skiarea') required <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\" target=\"_blank\">Wiki Dataset Type</a>")] = Query(None, description="Type to transform currently available: (&#39;accommodation&#39;, &#39;gastronomy&#39;, &#39;event&#39;, &#39;recipe&#39;, &#39;poi&#39;, &#39;region&#39;, &#39;tv&#39;, &#39;municipality&#39;, &#39;district&#39;, &#39;skiarea&#39;) required &lt;a href&#x3D;\&quot;https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Wiki Dataset Type&lt;/a&gt;", alias="type"),
    id: Annotated[Optional[StrictStr], Field(description="ID of the data to transform, required")] = Query(None, description="ID of the data to transform, required", alias="Id"),
    language: Annotated[Optional[StrictStr], Field(description="Output Language, standard EN")] = Query('en', description="Output Language, standard EN", alias="language"),
    idtoshow: Annotated[Optional[StrictStr], Field(description="ID to show on Json LD @id, not provided Id of ODH api call is taken")] = Query('', description="ID to show on Json LD @id, not provided Id of ODH api call is taken", alias="idtoshow"),
    urltoshow: Annotated[Optional[StrictStr], Field(description="url to show on Json LD @id, not provided idtoshow is taken, idtoshow not provided url is filled with url of the data")] = Query('', description="url to show on Json LD @id, not provided idtoshow is taken, idtoshow not provided url is filled with url of the data", alias="urltoshow"),
    imageurltoshow: Annotated[Optional[StrictStr], Field(description="image url to show on Json LD @image, not provided image url of data is taken")] = Query('', description="image url to show on Json LD @image, not provided image url of data is taken", alias="imageurltoshow"),
    showid: Annotated[Optional[StrictBool], Field(description="Show the @id property in Json LD default value true")] = Query(True, description="Show the @id property in Json LD default value true", alias="showid"),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
    token_oauth2: TokenModel = Security(
        get_token_oauth2, scopes=[]
    ),
) -> None:
    if not BaseJsonLDApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseJsonLDApi.subclasses[0]().v1_json_ld_detail_in_ld_get(type, id, language, idtoshow, urltoshow, imageurltoshow, showid)
