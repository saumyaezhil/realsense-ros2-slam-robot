#include <Arduino.h>

float linear = 0.0;
float angular = 0.0;

float wheel_base = 0.25;   // distance between wheels (meters)

float left_speed = 0.0;
float right_speed = 0.0;

String cmd;

void setup()
{
    Serial.begin(115200);
}

void loop()
{

    if (Serial.available())
    {
        cmd = Serial.readStringUntil('\n');

        sscanf(cmd.c_str(), "%f,%f", &linear, &angular);

        left_speed  = linear - angular * wheel_base / 2.0;
        right_speed = linear + angular * wheel_base / 2.0;

        Serial.print("Left: ");
        Serial.print(left_speed);

        Serial.print("  Right: ");
        Serial.println(right_speed);

        // send to motor driver here
    }
}
