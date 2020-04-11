import cv2
from production_line import ProductionLine


def main():
    img = cv2.imread('dog.jpeg', 1)
    img2 = cv2.imread('cat.jpeg', 1)
    prod = ProductionLine("nazwa")
    prod.add_step('geometrical')
    prod.add_step('color')
    res = prod.perform_steps(img)
    prod.show_image(res)
    prod.save_result_to_file('dog_result.jpeg', res)
    prod.remove_latest_step()
    prod.add_step('geometrical')
    prod.add_step('threshold')
    prod.show_image(prod.perform_steps(img2))


if __name__ == '__main__':
    main()
