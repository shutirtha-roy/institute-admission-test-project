import os
from datetime import datetime
from uuid import uuid4
import asyncio
from functools import wraps, partial
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


BASE62_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
TEST = False

def create_response(success: bool, message: str, status_code: int, **kwargs):
    return JSONResponse(status_code=status_code, content={'success': success, 'message': message, **jsonable_encoder(kwargs)})


def create_updated_fields(update_body: BaseModel | dict | None):
    update_fields = {}
    if type(update_body) == dict:
        update_fields = update_body
    elif update_body is not None:
        update_fields = update_body.dict(exclude_none=True, exclude_unset=True)
    update_fields['updated_at'] = datetime.utcnow()
    return update_fields


def create_update_doc(doc: dict):
    doc['updated_at'] = datetime.now()
    return doc


def get_mongodb_name() -> str:
    return os.environ.get('MONGO_DATABASE', None)


def generate_username() -> str:
  uid = uuid4().hex
  integer_value = int(uid, 16)
  
  base62_string = ""
  while integer_value > 0:
    remainder = integer_value % 62
    base62_string = BASE62_CHARS[remainder] + base62_string
    integer_value //= 62
  
  return base62_string


def async_wrapper(func):
  @wraps(func)
  async def wrapper(*args, loop=None, executor=None, **kwargs):
    if loop is None:
      loop = asyncio.get_event_loop()
    pfunc = partial(func, *args, **kwargs)
    return await loop.run_in_executor(executor, pfunc)
  return wrapper


def number_to_letters(num_str):
    parts, i = [], 0
    while i < len(num_str):
        if i + 1 < len(num_str) and int(num_str[i:i+2]) <= 25:
            parts.append(num_str[i:i+2])
            i += 2
        else:
            parts.append(num_str[i])
            i += 1
    
    letters = [chr(int(part) + 65) for part in parts]
    return ''.join(letters).upper()


def set_test(value: bool):
    global TEST
    TEST = value

def is_test():
    return TEST
