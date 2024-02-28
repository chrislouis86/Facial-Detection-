import mediapipe as mp
import cv2

mp_drawing=mp.solutions.drawing_utils
mp_face_mesh=mp.solutions.face_mesh

video=cv2.VideoCapture(1)

with mp_face_mesh(min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face_mesh:




    while True:
            ret.image=video.read()
            image=cv2,cvtColor(image, cv2.COLOR_BRG2RGB)
            image.flags.writeable=False
            results=face_mesh.process(image)
            #print(results)
            if results.multi_face_landmarks:
                for multi_face_landmarks in results.multi_face_landmarks:
                cv2.imshow("Face Mesh", image)
                 k=cv2.waitkey(1)
                if k==ord('q'):
                break

    video.release()
    cv2.destroyAllWindows()

