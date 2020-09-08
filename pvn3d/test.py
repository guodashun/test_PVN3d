import numpy as np
import os

def test_csv():
    mask = np.genfromtxt("/home/dataset/OCRTOC_dataset/mask_value.csv", delimiter=',')  
    print(mask)

def test_npy():
    mask = np.load("/home/dataset/OCRTOC_dataset/render_image_py/camera_extrinsic.npy", allow_pickle=True, encoding='bytes')  
    print(mask)

def test_class():
    dir_list = os.listdir("/home/dataset/OCRTOC_dataset/models")
    print(dir_list)

if __name__ == '__main__':
    # test_csv()
    # test_npy()
    test_class()
