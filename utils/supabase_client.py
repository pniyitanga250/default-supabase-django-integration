from supabase import create_client, Client
from django.conf import settings

def get_supabase_client() -> Client:
    """Get Supabase client with anon key"""
    return create_client(
        settings.SUPABASE_URL, 
        settings.SUPABASE_ANON_KEY
    )

def get_supabase_admin_client() -> Client:
    """Get Supabase client with service role key for admin operations"""
    return create_client(
        settings.SUPABASE_URL, 
        settings.SUPABASE_SERVICE_ROLE_KEY
    )