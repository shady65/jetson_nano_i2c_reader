import smbus
import struct
import time

# Define the I2C address of the Arduino
arduino_address = 8  # Make sure it matches the Arduino's I2C address

# Define the struct format to match the Arduino's struct
struct_format = 'ff ffff ff Q'

# Function to read the SensorData struct from Arduino
def read_sensor_data():
    try:
        # Open the I2C bus
        bus = smbus.SMBus(1)  # 1 indicates the I2C bus number on the Jetson Nano

        # Read the struct from Arduino
        raw_data = bus.read_i2c_block_data(arduino_address, 0, 32)  # 32 is the size of the struct in bytes

        # Unpack the received data into the SensorData struct
        sensor_data = struct.unpack(struct_format, bytearray(raw_data))
#comment
        # Close the I2C bus
        bus.close()

        return sensor_data

    except Exception as e:
        print(f"Error: {e}")
        return None

# Main loop
while True:
    # Read sensor data from Arduino
    data = read_sensor_data()

    if data is not None:
        # Print the received sensor data
        print("GPS Latitude:", data[0])
        print("GPS Longitude:", data[1])
        print("IMU Acc (X, Y, Z):", data[2], data[3], data[4])
        print("IMU Gyro:", data[5])
        print("Ultrasonic (1, 2):", data[6], data[7])
        print("Timestamp:", data[8])

    time.sleep(1)  # Adjust the delay as needed
