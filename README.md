## Overview ##

Very simple container that broadcasts a wake on LAN packet. Ideal for running on docker hosts or kubernetes clusters


## Usage ##
```docker run --rm --network host -d -e MAC=aa:bb:cc:dd:ee:ff -e BROADCAST=192.168.0.255 kevinchanaka/wake-on-lan```<br />
Replace MAC and BROADCAST variables with the relevant values for your target PC and network<br />
The container will work on x64 and ARM devices <br />
NOTE: Host network flags is required since broadcast packet will not be routed through the docker bridge network <br />
