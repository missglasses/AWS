response = s3.list_buckets()

# delete those buckets with 'gim' &create replacements.
for bucket in response['Buckets']:
  if 'gim' in bucket['Name']:
      s3.delete_bucket(Bucket=bucket['Name'])
    
s3.create_bucket(Bucket='gid-staging')
s3.create_bucket(Bucket='gid-processed')
  
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
