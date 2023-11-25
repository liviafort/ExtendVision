from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

class SupabaseSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            # "Inicialize a conexão Supabase aqui"
            url = os.environ.get("SUPABASE_URL")
            key = os.environ.get("SUPABASE_KEY")
            cls._instance.supabase = create_client(url, key)
        return cls._instance