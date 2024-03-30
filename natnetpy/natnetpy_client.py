import numpy as np
from scipy.spatial.transform import Rotation

from natnetpy.NatNetSDK.NatNetClient import NatNetClient


class OptiClient:
    def __init__(self, server_address="127.0.0.1", client_address="127.0.0.1"):
        self.mocap_data = dict()

        self.natnet_client = NatNetClient()
        self.natnet_client.set_server_address(server_address)
        self.natnet_client.set_client_address(client_address)
        self.natnet_client.rigid_body_listener = self.receive_rigid_body_frame
        self.natnet_client.run()

    def receive_rigid_body_frame(self, new_id, position, rotation):
        self.mocap_data[str(new_id)] = np.array(
            [
                position[2],
                position[0],
                position[1],
                rotation[3],
                rotation[2],
                rotation[0],
                rotation[1],
            ]
        )

    def to_euler_from_quat_list(self, quat_list):
        """_summary_

        Args:
            quat_list: quaternion list [w, x, y, z]

        Returns:
            euler: roll, pitch, yaw
        """
        _r = (
            Rotation.from_quat(
                [quat_list[1], quat_list[2], quat_list[3], quat_list[0]]
            )
            .as_euler("xyz", degrees=True)
            .round(1)
        )
        return _r
