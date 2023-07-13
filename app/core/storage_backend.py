from storages.backends.s3boto3 import S3Boto3Storage


#conexines de django con aws

class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "private"
    
class MediaStorage(S3Boto3Storage):
    location = "media"
    file_overwrite = False