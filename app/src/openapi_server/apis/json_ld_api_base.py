# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.security_api import get_token_oauth2

class BaseJsonLDApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseJsonLDApi.subclasses = BaseJsonLDApi.subclasses + (cls,)
    async def v1_json_ld_detail_in_ld_get(
        self,
        type: Annotated[Optional[StrictStr], Field(description="Type to transform currently available: ('accommodation', 'gastronomy', 'event', 'recipe', 'poi', 'region', 'tv', 'municipality', 'district', 'skiarea') required <a href=\"https://github.com/noi-techpark/odh-docs/wiki/Dataset-Type\" target=\"_blank\">Wiki Dataset Type</a>")],
        id: Annotated[Optional[StrictStr], Field(description="ID of the data to transform, required")],
        language: Annotated[Optional[StrictStr], Field(description="Output Language, standard EN")],
        idtoshow: Annotated[Optional[StrictStr], Field(description="ID to show on Json LD @id, not provided Id of ODH api call is taken")],
        urltoshow: Annotated[Optional[StrictStr], Field(description="url to show on Json LD @id, not provided idtoshow is taken, idtoshow not provided url is filled with url of the data")],
        imageurltoshow: Annotated[Optional[StrictStr], Field(description="image url to show on Json LD @image, not provided image url of data is taken")],
        showid: Annotated[Optional[StrictBool], Field(description="Show the @id property in Json LD default value true")],
    ) -> None:
        ...
