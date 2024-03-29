import threading
import time

from NatNetSDK.NatNetClient import NatNetClient


def receive_rigid_body_frame(new_id, position, rotation):
    print(new_id)


def opti_setup():
    optitrack_client = NatNetClient()
    optitrack_client.set_client_address("133.68.108.74")
    optitrack_client.set_server_address("133.68.108.109")
    optitrack_client.rigid_body_listener = receive_rigid_body_frame
    optitrack_client.run()


if __name__ == "__main__":
    opti_thr = threading.Thread(target=opti_setup, daemon=True).start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
