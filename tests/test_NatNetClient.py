import time

import numpy as np
from pyquaternion import Quaternion

from natnetpy.NatNetClient import OptiClient

fps = 240
opti_client = OptiClient(
    server_address="127.0.0.1", client_address="127.0.0.1"
)

init_pose = None
relative_pos = dict()
relative_rot = dict()
rigid_body_id = "1"
np.set_printoptions(precision=3)

while True:
    try:
        start_time = time.perf_counter()
        if len(opti_client.mocap_data.keys()) > 1:
            if init_pose:
                relative_pos[rigid_body_id] = (
                    opti_client.mocap_data[rigid_body_id][:3]
                    - init_pose[rigid_body_id][:3]
                )
                relative_rot[rigid_body_id] = (
                    Quaternion([1.0, 0.0, 0.0, 0.0])
                    * Quaternion(init_pose[rigid_body_id][3:]).inverse
                    * Quaternion(opti_client.mocap_data[rigid_body_id][3:])
                )
                print(f"Relative Pos: {relative_pos[rigid_body_id]}, Relative Rot: {opti_client.to_euler_from_quat_list(
                        list(relative_rot[rigid_body_id])
                    )}")
            else:
                init_pose = dict()
                init_pose[rigid_body_id] = opti_client.mocap_data[
                    rigid_body_id
                ]
        dt = time.perf_counter() - start_time
        if dt < 1 / fps:
            time.sleep(1 / fps - dt)
    except KeyboardInterrupt:
        opti_client.natnet_client.shutdown()
        break
