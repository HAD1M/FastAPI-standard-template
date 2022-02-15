FROM python:3.8

RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN mkdir mount

copy folder_copy folder_copy/
copy /fastapi_app.py /

CMD [ "python","-u","-W ignore", "./fastapi_app.py" ]