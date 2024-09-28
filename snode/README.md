# Scripts for interfacing with the SNode
This folder hosts a poetry environment to interface with the SNodes.
The current scripts are:
1. [Python] `read_aqi.py` which listens for any nodes that are logging smoke, environmental, etc. data
2. [Bash] `traceroute_test.sh` which uses the meshtastic CLI to request a network path between notes


# Flashing a SNode
Build the firmware.
Then configure using

```
poetry run python -m meshtastic \
--set lora.region US \
--set telemetry.device_update_interval 1800 \
--set telemetry.environment_display_fahrenheit true \
--set telemetry.environment_measurement_enabled true \
--set telemetry.environment_screen_enabled true \
--set telemetry.environment_update_interval 20 \
--set telemetry.air_quality_enabled true \
--set telemetry.air_quality_interval 60 \
--set telemetry.power_measurement_enabled true \
--set telemetry.power_screen_enabled true \
--set telemetry.power_update_interval 20
```