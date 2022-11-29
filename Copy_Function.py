import boto3
import os
import datetime
from datetime import datetime,timedelta

#Creating Session With Boto3.
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')
source_bucket = s3_resource.Bucket(os.environ['INPUT_BUCKET'])
current_time = datetime.now()

def lambda_handler(event, context):

    for obj in source_bucket.objects.all():
        print(obj)
        #Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
        copy_source = {
            'Bucket': os.environ['INPUT_BUCKET'],
            'Key': obj.key
        }
        
        
        bucket = s3_resource.Bucket(os.environ['OUTPUT_BUCKET'])
        bucket.copy(copy_source, os.environ['OUTPUT_FOLDER']+'Copied-{}-{}'.format(current_time.strftime('%Y-%m-%d-%H-%M-%S-%f'), obj.key.split('/')[-1]))
        
        # Printing the Information That the File Is Copied.
        print('Single File is copied')