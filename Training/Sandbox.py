import requests

base_url = 'https://api.everlaw.com.au/v1/'
endpoint = 'projects'
everlaw_api_token = 'Bearer everlaw-api.CVS3IVAC.PRYFORAIYHNEDFCHJOP7QJN7C7FNVCY7RA7RUNXYN7H6WDM6'
headers = {'Authorization': everlaw_api_token}
search_endpoint = f'/search/{x}'

#Begin data retreaval and orginization from API
# Function for requesting all projects in Everlaw
def main_requst(base_url, endpoint):
    r = requests.get(base_url + endpoint, headers=headers)
    return r.json()

# retrieves project id's from main list of projects.  Creates a list of all the id's to be used in the project_request
def project_ids(response):
    ids = []
    for item in response['data']:
        ids.append(item['id'])
    return ids

#variable to use for basic project request
main_get_data = main_requst(base_url=base_url, endpoint=endpoint)

