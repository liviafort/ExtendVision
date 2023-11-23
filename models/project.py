from database.supabd import supabase
from flask import jsonify

def get_project_by_id(project_id):
    data = supabase.table("Project").select("*").eq("id",project_id).execute()
    data = data.__dict__
    return data['data'][0]

def get_projects():
    data = supabase.table("Project").select("*").execute()
    data = data.__dict__
    return data['data']

def create_project(id_professor, id_field, title, theme, description, begin_date, end_date, register_begin, register_end, workload, available_spots, scholarship):
    data = supabase.table("Project").insert({'id_professor':id_professor,
        'id_field':id_field,
        'title':title,
        'theme':theme,
        'description':description,
        'begin_date':begin_date,
        'end_date':end_date,
        'register_begin':register_begin,
        'register_end':register_end,
        'workload':workload,
        'available_spots':available_spots,
        'scholarship':scholarship}).execute()
    
    data = data.__dict__
    return data['data'][0]['id']
    
def update_project(project_id, id_professor, id_field, title, theme, description, begin_date, end_date, register_begin, register_end, workload, available_spots, scholarship):
    data = supabase.table("Project").update({'id_professor':id_professor,
        'id_field':id_field,
        'title':title,
        'theme':theme,
        'description':description,
        'begin_date':begin_date,
        'end_date':end_date,
        'register_begin':register_begin,
        'register_end':register_end,
        'workload':workload,
        'available_spots':available_spots,
        'scholarship':scholarship}).eq('id', project_id).execute()
    
    data = data.__dict__
    return data['data'][0]['id']

def delete_project(project_id):
    data = supabase.table("Project").delete().eq("id", project_id).execute()
    data = data.__dict__
    return data['data'][0]

if __name__ == '__main__':
    pass