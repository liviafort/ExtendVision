from entitys.singleton.SupabaseSingleton import SupabaseSingleton


class Facade:
    def __init__(self):
        self.supabase_singleton = SupabaseSingleton()
