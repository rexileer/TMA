from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = fields.BigIntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    name = fields.CharField(max_length=64)
    
    class Meta:
        table = "users"
        

UserSchema = pydantic_model_creator(User)