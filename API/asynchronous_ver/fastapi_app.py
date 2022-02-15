import uvicorn 
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import fetch_data_simulation as fetch_data_simulation
import os

current_app_key = os.environ['app_key']
openport = int(os.environ['PORT'])

class ExampleInput(BaseModel):

    number_data: int

app = FastAPI()

@app.get('/')
def engine_name(response: JSONResponse):
    
    name ="Fastapi async docker template"
    version = "February 2022"
    port = openport
    
    result = {
		"name":name,
		"version":version,
		"port":port
	}
    
    return result

@app.post('/fetch_all_data', status_code = 200)
async def async_sample_func(input_:ExampleInput, request: Request, response: JSONResponse):

    app_key = request.headers.get('app-key')
    if app_key != current_app_key:
        response.status_code = 403
        status=0
        return {'status':status}
        
    try:
        input_dict = input_.dict()
        result = await fetch_data_simulation.fetch_all_data(input_dict['number_data'])
        status = 1 # Success
    except:
        result = {'all_data': []}
        status = 0 #  Failed

    return {'status': status, 'result':result}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=openport)
