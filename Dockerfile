FROM python:3.10.12
WORKDIR /app
COPY flaskproject .
RUN pip install flask 
RUN pip install flask_mysqldb
RUN ls -l 
EXPOSE 5000
CMD ["python3", "app.py"]


