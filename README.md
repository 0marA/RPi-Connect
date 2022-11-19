# RPi-Tuya-Control

Project based on the Tuya IOT API and a c̶u̶s̶t̶o̶m̶ ̶R̶a̶s̶p̶b̶e̶r̶r̶y̶ ̶P̶i̶ ̶s̶e̶n̶s̶o̶r̶ ̶t̶o̶ ̶a̶u̶t̶o̶m̶a̶t̶i̶c̶a̶l̶l̶y̶ ̶t̶u̶r̶n̶ ̶o̶n̶ ̶t̶h̶e̶ ̶t̶u̶y̶a̶ ̶s̶m̶a̶r̶t̶ ̶l̶a̶m̶p̶s̶ ̶i̶n̶ ̶m̶y̶ ̶r̶o̶o̶m̶ ̶w̶h̶e̶n̶ ̶I̶ ̶w̶a̶l̶k̶ ̶i̶n̶.̶ button to turn on my smart outlet controlled lamps.

## Setup

First, follow the [guide](https://developer.tuya.com/en/demo/python-iot-development-practice) to create an IOT project on a Tuya Devoloper account, then replace the device IDs and secret keys with the ones generated for you by Tuya.


### Hardware

Wire a push button to the 3.3V and GPIO 18 pin, and then an led to a GND pin and GPIO 23. Now configure crontab by running `crontab -e` and add
`@reboot python /home/pi/*path/to/file.py*`.
