# Assembly guide
Frame-specific instructions take priority for screw lengths, bearings and mounting orientation.

1. Inventory the parts and record the servo models in components.md.
2. Fix the base to a stable surface. Check that each joint moves freely with power disconnected.
3. Identify the base, shoulder, elbow and gripper servos. Label their signal leads.
4. Leave horns and mechanical links detached for the initial electrical test.
5. Wire and upload the sketch using wiring.md and the main README.
6. With a single unloaded servo connected, verify its neutral command and a small movement range as described in calibration.md. Repeat for all four.
7. Remove servo power before attaching each horn. Position the mechanism so the configured starting command corresponds to a clear, supported pose.
8. Attach links one at a time. Check for collisions, cable tension and hard stops with power off.
9. Set narrow initial software limits and reduce movement speed before testing the assembled mechanism.
10. Support the shoulder and elbow, power up without payload, and test one joint at a time.
11. Expand limits only after checking clearance across combined joint positions.
12. Add a light test object only after unloaded checks pass. Record its measured mass and actual results.

Power-up commands can cause immediate motion. A 90° command is not necessarily the physical midpoint or a safe assembled pose. Never force a powered servo by hand.
