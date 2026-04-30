import json
from PIL import Image
import boto3 # boto3 use to talk with s3 bucket
import io # why we use io we don't wants to save file on disk(harddrive)
# we want to process image in memory not saved and no time waste
from urllib.parse import unquote_plus


s3=boto3.client("s3")
# now connect is made with s3 

#event is message comes from s3 bucket like hey lambda this image is uploaded
# context is lambda information like check execution time and debugging time 
def lambda_handler(event, context):


    # get record of s3 bucket and using index1
    record=event["Records"][0]
    # extract the bucket name
    bucket=record["s3"]["bucket"]["name"]
    key=record["s3"]["object"]["key"]
    key = unquote_plus(key)

    # now I have record and bucket name and key 

    result=s3.get_object(Bucket=bucket,Key=key)

    binary_data=result["Body"].read()
    #read binary image data 
    image=io.BytesIO(binary_data)
    img=Image.open(image)
    new_resized_image=img.resize((200,200))
    buffer=io.BytesIO()
    image_name=key.split("/")
    extensions=image_name[-1].split(".")
    print("extensions of the images: ",extensions[-1])
    

    if extensions[-1]=="png":
        new_resized_image.save(buffer,format=extensions[-1])
    elif extensions[-1] == "jpeg":
        new_resized_image.save(buffer, format="JPEG")
    elif extensions[-1] == "jpg":
        new_resized_image.save(buffer, format="JPEG")
    else:
        print("Unsupported Format")
        return {"statusCode":404,"message":"Unsupported Format"}

    buffer.seek(0)

    

    # now put the image in resized folder
    s3.put_object(Bucket=bucket,Key="resized/"+image_name[-1],Body=buffer.getvalue())


    return {
    "statusCode": 200,
    "message": "Success",
    "input_bucket": bucket,
    "input_key": key,
    "output_path": "resized/" + image_name[-1]
}




