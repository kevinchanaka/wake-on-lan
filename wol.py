import socket
import sys
import os 
import ipaddress
import re

MAC_ADDR = os.environ["MAC"]
BROADCAST_ADDR = os.environ["BROADCAST"]
UDP_PORT = 9


def isValidBroadcast(ip):
    try:
        ip = ipaddress.ip_address(BROADCAST_ADDR)
    except ValueError:
        return False 
    if(ip.is_private == False):
        return False 
    return True


def isValidMac(mac):
    if not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        return False 
    return True


def createPayload(mac):
    payload = b"\xff" * 6
    macJoin = "".join(mac.lower().split(":"))
    macBytes = bytes.fromhex(macJoin)
    return payload + (macBytes * 16)


if not isValidBroadcast(BROADCAST_ADDR):
    print("BROADCAST_ADDR {} is not a valid private IPv4 address".format(BROADCAST_ADDR))
    sys.exit(1)


if not isValidMac(MAC_ADDR):
    print("MAC_ADDR {} is not a valid MAC address".format(MAC_ADDR))
    sys.exit(1)


with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    payload = createPayload(MAC_ADDR)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(payload, (BROADCAST_ADDR, UDP_PORT))
    s.close()
    print("Sent wake on LAN packet - MAC {} - Broadcast address {}".format(MAC_ADDR, BROADCAST_ADDR))