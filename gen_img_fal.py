import fal_client
import util.bucket as bucket

async def txt2img(promote="a cat on the talbe"):
    handler = fal_client.submit(
        "fal-ai/flux/schnell",
        arguments={
            "prompt": promote
        },
    )

    result = handler.get()
    print(result)
    image_url = result['images'][0]['url']
    res = await bucket.img2bucket(image_url)
    return bucket.assembl_cos_file_url(res.get("file_name", None))
