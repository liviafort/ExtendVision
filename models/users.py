#from database.bd import User, engine
#from sqlalchemy.orm import sessionmaker
from flask import jsonify
from database.bd2 import supabase

# Session = sessionmaker(bind=engine)
# session = Session()


def get_user_by_id(user_id):
    user = supabase.table('User').select("*").eq('id', user_id).execute()
    return user
    #user_dict = user.__dict__
    #user_dict.pop('_sa_instance_state', None)
    #return jsonify(user_dict)

def create_user(registration, password, name, title, gender, birth_date, tipe):
    data = supabase.table("User").insert({"registration":registration, "password":password, "name": name, "title":title, "gender":gender, "birth":birth_date, "type": tipe}).execute()
    return data

def update_user(user_id, registration, password, name, title, gender, birth_date, type):
    data, count = supabase.table('User').update({"registration": registration,
        "password": password,
        "name": name,
        "title": title,
        "gender": gender,
        "birth": birth_date,
        "type": type}).eq('id', user_id).execute()
    
    return data

def delete_user(user_id):
    data, count = supabase.table('User').delete().eq('id', user_id).execute()
    return data

if __name__ == '__main__':
    pass