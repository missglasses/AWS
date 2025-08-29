# generating a Boto3 client interacting with S3
s3 = boto3.client('s3', region_name='us-east-1', 
                        # credentials 
                        aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)
# list the buckets
buckets = s3.list_buckets()

#print
print(buckets)
