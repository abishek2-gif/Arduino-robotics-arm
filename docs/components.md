# Components
Exact servo models, frame dimensions, power requirements, costs and payload are not yet recorded. This is a selection worksheet, not a verified shopping list.

| Item | Quantity | Selection notes |
|---|---:|---|
| Arduino Uno | 1 | USB data cable compatible with the board |
| Positional hobby servos | 4 | Base, shoulder, elbow, gripper; continuous-rotation servos do not provide commanded angles |
| Two-axis analog joystick modules | 2 | VRx, VRy, supply and ground; switches unused |
| Robotic arm frame | 1 | Servo mount compatibility, bearings, horns and fasteners |
| Regulated servo supply | 1 | Voltage within every attached servo's rating; current capacity for simultaneous peak loads |
| Power distribution and wiring | 1 set | Rated for servo current; avoid routing motor power through light signal jumpers |
| Power switch / disconnect | 1 | Rated for supply current; accessible during tests |
| USB data cable | 1 | Power-only cables cannot upload sketches |
| Multimeter | 1 | Check polarity, voltage and continuity |

## Record your selected hardware
| Axis | Servo model | Rated voltage | Stall current | Rated torque | Link/load details |
|---|---|---|---|---|---|
| Base | TBD | TBD | TBD | TBD | TBD |
| Shoulder | TBD | TBD | TBD | TBD | TBD |
| Elbow | TBD | TBD | TBD | TBD | TBD |
| Gripper | TBD | TBD | TBD | TBD | TBD |

Supply: TBD. Frame: TBD. Payload target: TBD.

Estimate joint torque from all downstream masses and their horizontal lever arms, including links and other servos. Allow margin for motion; do not treat stall torque as a continuous operating rating. Select supply current from the chosen servo specifications, considering simultaneous loads. A blanket “5V 1A” recommendation is not sufficient for an unspecified arm.

Confirm voltage and connector pinout from each manufacturer's documentation before connecting power.
