from .step import Step
import cv2


class GeometricalStep(Step):
    def __call__(self, img):
        return self.rotate(img)

    @staticmethod
    def rotate(img):
        img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        return img_rotate_90_clockwise
