from database.supabd import supabase
from flask import jsonify

def get_fields():
    data = supabase.table("Field").select("*").execute()
    data = data.__dict__
    return data['data']

def get_field_by_id(field_id):
    data = supabase.table("Field").select('*').eq('id', field_id).execute()
    data = data.__dict__
    return data['data'][0]

def get_field_by_name(field_name):
    data = supabase.table("Field").select('*').eq('field', field_name).execute()
    data = data.__dict__
    return data['data'][0]

def create_field(field):
    data = supabase.table("Field").insert({"field":field}).execute()
    data = data.__dict__
    return data['data'][0]['id']

def update_field(id, field):
    data = supabase.table("Field").update({"field": field}).eq('id', id).execute()
    data = data.__dict__
    return data['data'][0]['id']

def delete_field(field_id):
    data = supabase.table("Field").delete().eq("id", field_id).execute()
    data = data.__dict__
    return data['data'][0]

if __name__ == '__main__':
    pass