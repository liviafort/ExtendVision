from entitys.bdClasses.Bd import Bd


class BdRegister(Bd):
    def get_user_by_token(self, token):
        try:
            data = self.supabase_singleton.supabase.table("RegisterData").select("*").eq("token", token).execute()
            data = data.__dict__
            return data['data'][0]
        except:
            return {}
        
    def get_user_by_email(self, email):
        try:
            data = self.supabase_singleton.supabase.table("RegisterData").select("*").eq("email", email).execute()
            data = data.__dict__
            return data['data'][0]
        except:
            return {}

    def get_register(self):
        try:
            data = self.supabase_singleton.supabase.table("RegisterData").select("*").execute()
            data = data.__dict__
            return data['data']
        except:
            return []

    def create_register(self, data):
        try:
            data = self.supabase_singleton.supabase.table("RegisterData").insert(data).execute()
            data = data.__dict__
            return data['data'][0]['id']
        except:
            return None

    def delete_register(self, token):
        try:
            data = self.supabase_singleton.supabase.table("RegisterData").delete().eq("token", token).execute()
            data = data.__dict__
            return data['data'][0]
        except:
            return {}

if __name__ == '__main__':
    pass