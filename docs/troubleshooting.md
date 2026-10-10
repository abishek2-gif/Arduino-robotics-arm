# Troubleshooting
| Symptom | Checks and action |
|---|---|
| Upload fails | Select Uno and the correct port; use a data-capable USB cable; close other software using the port |
| Servo.h missing | Install the official Arduino Servo library through Library Manager |
| No servo motion | Check external power, polarity, common ground, signal pin and connector pinout |
| Jitter or resets | Measure supply voltage under load; check current capacity, loose grounds, interference and mechanical binding |
| Motion with released joystick | Check analog wiring and measured centre values; adjust deadzone/centres |
| Wrong axis moves | Compare A0–A3 and D3/D5/D6/D9 wiring with wiring.md |
| Reversed movement | Reverse that axis's analog input as described in calibration.md |
| Buzzing or overheating | Disconnect servo power while supporting the arm; check obstruction, overload and commanded limits |
| Sudden motion on startup | Check initial angle variables and horn mounting; calibrate unloaded |
| Arm falls when power is off | Support it before disconnecting; assess mechanical support and load |
| Animation opens as code on GitHub | Download the HTML file and open locally in a browser |
| Camera does not control the arm | Camera/serial control is planned and not implemented in the current joystick firmware |

Change one factor at a time and record the result. Do not assume every jitter problem is caused by the power supply.

Reference: [Arduino servo troubleshooting](https://support.arduino.cc/hc/en-us/articles/360017053760-Troubleshoot-servo-motors).
