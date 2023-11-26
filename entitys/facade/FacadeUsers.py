from entitys.facade.Facade import Facade


class FacadeUser(Facade):
    def get_user_by_id(self, user_id):
        data = self.supabase_singleton.supabase.table("User").select("*").eq("id", user_id).execute()
        data = data.__dict__
        return data['data'][0]

    def get_user_by_email(self, user_email):
        data = self.supabase_singleton.supabase.table("User").select("*").eq("email", user_email).execute()
        data = data.__dict__
        return data['data'][0]

    def get_users(self):
        data = self.supabase_singleton.supabase.table("User").select("*").execute()
        data = data.__dict__
        return data['data']

    def create_user(self, data):
        data = self.supabase_singleton.supabase.table("User").insert(data).execute()
        data = data.__dict__
        return data['data'][0]['id']

    def update_user(self, user_id, informations):
        data = self.supabase_singleton.supabase.table("User").update(informations).eq('id', user_id).execute()

        data = data.__dict__
        return data['data'][0]['id']

    def delete_user(self, user_id):
        data = self.supabase_singleton.supabase.table("User").delete().eq("id", user_id).execute()
        data = data.__dict__
        return data['data'][0]


if __name__ == '__main__':
    pass