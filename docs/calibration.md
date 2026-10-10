# Calibration
The current sketch initializes every servo to 90°. Its example limits are base 0–180°, shoulder 25–155°, elbow 20–160° and gripper 45–120°. These have not been validated against a particular frame.

## Initial setup
1. Detach horns and loads. Connect only the servo under test.
2. In the sketch, temporarily restrict that axis's updateAngleFromJoystick call to a narrow range around the starting command, for example 85–95°, only if supported by its datasheet.
3. Set MOVE_STEP to 1 and LOOP_DELAY_MS to 40 for slower initial tests.
4. Upload with servo power off. Apply the correctly rated servo supply and confirm movement without binding, excessive heat or persistent buzzing.
5. Disconnect power and attach the horn in the intended supported home pose.
6. Test small movements. Expand the limits gradually; stop before mechanical contact or cable tension. Never intentionally drive into a stop.
7. Repeat for each axis, then check combinations of shoulder and elbow positions for collisions.

Edit baseAngle, shoulderAngle, elbowAngle and gripperAngle if your calibrated starting positions differ. Starting angles must fall inside their calibrated limits. The existing sketch writes the starting angles before applying joystick limits.

## Direction and joystick centre
If an axis moves opposite to the desired direction, replace its input argument with 1023 - joystickValue using the matching variable (for example 1023 - joystick1X for the base).

The sketch assumes centre 512 with a deadzone of 80. If it drifts, first check wiring and record analogRead values while the stick is released. Adjust centre/deadzone based on actual readings. Separate per-axis centres may be required.

## Calibration record
| Axis | Starting command | Minimum | Maximum | Direction reversed? | Verified date |
|---|---|---|---|---|---|
| Base | TBD | TBD | TBD | TBD | Not tested |
| Shoulder | TBD | TBD | TBD | TBD | Not tested |
| Elbow | TBD | TBD | TBD | TBD | Not tested |
| Gripper | TBD | TBD | TBD | TBD | Not tested |

Software limits do not detect collisions, torque overload or a disconnected joystick. Servo commands are not measured joint-position feedback.
