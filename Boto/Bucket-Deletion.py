# delete the gim-test bucket
s3.delete_bucket(Bucket='gim-test')

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])
