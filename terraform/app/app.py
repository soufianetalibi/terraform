def main():
    try:
        # Authentification automatique via AZURE_CREDENTIALS (GitHub Actions)
        credential = DefaultAzureCredential()

        client = SubscriptionClient(credential)

        # On essaie de récupérer au moins une subscription
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
