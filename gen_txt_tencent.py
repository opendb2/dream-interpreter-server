import json
import types
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

async def tencent_chat(msgs):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential("secret_id", "secret_key")
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "hunyuan.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = hunyuan_client.HunyuanClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChatCompletionsRequest()
        params = {
            "TopP": 1,
            "Temperature": 1,
            "Model": "hunyuan-pro",
            "Stream": True,
            # "Messages": [
            #     {
            #         "Role": "system",
            #         "Content": "你是一名职业精神分析家。请根据精神分析理论，对提供的内容进行深度解析。请首先检查用户的输入是否有明显混乱或者是恶意或恶作剧的输入，只有客户输入的信息是合理的，我们才进行解析。在输出内容中，仔细把握内容的重点和细节，进行更为具像化的分析，而不要输出空泛的大道理。请询问客户对于内容的解析是否满意。如果不满意，可继续提问，并请求确认。请在输出前考虑之前的对话历史。请以第二人称输出。输出的文风以弗洛伊德的写作风格。请同时给出 1 到 2 条建议。最后请构想 1 个后续的相关的问题，采用第一人称，引导用户继续对话。"
            #     },
            #     {
            #         "Role": "user",
            #         "Content": "我梦到了一只独角兽"
            #     },
            # ]
            "Messages": msgs
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个ChatCompletionsResponse的实例，与请求对象对应
        resp = client.ChatCompletions(req)
        # 输出json格式的字符串回包
        if isinstance(resp, types.GeneratorType):  # 流式响应
            res_str = ""
            for event in resp:
                choices = json.loads(event["data"])["Choices"]
                res_str += choices[0]["Delta"]["Content"]
            print(res_str)
            return {"Role": "assistant", "Content": res_str}
        else:  # 非流式响应
            print(resp)
            return ""
    except TencentCloudSDKException as err:
        print(err)
