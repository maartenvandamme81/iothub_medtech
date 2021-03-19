import random
import params
import time
from iothub_client_init import iothub_client_init
from azure.iot.device import IoTHubDeviceClient, Message


def iothub_med_normal_temp():
    try:
        client = iothub_client_init()

        while True:
            # Build the message with simulated telemetry values.
            temperature = random.uniform(params.normal_temp_min, params.normal_temp_max)
            heartbeat = random.uniform(params.normal_heartbeat_min, params.normal_heartbeat_max)
            oxygen = random.uniform(params.normal_oxygen_min, params.normal_oxygen_max)
            msg_txt_formatted = params.MSG_TXT.format(temperature=temperature, heartbeat=heartbeat, oxygen=oxygen)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if temperature > 40:
                message.custom_properties["temperatureAlert"] = "true"
            else:
                message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print("Sending normal_temp message: {}".format(message))
            client.send_message(message)
            time.sleep(5)

    except KeyboardInterrupt:
        pass
