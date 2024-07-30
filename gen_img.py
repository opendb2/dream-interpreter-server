import civitai
import util.bucket as bucket

txt2img_promote = "RAW photo, face portrait photo of woman, wearing black dress, happy face, hard shadows, cinematic shot, dramatic lighting"

async def txt2img(model, promote=txt2img_promote):
    img_url = ""
    input = {
        "model": "urn:air:sdxl:checkpoint:civitai:101055@128078",
        "params": {
            "prompt": promote,
            "negativePrompt": "(deformed, distorted, disfigured:1.3)",
            "scheduler": "EulerA",
            "steps": 20,
            "cfgScale": 7,
            "width": 768,
            "height": 512,
            "seed": -1,
            "clipSkip": 1
        },
    }

    response = await civitai.image.create(input, wait=True)
    job_token = response['token']
    job_id = response['jobs'][0]['jobId']

    # Retrieve job status and image
    img_response = await civitai.jobs.get(token=job_token, job_id=job_id)
    print("Job Status Response:", img_response)
    image_url = ""
    if img_response['jobs'][0]['result'].get('available'):
        image_url = img_response['jobs'][0]['result'].get('blobUrl')
        if image_url:
            print("image_url:", image_url)
        else:
            print("Image URL not found in the job result.")
    else:
        print("No image was created, the job is not yet complete, or the result is not available.")
    print('response:', img_response)
    # 将 img 上传到 cos，返回 cos link
    res = await bucket.img2bucket(image_url)
    return bucket.assembl_cos_file_url(res.get("file_name", None))
