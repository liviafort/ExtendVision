from entitys.bdClasses.Bd import Bd


class BdUser(Bd):
    def get_user_by_id(self, user_id):
        try:
            data = self.supabase_singleton.supabase.table("User").select("*").eq("id", user_id).execute()
            data = data.__dict__
            data = data['data'][0]
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def get_user_by_email(self, user_email):
        try:
            data = self.supabase_singleton.supabase.table("User").select("*").eq("email", user_email).execute()
            data = data.__dict__
            data = data['data'][0]
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def get_users(self):
        try:
            data = self.supabase_singleton.supabase.table("User").select("*").execute()
            data = data.__dict__
            data = data['data']
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

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