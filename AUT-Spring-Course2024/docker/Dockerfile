FROM python:3.9.19-alpine

COPY  requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python", "./cc_hw2_hello.py"]