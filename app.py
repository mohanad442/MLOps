from fastapi import FastAPI 
from Multiply_two_variables import Mul_two_variables
from models import SamplePostRequest
import logging
import time

app = FastAPI()

logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.get('/')
def home():
    return 'Hello World'

@app.get('/health')
def health_check():
    return 'OK'

@app.post('/predict')
def predict(request: SamplePostRequest):
    return request.a + request.c[0]

@app.get('/Multiply')
def Mul_two_variables_endpoint(value_1 : int, value_2 : int):
    start = time.time()
    # logger.error(f'Error Recieved {value_1=}, {value_2=}')
    # logger.exception(f'Exception Recieved {value_1=}, {value_2=}')
    # logger.warning(f'warning Recieved {value_1=}, {value_2=}')
    logger.info(f'Info Recieved {value_1=}, {value_2=}')
    # logger.debug(f'Debug Recieved {value_1=}, {value_2=}')
    output = Mul_two_variables(value_1, value_2)
    end = time.time()
    
    logger.info(f'time = {end - start} seconds')
    return 