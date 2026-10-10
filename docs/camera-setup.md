# Camera upgrade — planned
This is a design brief, not runnable installation instructions. No Python tracker or serial-control sketch is included yet.

## Intended data flow
Laptop camera → Python landmark tracking → calibrated joint commands → USB serial → Uno → servos.

The laptop handles image processing. The Uno receives validated commands and drives servos.

## Before implementation
1. Finish joystick calibration and record safe joint limits.
2. Choose hand or arm tracking and decide how each tracked movement maps to each joint.
3. Define a serial message format, send rate and startup/arming behaviour.
4. Implement length limits, complete-message parsing, numeric validation and joint clamping on the Uno.
5. Define and test what happens when tracking is lost or communication stops. Holding or relaxing the arm must be chosen with its load and mechanical support in mind.
6. Test with servo power disconnected, then one unloaded servo, before using the whole arm.

## Future files
- python/hand_tracking.py
- python/requirements.txt
- arduino/robotic_arm_serial/robotic_arm_serial.ino

Choose compatible Python and tracking-library versions at implementation time. The animation's comma-separated display is illustrative and is not an implemented protocol.
