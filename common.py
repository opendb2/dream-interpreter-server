import orm.mysql_models as db_models
from playhouse.shortcuts import model_to_dict
import json

async def share_create(prompt="", img="", messages=[], suggest="", dream_id=0):
    db_models.db.connect()
    id = None
    try:
        share_dream = db_models.Dream_Share.create()
        share_dream.prompt = prompt
        share_dream.img = img
        share_dream.conversations = json.dumps(messages)
        share_dream.suggest = suggest
        share_dream.dream_id = dream_id
        share_dream.save()
        id = share_dream.id
    except:
        print('share_view_save:error')
    db_models.db.close()
    return id

async def share_view_by_id(id = 1):
    db_models.db.connect()
    try:
        res = db_models.Dream_Share.get_by_id(id)
    except:
        res = None
    print('res.prompt:', res.prompt)
    db_models.db.close()
    return res

async def share_list():
    db_models.db.connect()
    res_list = []
    query  = db_models.Dream_Share.select().where(id != 0).order_by(db_models.Dream_Share.share_date.desc())
    results = list(query)
    print('share_list:select results:', results)
    for cur in results:
        # res_list.append(model_to_dict(cur))
        res_list.append({"id": cur.id, "prompt": cur.prompt, "img": cur.img, "conversations": cur.conversations, "suggest": cur.suggest, "dream_id": cur.dream_id})
    db_models.db.close()
    return res_list

async def dream_update(id, prompt="", img="", messages=[], suggest=""):
    print('dream_update:id:', id)
    print('dream_update:id is None:', id is None)
    if id is None:
        return await dream_save(prompt, img, messages, suggest)
    db_models.db.connect()
    curId = ''
    try:
        dream = db_models.Dream.get_by_id(id)
        if prompt != "":
            dream.prompt = prompt
        if img != "":
            dream.img = img
        if messages != "":
            dream.conversations = messages
        if suggest != "":
            dream.suggest = suggest
        dream.save()
        print('dream_update:save:success')
        curId = dream.id
    except:
        print('dream_update:error')
    db_models.db.close()
    return curId

async def dream_save(prompt="", img="", messages=[], suggest=""):
    print('dream_save:messages:', messages)
    db_models.db.connect()
    id = None
    try:
        dream = db_models.Dream.create()
        dream.prompt = prompt
        dream.img = img
        dream.conversations = json.dumps(messages)
        dream.suggest = suggest
        dream.save()
        print('dream_save:id:', dream.id)
        print('dream_save:prompt:', dream.prompt)
        id = dream.id
    except Exception as e:
        print('dream_save:error:', e.args)
    db_models.db.close()
    return id

async def dream_by_id(id = 1):
    db_models.db.connect()
    try:
        res = db_models.Dream.get_by_id(id)
    except:
        res = None
    print('res.prompt:', res.prompt)
    db_models.db.close()
    return res







