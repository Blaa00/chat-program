radio.onReceivedString(function (receivedString) {
    serial.writeLine(receivedString)
})
radio.setGroup(10)
basic.forever(function () {
    radio.sendString(serial.readLine())
})
