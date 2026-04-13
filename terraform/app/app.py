from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import SubscriptionClient
import sys

def main():
    try:
        credential = DefaultAzureCredential()

        client = SubscriptionClient(credential)

        subs = list(client.subscriptions.list())

        if len(subs) > 0:
            print("✅ Accès à Azure OK")
        else:
            print("⚠️ Connecté mais aucune subscription trouvée")

    except Exception as e:
        print(f"❌ Erreur d'authentification Azure: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
