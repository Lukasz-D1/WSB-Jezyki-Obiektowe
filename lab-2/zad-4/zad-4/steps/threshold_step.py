from .step import Step
import cv2


class ThresholdStep(Step):
    def __call__(self, img):
        return self.threshold(img)

    @staticmethod
    def threshold(img):
        ret, output = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        return output
