import requests
import logging
import readline

logger = logging.getLogger(__name__)


def tag_devices(api_key, network_id, device_list_path, tag_name):
    """
    Adds a tag to a list of devices in the specified Meraki network.

    :param api_key: Meraki API key.
    :param network_id: Meraki network ID.
    :param device_list_path: Path to a text file containing a list of device serial numbers or MAC addresses.
    :param tag_name: The name of the tag to add to the devices.
    """
    with open(device_list_path, "r") as f:
        devices = [line.strip() for line in f]

    if len(devices[0]) > 12:
        device_type = "wifiMacs"
    else:
        device_type = "serials"

    url = f"https://api.meraki.com/api/v0/networks/{network_id}/sm/devices/tags"

    confirm = input(f"Do you want to add the tag '{tag_name}' to {len(devices)} devices? (y/n) ")
    if confirm.lower() != "y":
        logger.info("Aborted tag addition.")
        return

    for device in devices:
        payload = {
            "updateAction": "add",
            "tags": tag_name,
            device_type: device
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": api_key
        }
        response = requests.put(url, headers=headers, json=payload)
        if response.status_code == 200:
                print(f"Tag '{tag_name}' added to device {device}.")
                success = f"Tag '{tag_name}' added to device {device}."
        else:
            print(f"Error adding tag to device {device}. Status code: {response.status_code}, Response: {response.text}")
            success = False


    return success