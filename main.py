# This is a sample Python script.
import init
init.init()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sanic import Sanic, response
import gen_img

init.init()
app = Sanic("Example")

@app.route("/api", methods=["POST", "PUT"])
async def test(request):
    return response.json({"test": True})

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
