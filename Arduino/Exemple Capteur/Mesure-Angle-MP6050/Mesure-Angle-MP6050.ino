#include <Wire.h>
#include <math.h>

const int MPU_addr = 0x68;  // I2C address of the MPU-6050

// Accelerometer and Gyroscope variables
int16_t AcX, AcY, AcZ, GyX, GyY, GyZ;

// Angle variables
float roll, pitch, yaw;

// Calibration offsets
const float ACCEL_SCALE = 16384.0; // Sensitivity scale factor for accelerometer
const float GYRO_SCALE = 131.0;    // Sensitivity scale factor for gyroscope

void setup() {
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(9600);
}

void loop() {
  // Read accelerometer and gyroscope data
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr, 14, true);  // request a total of 14 registers

  AcX = Wire.read() << 8 | Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
  AcY = Wire.read() << 8 | Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ = Wire.read() << 8 | Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Wire.read(); Wire.read(); // Skip temperature data
  GyX = Wire.read() << 8 | Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY = Wire.read() << 8 | Wire.read();  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ = Wire.read() << 8 | Wire.read();  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

  // Convert to degrees
  float accelX = AcX / ACCEL_SCALE;
  float accelY = AcY / ACCEL_SCALE;
  float accelZ = AcZ / ACCEL_SCALE;

  float gyroX = GyX / GYRO_SCALE;
  float gyroY = GyY / GYRO_SCALE;
  float gyroZ = GyZ / GYRO_SCALE;

  // Calculate pitch and roll
  roll  = atan2(accelY, accelZ) * 180.0 / PI;
  pitch = atan2(-accelX, sqrt(accelY * accelY + accelZ * accelZ)) * 180.0 / PI;

  // Simple yaw calculation (not very accurate as it does not integrate gyroscope data)
  yaw = atan2(accelY, accelX) * 180.0 / PI;

  Serial.print("Roll = "); Serial.print(roll); Serial.print("° | "); //X
  Serial.print("Pitch = "); Serial.print(pitch); Serial.print("° | "); //Y

  delay(500);
}
