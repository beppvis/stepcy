import cv2
from pyzbar.pyzbar import decode
import json

# Predefined dictionary of data, using "Falcon" as a key
data_dict = {
    "Falcon": "1:10:2",
    "xyzz": "User 2",
    "1234567890": "User 3",
    "yzkks": "Website",
    "Address": "User Address"
}

# Store the set of scanned QR codes
scanned_qr_codes = set()

def read_qr_code(frame):
    # Decode QR codes from the frame
    qr_codes = decode(frame)
    
    for qr_code in qr_codes:
        # Extract the coordinates of the QR code
        x, y, w, h = qr_code.rect
        # Draw a rectangle around the QR code
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Get the decoded QR code data as a string
        qr_data = qr_code.data.decode('utf-8')
        qr_type = qr_code.type
        
        # Display the QR code data and type on the frame
        text = f"{qr_data} ({qr_type})"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        return qr_data  # Return the QR code data
    
    return None

def main():
    global scanned_qr_codes
    
    # Open the webcam (0 is usually the default webcam)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    print("Press 'q' to exit the webcam.")
    
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break
        
        # Scan the frame for QR codes
        qr_data = read_qr_code(frame)
        
        if qr_data and qr_data not in scanned_qr_codes:
            # Add the QR code to the set of scanned QR codes
            scanned_qr_codes.add(qr_data)
            
            # Print the QR code data
            print(f"QR Code Data: {qr_data}")
            
            # Try to parse the QR code data as JSON
            try:
                qr_json = json.loads(qr_data)
                if "node" in qr_json:
                    node_value = qr_json["node"]
                    print(f"Extracted 'node': {node_value}")
                    
                    # Check if the 'node' value is in the dictionary
                    if node_value in data_dict:
                        print(f"QR Code matched: {data_dict[node_value]}")
                    else:
                        print("QR Code data not found in the dictionary.")
                else:
                    print("QR Code does not contain a 'node' key.")
                    
            except json.JSONDecodeError:
                # Handle non-JSON QR code data
                print("Error: QR code data is not in valid JSON format.")
        
        # Display the video frame
        cv2.imshow("QR Code Scanner", frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the webcam and close any open windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
