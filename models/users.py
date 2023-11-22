from database.supabd import supabase
from flask import jsonify

def get_user_by_id(user_id):
    data = supabase.table("User").select("*").eq("id",user_id).execute()
    data = data.__dict__
    return data['data'][0]

def get_user_by_email(user_email):
    data = supabase.table("User").select("*").eq("email",user_email).execute()
    data = data.__dict__
    return data['data'][0]

def get_users():
    data = supabase.table("User").select("*").execute()
    data = data.__dict__
    return data['data']

def create_user(registration, password, name, title, gender, birth, email):
    data = supabase.table("User").insert({'registration':registration,
        'password':password,
        'name':name,
        'title':title,
        'gender':gender,
        'birth':birth,
        'email':email}).execute()
    
    data = data.__dict__
    return data['data'][0]['id']
    
def update_user(user_id, registration, password, name, title, gender, birth, email):
    data = supabase.table("User").update({'registration':registration,
        'password':password,
        'name':name,
        'title':title,
        'gender':gender,
        'birth':birth,
        'email':email}).eq('id', user_id).execute()
    
    data = data.__dict__
    return data['data'][0]['id']

def delete_user(user_id):
    data = supabase.table("User").delete().eq("id", user_id).execute()
    data = data.__dict__
    return data['data'][0]

if __name__ == '__main__':
    pass