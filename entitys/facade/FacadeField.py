from entitys.facade.Facade import Facade


class FacadeField(Facade):
    def get_fields(self):
        data = self.supabase_singleton.supabase.table("Field").select("*").execute()
        data = data.__dict__
        return data['data']

    def get_field_by_id(self, field_id):
        data = self.supabase_singleton.supabase.table("Field").select('*').eq('id', field_id).execute()
        data = data.__dict__
        return data['data'][0]

    def get_field_by_name(self, field_name):
        data = self.supabase_singleton.supabase.table("Field").select('*').eq('field', field_name).execute()
        data = data.__dict__
        return data['data'][0]

    def create_field(self, field):
        data = self.supabase_singleton.supabase.table("Field").insert({"field":field}).execute()
        data = data.__dict__
        return data['data'][0]['id']

    def update_field(self, id, field):
        data = self.supabase_singleton.supabase.table("Field").update({"field": field}).eq('id', id).execute()
        data = data.__dict__
        return data['data'][0]['id']

    def delete_field(self, field_id):
        data = self.supabase_singleton.supabase.table("Field").delete().eq("id", field_id).execute()
        data = data.__dict__
        return data['data'][0]

if __name__ == '__main__':
    pass