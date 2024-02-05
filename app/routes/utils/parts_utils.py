import yaml
from bson import ObjectId

from app.config.setup import client
from app.models.part import Part

def parse_key(key: str) -> str:
    location_keys = ['warehouse', 'room', 'bookcase', 'shelf', 'cuvette', 'column', 'row']
    return 'location.' + key if key in location_keys else key


def parse_value(value: str) -> str | int | float:
    return yaml.safe_load(value)
    

def check_if_correct_category(part: Part):
    '''
    Category can't be empty
    Can't add a part to base category
    '''
    if part.category.split() == '':
        raise Exception(f"Category cannot be empty.")

    base_categories = client.konrad_borowik.categories.find(
        {'parent_name': ''}
    )
    for bc in base_categories:
        if part.category == bc['name']:
            raise Exception(f"Cannot assign part to base category '{part.category}'.")
        

def check_if_correct_part_id(id: ObjectId):
    if not client.konrad_borowik.parts.find_one_and_delete({"_id": ObjectId(id)}):
        raise Exception(f"Part id not in database")