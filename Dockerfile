FROM python:3.10-bullseye
WORKDIR /app
RUN mkdir /app/exposed
RUN mkdir /app/web
VOLUME /app/exposed
ADD mkRSS.py /app/
CMD ["python", "mkRSS.py"]
