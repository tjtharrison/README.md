# S3 Bucket Policy to enforce Public accessibility

When you enable public access to an S3 bucket – All created files CAN be made publicly accessibly but are not by default.

To make all files published to the S3 bucket publicly accessible by default, you must update the Bucket policy (Permissions > Bucket Policy)

```
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Sid": "AddPerm",
   "Effect": "Allow",
   "Principal": "*",
   "Action": "s3:GetObject",
   "Resource": "arn:aws:s3:::[bucket-name]/*"
  }
 ]
}
```