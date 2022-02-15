FROM python:3.8

RUN pip install fastapi
RUN pip install "uvicorn[standard]"

copy /fastapi_app.py /
copy /fetch_data_simulation.py /

CMD [ "python","-u","-W ignore", "./fastapi_app.py" ]