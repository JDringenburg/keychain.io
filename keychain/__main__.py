import os

from keychain.app import app

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
