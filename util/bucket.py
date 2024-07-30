import requests
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import os
import util.common as cmn_util


# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = os.environ['COS_SECRET_ID']     # 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
secret_key = os.environ['COS_SECRET_KEY']   # 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
region = 'ap-shanghai'      # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS 支持的所有 region 列表参见 https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入 token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
dream_img_bucket = 'dream-1316638121'       # 腾讯对象存储服务器生成图片后存放位置

async def img2bucket(url):
    stream = requests.get(url)
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
    client = CosS3Client(config)
    file_name = cmn_util.rand_file_name()
    # 网络流将以 Transfer-Encoding:chunked 的方式传输到 COS
    response = client.put_object(
        Bucket=dream_img_bucket,
        Body=stream,
        Key=file_name
    )
    return {"res": response, "file_name": file_name}

def assembl_cos_file_url(file_name="", bucket=""):
    return ''.join(['https://dream-1316638121.cos.ap-shanghai.myqcloud.com/', file_name])