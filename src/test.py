import torch
import numpy as np
import torchvision
from models.extract_features import *
from models.features_classifer import *
from data.dataset import preprocess
import json


def get_json(path=r"JiMei-Palmer-Recognition\config\model.json"):
    with open(path,"r") as f:
        config_model_dict=json.load(f)[0]
    print(config_model_dict)
    return config_model_dict

def get_features(test_img):
    image=preprocess(test_img)
    model=get_extract_model()
    return model(image)

def get_base_id(features):
    model=get_classifier_model()
    return model(features)

def get_extract_model():
    model_name=get_json["extract_features_model_name"]
    model=model_name()
    model_dict=torch.load(get_json["extract_features_model_path"])
    # model.load(model_dict)
    return model

def get_classifier_model():
    model_name=get_json["features_classifer_model_name"]
    model=model_name()
    model_dict=torch.load(get_json["features_classifer_model_path"])
    # model.load(model_dict)
    return model

def run(test_imgs):
    for test_img in test_imgs:
        features=get_features(test_img)
        id=get_base_id(features)




if __name__=="__main__":
    get_json()