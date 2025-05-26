from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

from .config import settings

apikey_scheme = APIKeyHeader(name="X-Api-Key", auto_error=False)


def api_key_check(apikey: Annotated[str, Depends(apikey_scheme)]):
    if apikey != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return True
