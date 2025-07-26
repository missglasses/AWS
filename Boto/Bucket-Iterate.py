# get list_buckets response
response = s3.list_buckets()

# iterarte buckets from ^^
for bucket in response['Buckets']:
  
#print each
    print(bucket['Name'])
