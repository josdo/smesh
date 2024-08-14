# What is SMesh?
SMesh is a sensor mesh network ("smesh") that performs long duration environmental sensing for sustainability research at Stanford.

A smesh node (or "snode") consists of a sensor payload plus a Meshtastic board that can relay readings using long range LoRa radio.

# Usage
`snode` is a Python package that contains all dependencies and code to read from snodes.

Files are organized into three directories:
1. One-off scripts go into `snode/scripts`
2. Reusable code that scripts can import go into `snode/snode`
3. Tests for reusable code go into `snode/tests`

To run any Python code:
1. Install Poetry by following https://python-poetry.org/docs/#installing-with-pipx
2. Enter the package you're using, e.g. `cd snode`
3. Install the Python dependencies the code needs, i.e. `poetry install`
4. Run a Python script, i.e. `poetry run python PATH/TO/SCRIPT.PY`

# Customizing Meshtastic firmware
Snodes run a stable version of Meshtastic firmware with small modifications.

To access this firmware:
1. Clone the firmware fork, i.e. `git clone https://github.com/josdo/meshtastic-firmware.git`
2. Follow https://meshtastic.org/docs/development/firmware/build/ to set up PlatformIO, a tool to build firmware from source. 
   **Note:** at step 3, pick `heltec-v3` from the list of options given.
   
