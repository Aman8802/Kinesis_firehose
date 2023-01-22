try:
    import re
    import os
    import json
    import boto3
    import datetime
    import uuid
    from datetime import datetime
    import json
    from faker import Faker
    import random
    #import faker
except Exception as e:
    print("Error : {} ".format(e))
 
 
def main():
 
    AWS_ACCESS_KEY = "AKIA2OLGZXFFBUKYA4BP"
    AWS_SECRET_KEY = "LK0nu3H6/wzBXoo1z/c9bm/Wk+QAtm2Yk3Wz1kGq"
    AWS_REGION_NAME = "ap-south-1"
 
    for i in range(1, 25):
        fake = Faker()
        json_data = {
            "name": fake.name(),
            "phone_numbers": fake.phone_number(),
            "city": fake.city(),
            "address": fake.address(),
            "date": str(fake.date()),
            "customer_id": str(random.randint(1, 5))
        }
        print(json_data)
 
        client = boto3.client(
            "firehose",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION_NAME,
        )
 
        response = client.put_record(
            DeliveryStreamName='Kinesis_Data_Firehose',
            Record={
                'Data': json.dumps(json_data)
            }
        )
        print(response)
 
 
 
main()
 
"""
customer_id=!{partitionKeyFromQuery:customer_id}/
"""
