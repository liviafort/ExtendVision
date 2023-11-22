from database.supabd import supabase
from flask import jsonify

def get_project_students():
    data = supabase.table("ProjectStudents").select("*").execute()
    data = data.__dict__
    return data['data']

def get_ps_by_user(id):
    data = supabase.table("ProjectStudents").select('*').eq('id_user', id).execute()
    data = data.__dict__
    return data['data']

def get_ps_by_project(id):
    data = supabase.table("ProjectStudents").select("*").eq('id_project', id).execute()
    data = data.__dict__
    return data['data']

def create_project_student(id_project, id_user):
    data = supabase.table("ProjectStudents").insert({'id_project': id_project, 'id_user': id_user}).execute()
    data = data.__dict__
    return (data['data'][0]['id_project'], data['data'][0]['id_user'])

def update_project_students(old_id_project, old_id_user, id_project, id_user):
    data = supabase.table("ProjectStudents").update({'id_project': id_project,'id_user': id_user}).match({'id_project': old_id_project,'id_user':old_id_user}).execute()
    data = data.__dict__
    return (data['data'][0]['id_project'], data['data'][0]['id_user'])

def delete_project_students(id_project, id_user):
    data = supabase.table("ProjectStudents").delete().match({'id_project': id_project,'id_user':id_user}).execute()
    data = data.__dict__
    return data['data'][0]

if __name__ == '__main__':
    pass