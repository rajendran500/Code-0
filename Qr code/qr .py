import cv2
from pyzbar.pyzbar import decode
import numpy as np

expected_data = "Harish Rajendran 19"

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    message = "No QR code detected"
    
    for qr in decode(frame):
        qr_data = qr.data.decode('utf-8')
        print("Scanned:", qr_data)

        if qr_data == expected_data:
            message = "Welcome Harish Rajendran"
        else:
            message = "Unknown QR code"

        # Draw polygon around QR code
        pts = np.array([qr.polygon], dtype=np.int32)
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        # Display message
        x, y = pts[0][0]
        cv2.putText(frame, message, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 0, 0), 2)

    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

