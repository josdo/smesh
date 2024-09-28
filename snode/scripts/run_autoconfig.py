import subprocess
import json
import pprint

# TODO: put this in a .proto or .config file
# Dictionary of field-value pairs
nondefault_parameters = {
    "lora.region": "US",
    "telemetry.device_update_interval": 1800,
    "telemetry.environment_display_fahrenheit": "false",
    "telemetry.environment_measurement_enabled": "true",
    "telemetry.environment_screen_enabled": "false",
    "telemetry.environment_update_interval": 20,
    "telemetry.air_quality_enabled": "true",
    "telemetry.air_quality_interval": 20,
    "telemetry.power_measurement_enabled": "true",
    "telemetry.power_screen_enabled": "true",
    "telemetry.power_update_interval": 20,
    "lora.channel_num": 104,
    "lora.frequency_offset": 0.05, # 50 kHz
    "device.role": "CLIENT",
}

# Construct the set command list
set_command = ["poetry", "run", "python", "-m", "meshtastic"]
for field, value in nondefault_parameters.items():
    set_command.extend(["--set", field, str(value)])

# # Run the set command
# subprocess.run(set_command)

# Command to get the info
info_command = ["poetry", "run", "python", "-m", "meshtastic", "--info"]

# Run the info command and capture the output
result = subprocess.run(info_command, capture_output=True, text=True)

# Extract the current config
info_output = result.stdout
preference_raw, tail = info_output.split("Preferences: ")[1].split("Module preferences: ")
module_preference_raw, tail = tail.split("Channels:")
preference_info = json.loads(preference_raw)
module_preference_info = json.loads(module_preference_raw)
info_data = {**preference_info, **module_preference_info}

print("Current parameters")
pprint.pprint(info_data)
print()

# Function to convert snake_case to camelCase
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Verify the values
for key, expected_value in nondefault_parameters.items():
    module, field = key.split('.')
    camel_field = snake_to_camel(field)
    actual_value = info_data.get(module, {}).get(camel_field)
    if str(actual_value) == str(expected_value):
        print(f"PASS: {key}")
    else:
        print(f"FAIL: {key} (expected {expected_value}, got {actual_value})")