# Arduino Robotic Arm
A beginner robotics project using an Arduino Uno, two joysticks and four positional servos: base, shoulder, elbow and gripper.

**Status:** starter firmware and a browser concept animation are available. Physical assembly, calibration, compile/upload verification and hardware testing have not been confirmed. Camera tracking and automatic pick-and-place on hardware are planned.

## Start here
1. Review the [components](docs/components.md) and choose servos suitable for your frame and load.
2. Follow the [wiring guide](docs/wiring.md) and [diagram](docs/circuit-diagram.svg).
3. Read [assembly](docs/assembly.md) and [calibration](docs/calibration.md) before powering the assembled arm.
4. Open [robotic_arm_joystick.ino](arduino/robotic_arm_joystick/robotic_arm_joystick.ino) in Arduino IDE. Keep the sketch in its matching folder.
5. Install the official Arduino Servo library if it is missing. Select Arduino Uno and the connected USB port, then Verify and Upload with servo power off.
6. Test one unloaded servo first, then record results in the [test checklist](docs/testing.md).

## Controls and connections
| Axis | Joystick input | Servo signal | Example code limits |
|---|---|---|---|
| Base | Joystick 1 VRx → A0 | D3 | 0–180° |
| Shoulder | Joystick 1 VRy → A1 | D5 | 25–155° |
| Elbow | Joystick 2 VRx → A2 | D6 | 20–160° |
| Gripper | Joystick 2 VRy → A3 | D9 | 45–120° |

These are example software limits, **not verified safe limits for your arm**. All axes start at 90°. Calibrate with horns detached before mounting.

Joystick deflection changes angle in 2° steps about every 20 ms; releasing the joystick holds the commanded angle. This is fixed-speed incremental control, not proportional positioning.

Power the Uno by USB and the joystick modules from Uno 5V/GND. Power servos from a separate regulated supply matching their ratings; join grounds. Do not connect the servo supply positive rail to Uno 5V.

## Animated explainer video
[Watch or download the 64-second MP4](media/robotic-arm-explainer.mp4) — 720p, 24 fps, with on-screen explanations (no audio). Shows each joint, joystick controls, power/control flow and a simulated pick-and-place sequence. This is animated simulation, not hardware test footage. [Chapters and regeneration instructions](docs/video.md).

## Browser demonstration
Download [robotic-arm-showcase.html](robotic-arm-showcase.html) and open it in a modern browser. It contains play/pause, reset and four angle sliders. GitHub's file view displays the source; download it to run it.

This is an illustrative animation, not a calibrated physics simulation. Base rotation is shown by a dial, and the example serial readout does not send commands. The joystick firmware does not accept serial or camera commands.

## Documentation
- [Components and selection worksheet](docs/components.md)
- [Wiring and power](docs/wiring.md)
- [Assembly](docs/assembly.md)
- [Calibration](docs/calibration.md)
- [Testing and results](docs/testing.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Demo recording](docs/demo.md) and [photo checklist](media/README.md)
- [Roadmap](docs/roadmap.md) and [camera upgrade design](docs/camera-setup.md)

## References
- [Arduino Servo library](https://github.com/arduino-libraries/Servo)
- [Arduino servo troubleshooting](https://support.arduino.cc/hc/en-us/articles/360017053760-Troubleshoot-servo-motors)

## License
Original project code and documentation are provided under the [MIT License](LICENSE). External libraries retain their own licenses.
