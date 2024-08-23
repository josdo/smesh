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