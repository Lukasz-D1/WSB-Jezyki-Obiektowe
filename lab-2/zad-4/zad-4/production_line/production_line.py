from steps import *
import cv2


class ProductionLine:
    def __init__(self, name):
        print('Production line open. To add image-transforming steps use "add_step" function with proper attribute.'
              '\nAvailable options: color, geometrical, threshold.'
              '\nTo remove last added step use "remove_latest_step".'
              '\nSave output to file using "save_result_to_file".')
        self.__name = name
        self.__steps = []

    def add_step(self, step_type):
        if step_type == 'color':
            self.__steps.append(ColorStep())
        elif step_type == 'geometrical':
            self.__steps.append(GeometricalStep())
        elif step_type == 'threshold':
            self.__steps.append(ThresholdStep())
        else:
            print('step not implemented')

    def remove_latest_step(self):
        self.__steps.pop()

    def perform_steps(self, img):
        if len(self.__steps) > 1:
            for i in range(len(self.__steps)):
                if i == 0:
                    output = self.__steps[i+1](self.__steps[i](img))
                elif i > 1:
                    output = self.__steps[i](output)
            return output
        else:
            return self.__steps[0](img)

    @staticmethod
    def show_image(img):
        cv2.imshow('image', img)
        cv2.waitKey(0)

    @staticmethod
    def save_result_to_file(name, img):
        cv2.imwrite(name, img)
