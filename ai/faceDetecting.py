import cv2 as cv
import matplotlib.pyplot as plt

def getMask(rect1, rect2):
    (x1, y1, w1, h1) = rect1
    (x2, y2, w2, h2) = rect2

    original_image = cv.imread(r"C:\Users\kdy94\vocational training\ai\face.jpg")
    if original_image is None:
        print("안들어옴")
        return
    grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

    face_cascade =cv.CascadeClassifier(r"C:\Users\kdy94\vocational training\ai\haarcascade_frontalface_default.xml")
    detected_faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)

    for (x1, y1, width, height) in detected_faces:
        rect = cv.rectangle(
            original_image,
            (x1, y1),
            (x1 + width, y1 + height),
            (0, 255, 0),
            2
        )

    cv.imshow('Image', original_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # plt.imshow(cv.cvtColor(original_image, cv.COLOR_BGR2RGB))
    # plt.title("Detected Faces")
    # plt.axis('off')
    # plt.show()



getMask((0, 0, 0, 0), (0, 0, 0, 0))

