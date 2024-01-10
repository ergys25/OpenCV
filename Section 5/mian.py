import cv2


def draw_circle(event, x, y, flags, param):
    global center, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = True


center = (0, 0)  # Initialize the center of the circle
clicked = False  # Initialize the clicked flag

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Open the video capture device

cv2.namedWindow(winname="my_img")  # Create a named window
cv2.setMouseCallback("my_img", draw_circle)  # Set the mouse callback function

while True:
    ret, frame = cap.read()  # Read a frame from the video capture device
    if clicked:
        cv2.circle(
            frame, center, 50, (0, 255, 0), thickness=10
        )  # Draw a circle on the frame with the specified parameters
    cv2.imshow("my_img", frame)  # Display the frame in the named window
    if cv2.waitKey(1) & 0xFF == 27:  # Break the loop if the 'Esc' key is pressed
        break
