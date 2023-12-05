from entitys.bdClasses.Bd import Bd


class BdField(Bd):
    def get_fields(self):
        data = self.supabase_singleton.supabase.table("Field").select("*").execute()
        data = data.__dict__
        return data['data']

    def get_field_by_id(self, field_id):
        try:
            data = self.supabase_singleton.supabase.table("Field").select('*').eq('id', field_id).execute()
            data = data.__dict__
            data = data['data'][0]
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def get_field_by_name(self, field_name):
        try:
            data = self.supabase_singleton.supabase.table("Field").select('*').eq('field', field_name).execute()
            data = data.__dict__
            data = data['data'][0]
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def create_field(self, informations):
        data = self.supabase_singleton.supabase.table("Field").insert(informations).execute()
        data = data.__dict__
        return data['data'][0]['id']

    def update_field(self, id, informations):
        data = self.supabase_singleton.supabase.table("Field").update(informations).eq('id', id).execute()
        data = data.__dict__
        return data['data'][0]['id']

    def delete_field(self, field_id):
        data = self.supabase_singleton.supabase.table("Field").delete().eq("id", field_id).execute()
        data = data.__dict__
        return data['data'][0]


if __name__ == '__main__':
    pass