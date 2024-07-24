from peewee import *
import datetime
from playhouse.db_url import connect

db = connect('mysql://root:guchanDabai2@sh-cynosdbmysql-grp-fl63f6xe.sql.tencentcdb.com:22902/dream_interpreter')

class BaseModel(Model):
    class Meta:
        database = db
class Dream_Share(BaseModel):
    id = AutoField()
    prompt = TextField()
    img = CharField()
    conversations = CharField()
    suggest = CharField()
    share_date = DateTimeField(default=datetime.datetime.now)