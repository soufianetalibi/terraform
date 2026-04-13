from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient
import sys

def main():
    try:
        credential = DefaultAzureCredential()

        client = SubscriptionClient(credential)

        subs = list(client.subscriptions.list())

        if subs:
            print("✅ Accès Azure OK")
        else:
            print("⚠️ Aucune subscription trouvée")

    except Exception as e:
        print(f"❌ Erreur Azure: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
