from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()


# Access the variables using os.getenv
mongo_url = os.getenv('MONGODB_URL_KEY')
region = os.getenv('REGION_NAME')
aws = os.getenv('AWS_ACCESS_KEY_ID_ENV_KEY')

# Use the variables in your project
print(mongo_url, region, aws)