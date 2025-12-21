from utils.camera_status import camera_status

def main():
    print("Starting Drone Construction Project...")
    status = camera_status()
    print(status)
    
if __name__ == "__main__":
    main()