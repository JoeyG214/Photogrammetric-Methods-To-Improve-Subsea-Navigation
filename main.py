import cv2

def main():

    cap = cv2.VideoCapture(0)

    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Wait for a key press and if 'q' is pressed, break from the loop
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
        
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()