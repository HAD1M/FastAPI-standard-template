import uvicorn 
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os

current_app_key = os.environ['app_key']
openport = int(os.environ['PORT'])

class ExampleInput(BaseModel):

    string: str 
    number: float


app = FastAPI()


@app.get('/')
def engine_name(response: JSONResponse):
    
    name ="Fastapi docker template"
    version = "February 2022"
    port = openport
    
    result = {
		"name":name,
		"version":version,
		"port":port
	}
    
    return result

@app.post('/sample_request_1', status_code = 200)
def sample_func_1(request: Request, response: JSONResponse):
    app_key = request.headers.get('app-key')
    if app_key != current_app_key:
        response.status_code = 403
        status=0
        return {'status':status}
        
    data = ["kuaci","sapi","api","smilikiti"]
    file_list = []
    
    try:
        file_list = os.listdir("mount/")
    except Exception as e:
        print(e)
        
    try:
        with open("folder_copy/sample.txt", "r") as f:
            data.append(f.readline())
    except Exception as e:
        print(e)
        
    return {"status":1,"data":data,"file_list":file_list}

@app.post('/sample_request_2', status_code = 200)
def sample_func_2(input_:ExampleInput, request: Request, response: JSONResponse):
    """
    Compute string length times the number
    """
    app_key = request.headers.get('app-key')
    if app_key != current_app_key:
        response.status_code = 403
        status=0
        return {'status':status}
        
    try:
        input_dict = input_.dict()
        result = len(input_dict['string'])*input_dict['number']
        status = 1 # Success
    except:
        result = 0
        status = 0 #  Failed

    return {'status': status, 'result':result}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=openport)
