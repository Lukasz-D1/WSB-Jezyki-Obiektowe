from .step import Step


class ColorStep(Step):
    def __call__(self, img):
        return self.invert_colors(img)

    @staticmethod
    def invert_colors(img):
        img_neg = 255 - img
        return img_neg
