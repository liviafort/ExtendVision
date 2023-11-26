from entitys.singleton.SupabaseSingleton import SupabaseSingleton


class Bd:
    def __init__(self):
        self.supabase_singleton = SupabaseSingleton()
