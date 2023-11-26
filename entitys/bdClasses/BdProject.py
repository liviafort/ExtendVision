from entitys.bdClasses.Bd import Bd


class BdProject(Bd):
    def get_project_by_id(self, project_id):
        data = self.supabase_singleton.supabase.table("Project").select("*").eq("id",project_id).execute()
        data = data.__dict__
        return data['data'][0]

    def get_project_by_id_professor(self, id_professor):
        try:
            data = self.supabase_singleton.supabase.table("Project").select("*").eq("id_professor", id_professor).execute()
            data = data.__dict__
            return data['data']
        except:
            return []

    def get_projects(self):
        data = self.supabase_singleton.supabase.table("Project").select("*").execute()
        data = data.__dict__
        return data['data']

    def create_project(self, data):
        data = self.supabase_singleton.supabase.table("Project").insert(data).execute()

        data = data.__dict__
        return data['data'][0]['id']

    def update_project(self, project_id, informations):
        data = self.supabase_singleton.supabase.table("Project").update(informations).eq('id', project_id).execute()

        data = data.__dict__
        return data['data'][0]['id']

    def delete_project(self, project_id):
        data = self.supabase_singleton.supabase.table("Project").delete().eq("id", project_id).execute()
        data = data.__dict__
        return data['data'][0]


if __name__ == '__main__':
    pass