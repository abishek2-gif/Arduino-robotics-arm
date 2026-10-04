# Arduino Robotic Arm

A four-axis Arduino Uno robotic arm project with joystick control and an interactive browser animation for portfolio/demo use.

## Project Overview

This project is designed as a beginner-friendly embedded systems and robotics build. The first version uses two joystick modules to control four servo motors:

- Base rotation
- Shoulder movement
- Elbow movement
- Gripper open/close

The repository also includes an interactive HTML animation that demonstrates a pick-and-place motion before the physical hardware is fully completed.

## Files

| File | Purpose |
|---|---|
| `arduino/robotic_arm_joystick/robotic_arm_joystick.ino` | Arduino Uno joystick controller sketch |
| `robotic-arm-showcase.html` | Interactive robotic arm animation/demo |
| `README.md` | Project explanation and setup guide |

## Hardware Required

- Arduino Uno
- 4 servo motors
- 2 joystick modules
- External 5V servo power supply
- Jumper wires
- Robotic arm frame or 3D printed structure

Important: do not power all servos directly from the Arduino Uno. Use an external 5V supply for the servos and connect the external power ground to Arduino GND.

## Pin Mapping

| Component | Arduino Pin |
|---|---|
| Joystick 1 VRx | A0 |
| Joystick 1 VRy | A1 |
| Joystick 2 VRx | A2 |
| Joystick 2 VRy | A3 |
| Base servo signal | D3 |
| Shoulder servo signal | D5 |
| Elbow servo signal | D6 |
| Gripper servo signal | D9 |

## Control Mapping

| Joystick Control | Robotic Arm Movement |
|---|---|
| Joystick 1 left/right | Base rotation |
| Joystick 1 up/down | Shoulder movement |
| Joystick 2 left/right | Elbow movement |
| Joystick 2 up/down | Gripper open/close |

## How To Upload The Arduino Code

1. Open `arduino/robotic_arm_joystick/robotic_arm_joystick.ino` in Arduino IDE.
2. Select `Arduino Uno` from the board menu.
3. Connect the Arduino Uno using USB.
4. Upload the sketch.
5. Test one servo first, then connect the full robotic arm.

## View The Animation

Download `robotic-arm-showcase.html` and open it in a modern web browser.

The animation includes:

- Play/Pause demo motion
- Manual sliders for each robotic arm axis
- Pick-and-place style movement
- Example servo angle values for explanation/demo use

This animation is a concept visualization. It does not communicate with the Arduino directly.

## Future Improvements

- Add record and replay movement mode
- Add camera/gesture control using Python, OpenCV or MediaPipe
- Send angle values from laptop to Arduino through USB serial
- Add project photos and demo videos
- Create a LinkedIn and portfolio write-up
