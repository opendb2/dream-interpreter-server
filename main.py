# This is a sample Python script.
import init
init.init()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sanic import Sanic, response
import gen_img
import gen_txt_tencent

init.init()
app = Sanic("Example")

@app.route("/api/test-img", methods=["POST", "GET", "PUT"])
async def test_img(request):
    return response.json({"errNo": 0, "data": {"imgUrl": 'https://blobs-temp.sfo3.digitaloceanspaces.com/C7E3144965E8CEF284ADA436DDA792C53EADE2D1D94AD35E501327BFBC785C25?X-Amz-Expires=3600&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=DO00F84RAAYEUTBJ6D9L%2F20240717%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240717T064308Z&X-Amz-SignedHeaders=host&X-Amz-Signature=5edfbc291b59245786cc7be87402325502893e62b198277877899f582da1e7bc'}})
@app.route("/api", methods=["POST", "PUT"])
async def test(request):
    return response.json({"test": True})

@app.route("/api/gen-chat", methods=["POST", "GET", "PUT"])
async def gen_chat(request):
    params = request.json
    if params["messages"] is None:
        return response.json({"errNo": 999, "data": '缺少对话信息'})
    print("gen_chat:messages:", params["messages"])
    res = await gen_txt_tencent.tencent_chat(params["messages"])
    return response.json({"errNo": 0, "data": {"suggest": res}})
@app.route("/api/gen-img", methods=["POST", "GET", "PUT"])
async def gen2img(request):
    print("api:gen2img:")
    params = request.json
    print("gen-img:params:", params, params["promote"])
    # img_url = ""
    img_url = await gen_img.txt2img("", params["promote"])
    if img_url:
        return response.json({"errNo": 0, "data": {"imgUrl": img_url}})
    return response.json({"errNo": 999, "data": {"imgUrl": ''}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
