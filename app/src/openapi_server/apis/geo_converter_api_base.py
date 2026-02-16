# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.security_api import get_token_oauth2

class BaseGeoConverterApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseGeoConverterApi.subclasses = BaseGeoConverterApi.subclasses + (cls,)
    async def v1_geo_converter_kml_to_geo_json_get(
        self,
        url: Annotated[Optional[StrictStr], Field(description="The URL to the KML file.")],
    ) -> None:
        ...


    async def v1_geo_converter_kml_to_geo_json_post(
        self,
        body: Annotated[Optional[StrictStr], Field(description="The KML file content.")],
    ) -> None:
        ...


    async def v1_geo_converter_gpx_to_geo_json_get(
        self,
        url: Annotated[Optional[StrictStr], Field(description="The URL to the GPX file.")],
    ) -> None:
        ...


    async def v1_geo_converter_gpx_to_geo_json_post(
        self,
        body: Annotated[Optional[StrictStr], Field(description="The GPX file content.")],
    ) -> None:
        ...
