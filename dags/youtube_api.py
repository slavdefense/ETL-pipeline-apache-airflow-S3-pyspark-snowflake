
from googleapiclient.discovery import build
import json
from dotenv import load_dotenv
load_dotenv()
import os

def extract_youtube_data():
    api_key = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.videos().list(
        part='snippet,statistics',
        chart='mostPopular',
        regionCode='US',
        maxResults=50
    )
    response = request.execute()
    print(response)
    print('hi')
    
    # Save the response to a JSON file
    with open('/Users/sagunshrestha/airflow/dags/youtube_data.json', 'w') as f:
        json.dump(response, f)

# extract_youtube_data()