# upload final_report.csv to gid-staging
s3.upload_file(Filename='final_report.csv',
               Bucket='gid-staging',
               Key='2019/final_report_01_01.csv')

# get obj
response = s3.head_object(Bucket='gid-staging', 
                          Key='2019/final_report_01_01.csv')

# print size of uploaded obj
print(response['ContentLength']) #209
