#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import glob
import os
import re
from collections import OrderedDict

from batchgenerators.utilities.file_and_folder_operations import save_json


def list_sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """

    def tryint(s):
        try:
            return int(s)
        except:
            return s

    def alphanum_key(s):
        """ Turn a string into a list of string and number chunks.
            "z23a" -> ["z", 23, "a"]
        """
        return [tryint(c) for c in re.split('([0-9]+)', s)]

    l.sort(key=alphanum_key)
    return l


# path_originalData = 'xxxx/PycharmProjects/nnUNet/nnUNet_raw/nnUNet_raw_data/Task072_HCC/'
path_originalData = '/mnt/data/datasets/nnunet_dataset/nnUNet_raw_data_base/nnUNet_raw_data/Task022_FLARE23'

train_image = list_sort_nicely(glob.glob(os.path.join(path_originalData, 'imagesTr', '*')))
train_label = list_sort_nicely(glob.glob(os.path.join(path_originalData, 'labelsTr', '*')))
test_image = list_sort_nicely(glob.glob(os.path.join(path_originalData, 'imagesTs', '*')))
# test_label = list_sort_nicely(glob.glob(os.path.join(path_originalData, 'labelsTs', '*')))

train_image = ["{}".format(os.path.basename(item)) for item in train_image]
train_label = ["{}".format(os.path.basename(item)) for item in train_label]
test_image = ["{}".format(os.path.basename(item)) for item in test_image]
# test_label = ["{}".format(os.path.basename(item)) for item in test_label]
# 输出一下目录的情况，看是否成功
print(train_image)
print(train_label)
print(test_image)
# print(test_label)

# 自行修改
json_dict = OrderedDict()
json_dict['name'] = "FLARE2023"
json_dict['description'] = "nothing"
json_dict['tensorImageSize'] = "3D"
json_dict['reference'] = "ssw"
json_dict['licence'] = "ssw"
json_dict['release'] = "0.0"
json_dict['modality'] = {
    "0": "CT"
    # "0": "HBP",
    # "1" : "T1"
    # 将模态信息写在这里

}
json_dict['labels'] = {
    "0": "background",
    "1": "Liver",
    "2": "Right kidney",
    "3": "Spleen",
    "4": "Pancreas",
    "5": "Aorta",
    "6": "Inferior vena cava",
    "7": "Right adrenal gland",
    "8": "Left adrenal gland",
    "9": "Gallbladder",
    "10": "Esophagus",
    "11": "Stomach",
    "12": "Duodenum",
    "13": "Left Kidney",
    "14": "Tumor",
}
json_dict['numTraining'] = len(train_image)
json_dict['numTest'] = len(test_image)
json_dict['training'] = [{'image': "./imagesTr/%s" % i, "label": "./labelsTr/%s" % i} for i in train_label]
json_dict['test'] = ["./imagesTs/%s" % i for i in test_image]
save_json(json_dict, os.path.join(path_originalData, "dataset.json"))
