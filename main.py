# This is a sample Python script.
import json

import init
init.init()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sanic import Sanic, response
import gen_img
import gen_txt_tencent
import common as common_api
import gen_txt_gpt as gpt_text
import util.bucket as bucket
import gen_img_fal as fal_gen

init.init()
app = Sanic("Example")


# @app.route("/api/test-sql", methods=["GET"])
# async def test_sql(request):
#     res = await common_api.share_view_by_id()
#     return response.json({"errNo": 0, "data": {}})

# 测试 cos 上传
# @app.route("/api/test-cos", methods=["GET"])
# async def test_cos(request):
#     res = await bucket.img2bucket("https://pic.52112.com/180128/Unicorns/Afb0IIfm0u.jpg")
#     print(res)
#     print('file url:', bucket.assembl_cos_file_url(res.get("file_name", None)))
#     return response.json({"errNo": 0, "data": {}})

@app.route("/api/test-img", methods=["POST", "GET", "PUT"])
async def test_img(request):
    return response.json({"errNo": 0, "data": {"imgUrl": 'https://blobs-temp.sfo3.digitaloceanspaces.com/C7E3144965E8CEF284ADA436DDA792C53EADE2D1D94AD35E501327BFBC785C25?X-Amz-Expires=3600&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=DO00F84RAAYEUTBJ6D9L%2F20240717%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240717T064308Z&X-Amz-SignedHeaders=host&X-Amz-Signature=5edfbc291b59245786cc7be87402325502893e62b198277877899f582da1e7bc'}})

@app.route("/api/test-img-fal", methods=["GET"])
async def test_img_fal(request):
    fal_gen.txt2img()
    return response.json({"errNo": 0, "data": {}})
@app.route("/api/test-gpt", methods=["POST", "GET", "PUT"])
async def test_gpt(request):
    res = await gpt_text.gpt_chat([])
    return response.json({"errNo": 0, "data": {}})

@app.route("/api", methods=["POST", "PUT"])
async def test(request):
    return response.json({"test": True})

@app.route("/api/gen-gpt-chat", methods=["POST", "GET", "PUT"])
async def gen_gpt_chat(request):
    params = request.json
    messages = params.get('messages', None)
    if messages is None:
        return response.json({"errNo": 999, "data": 'messages is required'})
    print("gen_chat:messages:", messages)
    res = await gpt_text.gpt_chat(messages)
    return response.json({"errNo": 0, "data": {"suggest": res}})

@app.route("/api/gen-chat", methods=["POST", "GET", "PUT"])
async def gen_chat(request):
    params = request.json
    messages = params.get('messages', None)
    if messages is None:
        return response.json({"errNo": 999, "data": 'messages is required'})
    print("gen_chat:messages:", params["messages"])
    res = await gen_txt_tencent.tencent_chat(params["messages"])
    return response.json({"errNo": 0, "data": {"suggest": res}})
@app.route("/api/gen-img", methods=["POST", "GET", "PUT"])
async def gen2img(request):
    params = request.json
    promote = params.get('promote', None)
    # img_url = ""
    # img_url = await gen_img.txt2img("", params["promote"])
    img_url = await fal_gen.txt2img(promote)
    if img_url:
        return response.json({"errNo": 0, "data": {"imgUrl": img_url}})
    return response.json({"errNo": 999, "data": {"imgUrl": ''}})

@app.route("/api/share", methods=["POST", "PUT"])
async def share(request):
    params = request.json
    dream_id = params.get('dream_id', None)
    prompt = params.get('prompt', None)
    img = params.get('img', None)
    messages = params.get('messages', None)
    suggest = params.get('suggest', None)
    if prompt is None:
        return response.json({"errNo": 999, "data": 'prompt is required'})
    if img is None:
        return response.json({"errNo": 999, "data": 'img is required'})
    if messages is None:
        return response.json({"errNo": 999, "data": 'messages are required'})
    if suggest is not None:
        suggest = params["suggest"]
    if dream_id is None:
        return response.json({"errNo": 999, "data": 'dream_id is required'})
    id = await common_api.share_create(prompt, img, messages, suggest, dream_id)
    return response.json({"errNo": 0, "data": {"id": id}})

@app.route("/api/share-list", methods=["GET"])
async def share_list(request):
    list = await common_api.share_list()
    print("api/share-list: list:", list)
    return response.json({"errNo": 0, "data": {"list": list}})

@app.route("/api/share-get", methods=["POST", "GET"])
async def share_get(request):
    params = request.json
    id = params.get("id", None)
    if id is None:
        return response.json({"errNo": 999, "data": 'id is required'})
    dream = await common_api.share_view_by_id(id)
    if dream is None:
        response.json({"errNo": 0,
                       "data": {}})
    return response.json({"errNo": 0, "data": {"id": id, "prompt": dream.prompt, "img": dream.img, "messages": dream.conversations, "suggest": dream.suggest}})


@app.route("/api/dream-update", methods=["POST", "PUT"])
async def dream_update(request):
    params = request.json
    id = params.get('id', None)
    prompt = params.get('prompt', None)
    img = params.get('img', None)
    messages = params.get('messages', None)
    suggest = params.get('suggest', None)
    if prompt is None:
        return response.json({"errNo": 999, "data": 'prompt is required'})
    if img is None:
        return response.json({"errNo": 999, "data": 'img is required'})
    if messages is None:
        return response.json({"errNo": 999, "data": 'messages are required'})
    id = await common_api.dream_update(id, prompt, img, messages, suggest)
    print('api:dream-update:id:', id)
    return response.json({"errNo": 0, "data": {"id": id}})

@app.route("/api/dream-get", methods=["POST", "GET"])
async def dream_get(request):
    params = request.json
    id = params.get('id', None)
    if id is None:
        return response.json({"errNo": 999, "data": 'id is required'})
    dream = await common_api.dream_by_id(id)
    if dream is None:
        response.json({"errNo": 0,
                       "data": {}})
    return response.json({"errNo": 0, "data": {"id": id, "prompt": dream.prompt, "img": dream.img, "messages": dream.conversations, "suggest": dream.suggest}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
