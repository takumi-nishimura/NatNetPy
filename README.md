# natnetpy
Python client for natnet.  
Based on NatNet SDK 4.1.1, modified multicast handling.  
In addition, a wrapper has been added to simplify configuration.  
## Install
```bash
poetry add git+ssh://git@github.com:takumi-nishimura/NatNetPy.git
```
## Usage
```python
from natnetpy.NatNetClient import OptiClient

opti_client = OptiClient(
    server_address="127.0.0.1", client_address="127.0.0.1"
)

while True:
    try:
        if (len(opti_client.mocap_data.keys()) > 1):
            print(opti_client.mocap_data)
    except KeyboardInterrupt:
        opti_client.shutdown()
        break
```
