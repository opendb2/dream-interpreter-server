from openai import OpenAI
client = OpenAI()

async def gpt_chat(messages = []):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        # messages=[
        #     {"role": "system", "content": "你是一名职业精神分析家。请根据精神分析理论，对提供的内容进行深度解析。请首先检查用户的输入是否有明显混乱或者是恶意或恶作剧的输入，只有客户输入的信息是合理的，我们才进行解析。在输出内容中，仔细把握内容的重点和细节，进行更为具像化的分析，而不要输出空泛的大道理。请询问客户对于内容的解析是否满意。如果不满意，可继续提问，并请求确认。请在输出前考虑之前的对话历史。请以第二人称输出。输出的文风以弗洛伊德的写作风格。请同时给出 1 到 2 条建议。最后请构想 1 个后续的相关的问题，采用第一人称，引导用户继续对话。"},
        #     {"role": "user", "content": "I dreamed a unicorn."},
        # ]
        # messages=[
        #     {"role": "system", "content": "You are a helpful assistant."},
        #     {"role": "user", "content": "Who won the world series in 2020?"},
        # ]
        messages=messages
    )
    print("gpt_chat:response.choices[0].message:", response.choices[0].message.content)
    return response.choices[0].message.content