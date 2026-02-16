# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictStr
from typing import Any, List, Optional
from openapi_server.models.string_string_values_key_value_pair import StringStringValuesKeyValuePair
from openapi_server.security_api import get_token_oauth2

class BaseFileUploadApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseFileUploadApi.subclasses = BaseFileUploadApi.subclasses + (cls,)
    async def v1_file_upload_post(
        self,
        form: Optional[List[StringStringValuesKeyValuePair]],
    ) -> None:
        ...


    async def v1_file_upload_image_post(
        self,
        form: Optional[List[StringStringValuesKeyValuePair]],
    ) -> None:
        ...


    async def v1_file_delete_filepath_delete(
        self,
        filepath: StrictStr,
    ) -> None:
        ...
