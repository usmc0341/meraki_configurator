import argparse
import logging
import os
import yaml
import getpass
import requests
import json
from create_target_group import create_target_group
from tag_devices import tag_devices

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler to write the log messages to a file
file_handler = logging.FileHandler("../log/meraki-configurator.log")
file_handler.setLevel(logging.DEBUG)


# Create a console handler to print the log messages to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter for the log messages
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add the formatter to the file handler and console handler
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the file handler and console handler to the logger object
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Set up the argument parser
parser = argparse.ArgumentParser(description="Create a new target group in Meraki and add a tag to a list of devices.")
parser.add_argument("--create-group", action="store_true", help="Create a new target group.")
parser.add_argument("--tag-devices", metavar="device_list_file", help="Add a tag to a list of devices.")
parser.add_argument("--tag-name", metavar="tag_name", help="The name of the tag to add to the devices.")
args = parser.parse_args()


# Define the main function for the script
def main():
    """
    The main function for the Meraki tagger script.

    This function prompts the user to create/update the configuration file and then prompts the user to choose
    an action to perform (create a target group or add a tag to devices). The function calls the appropriate function
    based on the user's selection.
    """
    # Check if the configuration file exists and prompt the user to create/update it if necessary
    config_path = os.path.join(os.path.dirname(__file__), "../data/config/default.yaml")
    if not os.path.exists(config_path):
        print("The configuration file is missing. Please create a new configuration file with your Meraki API key and network ID.")
        api_key = getpass.getpass("Meraki API key: ")
        network_id = input("Meraki network ID: ")
        config = {
            "meraki": {
                "api_key": api_key,
                "network_id": network_id
            }
        }
        with open(config_path, "w") as f:
            yaml.dump(config, f)
    else:
        with open(config_path) as f:
            config = yaml.safe_load(f)
        if config["meraki"]["api_key"] == "YOUR_API_KEY" or config["meraki"]["network_id"] == "YOUR_NETWORK_ID":
            print("The configuration file contains default values. Please update the configuration file with your Meraki API key and network ID.")
            api_key = getpass.getpass("Meraki API key: ")
            network_id = input("Meraki network ID: ")
            config["meraki"]["api_key"] = api_key
            config["meraki"]["network_id"] = network_id
            with open(config_path, "w") as f:
                yaml.dump(config, f)
        else:
            api_key = config["meraki"]["api_key"]
            network_id = config["meraki"]["network_id"]

    # Prompt the user to choose an action to perform
    action = input("What action do you want to perform? (1 = create target group, 2 = add tag to devices): ")
    if action == "1":
        # Prompt the user for the name of the target group to create
        target_group_name = input("Enter the name of the target group to create (default: SentinelOneTargets): ") or "SentinelOneTargets"
        scope = "withAny, SentinelOneTarget"
        tags = "SentinelOneTarget"
        create_target_group(api_key, network_id, target_group_name, scope, tags)
    elif action == "2":
        device_list_path = input("Enter the path to the file containing the list of devices: ")
        tag_name = input("Enter the name of the tag to add (default: SentinelOneTarget): ") or "SentinelOneTarget"
        tag_devices(api_key, network_id, device_list_path, tag_name)
    else:
        print("Invalid action selected. Please choose 1 or 2.")

if __name__ == "__main__":
    main()