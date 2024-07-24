import orm.mysql_models as db_models
import json

async def share_view_save(prompt="", img="", messages=[], suggest=""):
    db_models.db.connect()
    id = None
    try:
        share_dream = db_models.Dream_Share.create()
        share_dream.prompt = prompt
        share_dream.img = img
        share_dream.messages = json.dumps(messages)
        share_dream.suggest = suggest
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

async def dream_save(prompt="", img="", messages=[], suggest=""):
    db_models.db.connect()
    id = None
    try:
        dream = db_models.Dream.create()
        dream.prompt = prompt
        dream.img = img
        dream.messages = json.dumps(messages)
        dream.suggest = suggest
        dream.save()
        id = dream.id
    except:
        print('share_view_save:error')
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







