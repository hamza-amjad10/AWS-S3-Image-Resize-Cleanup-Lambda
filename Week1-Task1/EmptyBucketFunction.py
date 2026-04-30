import json
import boto3

s3=boto3.client("s3")

def lambda_handler(event, context):

    bucket_name="testimages-storage-task1"

    #uploaded files deleted
    uploads_objects=s3.list_objects_v2(Bucket=bucket_name,Prefix="uploads/")
    if "Contents" not in uploads_objects:
        print("No files to delete in uploads folder")
    else:
        for obj in uploads_objects["Contents"]:
            image_name_upload=obj["Key"]
            s3.delete_object(Bucket=bucket_name,Key=image_name_upload)


    #resized files deleted
    resized_objects=s3.list_objects_v2(Bucket=bucket_name,Prefix="resized/")
    if "Contents" not in resized_objects:
        print("No files to delete in resized folder")
    else:
        for obj in resized_objects["Contents"]:
            image_name_resized=obj["Key"]
            s3.delete_object(Bucket=bucket_name,Key=image_name_resized)
    
    return {
        'statusCode': 200,
        'body': "Both folders files deleted"
    }


