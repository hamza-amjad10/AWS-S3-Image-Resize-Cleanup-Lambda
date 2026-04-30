# AWS Lambda Image Processing with S3 (Resize + Cleanup)

This project demonstrates a **serverless image processing pipeline using AWS Lambda and Amazon S3**. It automatically resizes uploaded images and stores them in a separate folder, and also provides a cleanup function to delete processed files.

---

## 🚀 Features

- 📤 Automatically triggers on image upload to S3 (`uploads/` folder)
- 🖼️ Resizes images to **200x200 pixels**
- 💾 Stores processed images in `resized/` folder
- 🧠 Uses **in-memory processing (no disk usage)**
- 🧹 Separate Lambda function to delete files from S3 folders
- ⚡ Fully serverless architecture

---

## 🏗️ Architecture


S3 Bucket (uploads/)
↓
Lambda Trigger
↓
Resize Image (Pillow)
↓
S3 Bucket (resized/)


---

## 📁 Project Structure

```
Week1-Task1/
│
├── ImageResizeLambdaFunction.py # Resizes uploaded images
├── EmptyBucketFunction.py # Deletes files from S3 folders
└── README.md
```

---

## ⚙️ Technologies Used

- AWS Lambda 
- Amazon S3 
- Python 
- Pillow (PIL) 
- Boto3 

---

## 🧠 How It Works

### 1. Image Upload Flow
1. Image is uploaded to S3 bucket → `uploads/`
2. S3 triggers Lambda function
3. Lambda:
   - Reads image in memory
   - Resizes it to **200x200**
   - Saves it to `resized/` folder

---

### 2. Cleanup Flow
1. Second Lambda function runs manually or via trigger
2. It deletes:
   - All files in `uploads/`
   - All files in `resized/`

---

## 🧾 Lambda Code Overview

### 🖼️ Resize Lambda
- Reads image from S3
- Handles `.png`, `.jpg`, `.jpeg`
- Uses `io.BytesIO` for memory processing
- Uploads resized image back to S3

---

### 🧹 Cleanup Lambda
- Lists objects in S3 folders
- Deletes all files in:
  - `uploads/`
  - `resized/`

---

## 📦 Requirements

Install dependencies:

```bash
pip install boto3 pillow


boto3
Pillow
🔐 IAM Permissions Required

Your Lambda role must include:

s3:GetObject
s3:PutObject
s3:ListBucket
s3:DeleteObject
🪣 S3 Bucket Structure
testimages-storage-task1/
│
├── uploads/   → Original images
└── resized/   → Processed images
⚠️ Important Notes
Lambda processes images in memory (no disk storage)
Always ensure correct S3 trigger on uploads folder
Large images may require increased Lambda timeout/memory
```
---

##📌 Example Output
```bash
{
  "statusCode": 200,
  "message": "Success",
  "input_bucket": "testimages-storage-task1",
  "input_key": "uploads/image.png",
  "output_path": "resized/image.png"
}

```

## 👨‍💻 Author
```bash
Hamza Amjad
Built for learning AWS serverless architecture with real-world image processing flow.

```
