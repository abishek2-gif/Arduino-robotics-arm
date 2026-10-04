# Arduino Robotic Arm

Interactive concept animation for a four-axis Arduino Uno robotic arm: base, shoulder, elbow and gripper.

## View the animation

Download [robotic-arm-showcase.html](robotic-arm-showcase.html) and open it in a modern web browser. No installation or internet connection is needed.

- Play/Pause controls the automatic demonstration.
- Move the four sliders to explore servo angles manually.
- Reset returns all angles to 90 degrees.

This is a conceptual visualization, not a calibrated robotics simulator. It does not communicate with the Arduino. Camera tracking and USB serial control are planned upgrades; the displayed serial values are illustrative.

## Planned hardware

Arduino Uno, four servos, two joystick modules, and a suitable external servo power supply with common ground to the Uno. Servo voltage, current requirements and mechanical angle limits must be checked against the actual hardware.
