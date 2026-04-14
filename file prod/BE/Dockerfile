FROM python:3.13.3-slim

WORKDIR /main-app

COPY . . 

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "webserver.py"]


HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "-f", "localhost:5000/health" ] || exit 1