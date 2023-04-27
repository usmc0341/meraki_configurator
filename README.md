<<<<<<< HEAD
# Meraki Configurator

A Python project to help set up a deployment configuration in Meraki SM.

## Project Structure

meraki-configurator/
    src/
        __init__.py
        main.py
        create_target_group.py
        tag_devices.py
    data/
        config/
            __init__.py
            default.yaml
    log/
        meraki_configurator.log
    requirements.txt
README.md

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/meraki-configurator.git

2. Change directory to the cloned repository:

   cd meraki-configurator

3. Install the required packages:

   pip install -r requirements.txt

## Usage

1. Set up the configuration file:

   Update the `data/config/default.yaml` with your Meraki API key and network ID.

   **Note:** You can also use environment variables to store your Meraki API key and network ID, to avoid storing sensitive data in the repository.

2. Run the script:

   python src/meraki-configurator.py

   Follow the prompts to create a new target group or add a tag to devices.

## Functions

- `create_target_group(api_key: str, network_id: str, target_group_name: str, scope: str, tags: str) -> bool`:

  Creates a new target group in the specified Meraki network with the given name, scope, and tags.

- `tag_devices(api_key: str, network_id: str, device_list_path: str, tag_name: str) -> bool`:

  Adds a tag to a list of devices in the specified Meraki network.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
=======
# meraki_configurator
>>>>>>> origin/main
