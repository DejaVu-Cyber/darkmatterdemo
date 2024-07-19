import os
from dotenv import load_dotenv
load_dotenv("keys.env")
print(os.getenv("EMAIL_HOST_PASSWORD"))