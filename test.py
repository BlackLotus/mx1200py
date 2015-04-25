import usb.core
import usb.util
import binascii,time

reset=[binascii.unhexlify('06cb150010000000')]
rainb=[binascii.unhexlify('06cd080800000000')]
color=[binascii.unhexlify('06cd080100000000'), #red
            binascii.unhexlify('06cd080200000000'),#yellow
            binascii.unhexlify('06cd080300000000'),#green
            binascii.unhexlify('06cd080400000000'),#cyan
            binascii.unhexlify('06cd080500000000'),#blue
            binascii.unhexlify('06cd080600000000'),#pink
            binascii.unhexlify('06cd080700000000')]#white

# find our device
dev = usb.core.find(idVendor=0x1a81, idProduct=0x220a)
#06:cd:08:03:00:00:00:00
# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
#print dir(dev)
interface=[]
for i in range(0,2):
    if dev.is_kernel_driver_active(i) is True:
            print "Kernel driver is in use by "+str(i)
            interface.append(i)
            dev.detach_kernel_driver(i)
#print dev.get_active_configuration()
dev.set_configuration()

for i in range(0,8):
    dev.ctrl_transfer(0x21,9,0x0306,1,color[i])
    time.sleep(1)

#dev.attach_kernel_driver(0)
dev.reset()
