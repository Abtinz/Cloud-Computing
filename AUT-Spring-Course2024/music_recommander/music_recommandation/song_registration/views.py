from django.shortcuts import render

# Create your views here.
import boto3
from botocore.exceptions import ClientError

ENDPOINT_URL = "https://storage.iran.liara.space"
ACCESS_KEY = '8i78bqf275249chu'
SECRET_KEY = '3fadd59f-da2e-4978-bab5-a5968d3977f1'
BUCKET_NAME = 'sarvins3'