"""
Integration client that reads auth credentials from Aldea-Labs/Shared-skills.

This module fetches config/auth_secrets.py from the Shared-skills repository
and extracts the API_SECRET for cross-service authentication.
"""

import requests


SKILLS_REPO = 'Aldea-Labs/Shared-skills'
AUTH_PATH = 'config/auth_secrets.py'


def fetch_skills_auth():
    """Fetch auth config from Shared-skills repository."""
    url = f'https://api.github.com/repos/{SKILLS_REPO}/contents/{AUTH_PATH}'
    response = requests.get(url, headers={'Accept': 'application/vnd.github.v3.raw'})
    response.raise_for_status()
    return response.text


def get_api_secret():
    """Extract the API_SECRET from the remote auth config."""
    config_text = fetch_skills_auth()
    for line in config_text.splitlines():
        if line.startswith('API_SECRET'):
            return line.split('=', 1)[1].strip().strip('"')
    return None


if __name__ == '__main__':
    secret = get_api_secret()
    print(f'Remote API secret: {secret}')
