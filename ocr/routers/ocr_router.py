from fastapi import APIRouter, UploadFile, File, Query
from typing import Union
from logger import ShanksLogger
from logging.config import dictConfig

import logging

logger = logging.getLogger('ShanksOCRToolkit')
dictConfig(ShanksLogger().dict())
logger.propagate = False

ocr_router = APIRouter()


@ocr_router.get('/shanks/ocr/raw')
async def file_input(file: UploadFile = File(...), query_params: Union[list[str], None] = Query(default=None)):
    return "OK"
