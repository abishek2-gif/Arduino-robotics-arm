#include <Servo.h>

Servo baseServo;
Servo shoulderServo;
Servo elbowServo;
Servo gripperServo;

const int BASE_SERVO_PIN = 3;
const int SHOULDER_SERVO_PIN = 5;
const int ELBOW_SERVO_PIN = 6;
const int GRIPPER_SERVO_PIN = 9;

const int JOYSTICK_1_X_PIN = A0;
const int JOYSTICK_1_Y_PIN = A1;
const int JOYSTICK_2_X_PIN = A2;
const int JOYSTICK_2_Y_PIN = A3;

const int JOYSTICK_CENTER = 512;
const int DEADZONE = 80;
const int MOVE_STEP = 2;
const int LOOP_DELAY_MS = 20;

int baseAngle = 90;
int shoulderAngle = 90;
int elbowAngle = 90;
int gripperAngle = 90;

void setup() {
  baseServo.attach(BASE_SERVO_PIN);
  shoulderServo.attach(SHOULDER_SERVO_PIN);
  elbowServo.attach(ELBOW_SERVO_PIN);
  gripperServo.attach(GRIPPER_SERVO_PIN);

  baseServo.write(baseAngle);
  shoulderServo.write(shoulderAngle);
  elbowServo.write(elbowAngle);
  gripperServo.write(gripperAngle);

  delay(1000);
}

void loop() {
  int joystick1X = analogRead(JOYSTICK_1_X_PIN);
  int joystick1Y = analogRead(JOYSTICK_1_Y_PIN);
  int joystick2X = analogRead(JOYSTICK_2_X_PIN);
  int joystick2Y = analogRead(JOYSTICK_2_Y_PIN);

  baseAngle = updateAngleFromJoystick(joystick1X, baseAngle, 0, 180);
  shoulderAngle = updateAngleFromJoystick(joystick1Y, shoulderAngle, 25, 155);
  elbowAngle = updateAngleFromJoystick(joystick2X, elbowAngle, 20, 160);
  gripperAngle = updateAngleFromJoystick(joystick2Y, gripperAngle, 45, 120);

  baseServo.write(baseAngle);
  shoulderServo.write(shoulderAngle);
  elbowServo.write(elbowAngle);
  gripperServo.write(gripperAngle);

  delay(LOOP_DELAY_MS);
}

int updateAngleFromJoystick(int joystickValue, int currentAngle, int minAngle, int maxAngle) {
  if (joystickValue > JOYSTICK_CENTER + DEADZONE) {
    currentAngle += MOVE_STEP;
  } else if (joystickValue < JOYSTICK_CENTER - DEADZONE) {
    currentAngle -= MOVE_STEP;
  }

  return constrain(currentAngle, minAngle, maxAngle);
}
