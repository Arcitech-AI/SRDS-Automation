import requests

# Define your API URLs
api_1_url = "https://dev.srds.ai/api/courses/retrieve-schoology-courses/?fetch=true&bypass=true"
api_2_url = "https://dev.srds.ai/api/courses/schoology-recent-logs/?per_page=10&page=2"
api_3_url = "https://dev.srds.ai/api/courses/process-schoology-course/"
api_4_url = "https://dev.srds.ai/api/courses/schoology-detail-logs/?sections_ids=7685611037&batch_id=d760ef13-dc02-448c-9f01-2c7583fcc6d1"

# Your API token
api_token = "a6d95ec174946fd134e7af227274e2c4c49ec95b"
batch_id = "d760ef13-dc02-448c-9f01-2c7583fcc6d1"


# Function to hit the API using the token
def hit_api_with_token(url, token):
    headers = {
        "Authorization": f"Token {token}",  # Using the provided token for authorization
        "Content-Type": "application/json"  # Optional: Set content type to JSON if required by API
    }

    try:
        # Sending GET request (use POST or other methods if needed)
        response = requests.get(url, headers=headers)

        # Handle different status codes
        if response.status_code == 200:
            print(f"200 OK: Success! Response from {url}: {response.json()}")
        elif response.status_code == 201:
            print(f"201 Created: Resource successfully created at {url}.")
        elif response.status_code == 400:
            print(f"400 Bad Request: The request from {url} was malformed.")
        elif response.status_code == 401:
            print(f"401 Unauthorized: Authentication failed. Check your token for {url}.")
        elif response.status_code == 403:
            print(f"403 Forbidden: You do not have permission to access {url}.")
        elif response.status_code == 404:
            print(f"404 Not Found: The resource at {url} was not found.")
        elif response.status_code == 500:
            print(f"500 Internal Server Error: Server error when hitting {url}.")
        elif response.status_code == 503:
            print(f"503 Service Unavailable: {url} is temporarily unavailable. Try again later.")
        else:
            print(f"Unexpected status code {response.status_code} received from {url}.")
    except requests.exceptions.RequestException as e:
        print(f"Error hitting {url}: {e}")


# Hit all the APIs sequentially with token authentication
hit_api_with_token(api_1_url, api_token)
hit_api_with_token(api_2_url, api_token)
hit_api_with_token(api_3_url, api_token)
hit_api_with_token(api_4_url, api_token)
