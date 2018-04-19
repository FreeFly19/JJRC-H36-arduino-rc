# nrf24_cx10_pc

## Overview

This is a fork of [https://github.com/perrytsao/nrf24_cx10_pc](https://github.com/perrytsao/nrf24_cx10_pc). This code has been updated with the latest code from [goebish/nrf24_multipro](https://github.com/goebish/nrf24_multipro). This updates the code with additional drone support.

[goebish/nrf24_multipro](https://github.com/goebish/nrf24_multipro) was modified by [https://github.com/perrytsao/nrf24_cx10_pc](https://github.com/perrytsao/nrf24_cx10_pc) to allow input to control a drone through a serial port instead of PPM signals from a transmitter. This code will always select the JJRC H36 mini protocol for operation, but the code for using other quadcopters is still intact so it should be easy to modify for those who are interested.  

## Usage

In order to use this code, you will need an Arduino, nrF24L01+ wireless cards, two resistors, one green & one red LED and a JJRC H36 mini drone. This webpage has a [list of hardware needed](http://www.makehardware.com/2016/04/24/teach-your-pc-to-fly-a-mini-drone/). The Arduino and the wireless cards should be wired following this table:

| Arduino Uno    | NRF24L01+ Socket Adapter Board | Wire Color            |
|----------------|--------------------------------|-----------------------|
| GND            | GND                            | Orange                |
| 5V             | VCC                            | Red                   |
| D5 (Digital 5) | CE                             | Yellow                |
| A1 (Analog 1)  | CSN                            | Green                 |
| D4 (Digital 4) | SCK                            | Blue                  |
| D3 (Digital 3) | MO (MOSI)                      | Purple                |
| A0 (Analog 0)  | MI (MISO)                      | Gray                  |
| Not Used       | IRQ                            | White                 |
| 10             | N/A                            | Resistor & red LED    |
| 11             | N/A                            | Resistor & green LED  |


This sketch was tested with Arduino version 1.6.7.  nRF24_multipro.ino is the top-level code.  

The python script serial_test.py can be used to test the connection, although it's not really practical for flying.  

This code was originally developed by [https://github.com/perrytsao/nrf24_cx10_pc](https://github.com/perrytsao/nrf24_cx10_pc) as part of the [Teach your PC to Fly a Mini-Drone](http://www.makehardware.com/2016/04/24/teach-your-pc-to-fly-a-mini-drone/) project on [MakeHardware.com](www.makehardware.com).


