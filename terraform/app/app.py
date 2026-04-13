from azure.identity import AzureCliCredential
import sys

def main():
    try:
        credential = AzureCliCredential()

        token = credential.get_token("https://management.azure.com/.default")

        print("✅ Auth Azure OK")

    except Exception as e:
        print(f"❌ Auth failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
