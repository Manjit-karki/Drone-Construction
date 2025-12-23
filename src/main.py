from flight_controller.components.camera_status import camera_status

def main():
    status = camera_status()
    print("Drone Control System...")
    print(status)

if __name__ == "__main__":
    main()