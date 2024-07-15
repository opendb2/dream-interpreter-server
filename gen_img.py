import civitai
import os

async def txt2img(account_info, params):
    input = {
        "model": "urn:air:sdxl:checkpoint:civitai:101055@128078",
        "params": {
            "prompt": "RAW photo, face portrait photo of woman, wearing black dress, happy face, hard shadows, cinematic shot, dramatic lighting",
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

    if img_response['jobs'][0]['result'].get('available'):
        image_url = img_response['jobs'][0]['result'].get('blobUrl')
        if image_url:
            print("image_url:", image_url)
        else:
            print("Image URL not found in the job result.")
    else:
        print("No image was created, the job is not yet complete, or the result is not available.")
    print('response:', img_response)
    return img_response
