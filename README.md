# jetson_nano_i2c_reader
this code is meant to read data sent through i2c coming from arduino Nano328P
I2C Communication with Arduino on Jetson Nano
This Python script is designed for reading sensor data from an Arduino using I2C communication on a Jetson Nano. The Arduino is expected to send a struct containing various sensor readings. Here's a brief overview of the script:

Dependencies
smbus: Python module for interacting with the System Management Bus (SMBus) on the Jetson Nano.
struct: Python module for packing and unpacking binary data.
Constants
arduino_address: The I2C address of the Arduino. Make sure it matches the Arduino's I2C address.
struct_size: The size of the struct in bytes.
struct_format: The format of the struct, specifying the data types and order.
Functions
read_sensor_data()
Opens the I2C bus using smbus.SMBus(1) (assuming I2C bus number 1 on the Jetson Nano).
Reads a block of data (struct_size bytes) from the Arduino at the specified I2C address.
Unpacks the received binary data into a Python tuple using struct.unpack.
Closes the I2C bus.
Returns the unpacked sensor data.
Main Loop
In an infinite loop, it reads sensor data from the Arduino using read_sensor_data().
If the data is not None, it prints each reading in the data tuple, including GPS longitude, IMU accelerometer and gyroscope readings, and ultrasonic sensor readings.
Adjusts the delay using time.sleep(1).
Note
Ensure the correct I2C address for the Arduino is specified (arduino_address).
Adjust the I2C bus number if needed (smbus.SMBus(1)).
Modify the struct_format to match the data sent by the Arduino.
The script assumes the Arduino is sending a struct with seven float values in the specified order.
