import requests
import logging

logger = logging.getLogger(__name__)

def create_target_group(api_key, network_id, target_group_name, scope, tags):
    """
    Creates a new target group in the specified Meraki network with the given name, scope, and tags.

    :param api_key: Meraki API key.
    :param network_id: Meraki network ID.
    :param target_group_name: The name of the target group to create.
    :param scope: The scope for the target group.
    :param tags: The tags for the target group.
    """
    url = f"https://api.meraki.com/api/v1/networks/{network_id}/sm/targetGroups"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    payload = {
        "name": target_group_name,
        "scope": scope,
        "tags": tags
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        logger.info("New target group created.")
    else:
        logger.error(f"Error creating new target group: {response.text}")
