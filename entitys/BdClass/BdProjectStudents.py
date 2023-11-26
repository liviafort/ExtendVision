from entitys.BdClass.Bd import Bd


class BdProjectStudents(Bd):
    def get_project_students(self):
        data = self.supabase_singleton.supabase.table("ProjectStudents").select("*").execute()
        data = data.__dict__
        return data['data']

    def get_ps_by_user(self, id):
        try:
            data = self.supabase_singleton.supabase.table("ProjectStudents").select('*').eq('id_user', id).execute()
            data = data.__dict__
            return data['data']
        except:
            return []

    def get_ps_by_project(self, id):
        data = self.supabase_singleton.supabase.table("ProjectStudents").select("*").eq('id_project', id).execute()
        data = data.__dict__
        return data['data']

    def create_project_student(self, informations):
        data = self.supabase_singleton.supabase.table("ProjectStudents").insert(informations).execute()
        data = data.__dict__
        return (data['data'][0]['id_project'], data['data'][0]['id_user'])

    def update_project_students(self, old_id_project, old_id_user, informations):
        data = self.supabase_singleton.supabase.table("ProjectStudents").update(informations).match({'id_project': old_id_project,'id_user':old_id_user}).execute()
        data = data.__dict__
        return (data['data'][0]['id_project'], data['data'][0]['id_user'])

    def delete_project_students(self, id_project, id_user):
        data = self.supabase_singleton.supabase.table("ProjectStudents").delete().match({'id_project': id_project,'id_user':id_user}).execute()
        data = data.__dict__
        return data['data'][0]

if __name__ == '__main__':
    pass