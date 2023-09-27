import bec

public_key, private_key = bec.generateKeyPair(random.randint(50, 80))

connected = False

while !connected:
    radio.send_string(public_key)
    basic.pause(1000)

def on_received_string(receivedString):
    if !connected:
        if bec.decryptString(receivedString, private_key):
            connected = True
        radio.send_string(bec.encryptString(receivedString, receivedString))
        return
    serial.write_line(receivedString)
radio.on_received_string(on_received_string)

radio.set_group(10)

def on_forever():
    radio.send_string(serial.read_line())
basic.forever(on_forever)
