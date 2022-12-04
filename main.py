from fastapi import FastAPI
from ocr import ocr_router
from logger import ShanksLogger
from logging.config import dictConfig

import logging
import uvicorn

logger = logging.getLogger('ShanksOCRToolkit')
dictConfig(ShanksLogger().dict())
logger.propagate = False

app = FastAPI()
app.include_router(ocr_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8080, workers=2)
