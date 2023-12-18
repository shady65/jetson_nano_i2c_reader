import smbus
import struct
import time

# Define the I2C address of the Arduino
arduino_address = 3*16 # Make sure it matches the Arduino's I2C address
struct_size = 28
# Define the struct format to match the Arduino's struct
struct_format = 'fffffff'


# Function to read the SensorData struct from Arduino
def read_sensor_data():
    try:
        # Open the I2C bus
        bus = smbus.SMBus(1)  # 1 indicates the I2C bus number on the Jetson Nano
        print('bus is opened')
        # Read the struct from Arduino
        raw_data = bus.read_i2c_block_data(arduino_address, 0, struct_size)  
        print(len(raw_data))
   
        # Unpack the received data into the SensorData struct
        sensor_data = struct.unpack(struct_format, bytearray(raw_data))

         # Close the I2C bus
        bus.close()

        return sensor_data

    except Exception as e:
        print(f"Error: {e}")
        return None

# Main loop
while True:
    # Read sensor data from Arduino
    # data = read_sensor_data()

    # if data is not None:
    #     # Print the received sensor data
    #     for i in data:
    #        print("reading:", repr(i))

    #     print("GPS Longitude:", data[0])
    #     print("IMU Acc (X, Y, Z):", data[1], data[2], data[3])
    #     print("IMU Gyro:", data[4])
    #     print("Ultrasonic (1, 2):", data[5], data[6])
    bus = smbus.SMBus(1)  # 1 indicates the I2C bus number on the Jetson Nano
    print('bus is opened')
    bus.write_byte(arduino_address, 0x1)
    time.sleep(1)  # Adjust the delay as needed
