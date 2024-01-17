FROM tiangolo/uvicorn-gunicorn:python3.9

RUN mkdir /fastapi

COPY requirements.txt /fastapi

WORKDIR /fastapi

RUN pip install --no-cache-dir --upgrade  -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . /fastapi

EXPOSE 8000

ENTRYPOINT ["uvicorn", "server:app","--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

