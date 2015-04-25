import usb.core
import usb.util

devices=[[0x1a81,0x1708],[0x1a81,0x220a]]
for device in devices:
    dev = usb.core.find(idVendor=device[0], idProduct=device[1])
    if dev != None:
        dev.reset()
