# This is a sample Python script.
import init
init.init()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sanic import Sanic, response
import gen_img

init.init()
app = Sanic("Example")

@app.route("/")
async def test(request):
    return response.json({"test": True})

@app.route("/gen-img")
async def gen2img(request):
    print("api:gen2img:")
    print(await gen_img.txt2img("",""))
    return response.json({"test": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
