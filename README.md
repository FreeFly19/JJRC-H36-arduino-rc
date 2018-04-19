# nrf24_JJRC_H36_pc

This branch includes the files for Visual Studio 2015+ in conjunction with the excellent [Visual Micro](http://www.visualmicro.com/) - the fully compatible Arduino programming tool for Microsoft Visual Studio. 

## Overview

This is a fork of [perrytsao/nrf24_cx10_pc](https://github.com/perrytsao/nrf24_cx10_pc). This code has been updated with the latest drone support from [goebish/nrf24_multipro](https://github.com/goebish/nrf24_multipro). 

[goebish/nrf24_multipro](https://github.com/goebish/nrf24_multipro) was modified by [perrytsao/nrf24_cx10_pc](https://github.com/perrytsao/nrf24_cx10_pc) to allow input to control a drone through a serial port instead of PPM signals from a transmitter. This code will always select the JJRC H36 mini protocol for operation, but the code for using other drones is still intact so it should be easy to modify for those who are interested.  

## Usage

In order to use this code, you will need an Arduino, nrF24L01+ wireless cards, two resistors, one green, one red LED and a JJRC H36 mini drone. This webpage has a [list of hardware needed](http://www.makehardware.com/2016/04/24/teach-your-pc-to-fly-a-mini-drone/). The Arduino and the wireless cards should be wired following this table:

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


## Drones

### Change drone support in code

To change the drone selected by the code, edit the selectProtocol() method in nRF24_multipro.ino and replace PROTO_E010 with the drone  of your choice - the enum is defined at the top of the file.

### Supported drones

	- WLToys V2x2, JXD JD38x, JD39x, JJRC H6C, Yizhan Tarantula X6
	- EAchine CG023, CG032, 3D X4
	- Cheerson CX-10 blue board, newer red board, CX-10A, CX-10C, Floureon FX-10, CX-Stars (todo: add DM007 variant)
	- Cheerson CX-10 green board
	- EAchine H7, MoonTop M99xx
	- EAchine H8(C) mini, H10, BayangToys X6, X7, X9, JJRC JJ850, Floureon H101
	- Syma X5C-1 (not older X5C), X11, X11C, X12
	- YD-829, YD-829C, YD-822 ...
	- EAchine H8 mini 3D, JJRC H20, H22
	- MJX X600 (can be changed to Weilihua WLH08, X800 or H26D)
	- Syma X5C, X2
	- HiSky RXs, HFP80, HCP80/100, FBL70/80/90/100, FF120, HMX120, WLToys v933/944/955 ...
	- KN (WLToys variant) V930/931/939/966/977/988
	- Cheerson CX-10 red (older version)/CX11/CX205/CX30, JXD389/390/391/393, SH6057/6043/6044/6046/6047, FY326Q7, WLToys v252 Pro/v343, XinXun X28/X30/X33/X39/X40
	- FQ777-124 pocket drone
	- EAchine E010, NiHui NH-010, JJRC H36 mini
	- Bayang for Silverware with frsky telemetry


## Build notes

This sketch was tested with Arduino version 1.6.7.  nRF24_multipro.ino is the top-level code.  

The python script serial_test.py can be used to test the connection, although it's not really practical for flying.  


## Additional comments

This code was originally developed by [perrytsao/nrf24_cx10_pc](https://github.com/perrytsao/nrf24_cx10_pc) as part of the [Teach your PC to Fly a Mini-Drone](http://www.makehardware.com/2016/04/24/teach-your-pc-to-fly-a-mini-drone/) project on [MakeHardware.com](www.makehardware.com).


