## Overview ##

Very simple container that broadcasts a wake on LAN packet. Ideal for running on docker hosts or kubernetes clusters

## Usage ##
```docker run --rm -d -e MAC=aa:bb:cc:dd:ee:ff -e BROADCAST=192.168.0.1 kevinchanaka/wake-on-lan```<br />
Replace MAC and BROADCAST variables with the relevant values for your target PC and network