from storages.backends.s3 import S3Storage
from django.conf import settings



class StaticFileStorage(S3Storage):
    bucket_name = "static"
    custom_domain = settings.AWS_S3_CUSTOM_STATIC_DOMAIN
    url_protocol = settings.AWS_S3_URL_PROTOCOL
    querystring_auth = False


class PrivateMediaStorage(S3Storage):
    bucket_name = "media"
    custom_domain = settings.AWS_S3_CUSTOM_PRIVATE_MEDIA_DOMAIN
    url_protocol = settings.AWS_S3_URL_PROTOCOL
    querystring_auth = True
    

class PublicMediaStorage(S3Storage):
    bucket_name = "media-public"
    custom_domain = settings.AWS_S3_CUSTOM_PUBLIC_MEDIA_DOMAIN
    url_protocol = settings.AWS_S3_URL_PROTOCOL
    querystring_auth = False