from telethon.sync import TelegramClient
from telethon.errors import UsernameNotOccupiedError

# Substitua com seu api_id e api_hash
api_id = 
api_hash = ''

with TelegramClient('session_name', api_id, api_hash) as client:
    while True:
        username = input("\nEnter the person's @username: ").strip()

        # Remove o @ se tiver
        if username.startswith('@'):
            username = username[1:]

        try:
            user = client.get_entity(username)
            print("\n--- Result ---")
            print(f"Username: @{user.username}")
            print(f"Name: {user.first_name}")
            print(f"ID: {user.id}")
            print("------------------")
        except UsernameNotOccupiedError:
            print(f"\n❌ Ninguém está usando o username @{username}")
        except Exception as e:
            print(f"\n⚠️ Ocorreu um erro inesperado:\n{e}")
