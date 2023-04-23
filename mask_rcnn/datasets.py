import os
from typing import Callable


from mask_rcnn.coco_dataset import CocoDatasetImpl
from mask_rcnn.helpers.train import get_transform

from definitions import ROOT_DIR


class UAVVasteDataset(CocoDatasetImpl):
  
    def __init__(self, name: str, transforms: Callable, train: bool = False):
        super().__init__(
            img_dir=os.path.join(ROOT_DIR, 'data/UAVVaste/images'),
            annot_path=os.path.join(ROOT_DIR, 'data/UAVVaste/annotations.json'),
            transforms=transforms,
            auto_download=train
        )

    def get_name(self) -> str:
        return self.name
    

class TacoDataset(CocoDatasetImpl):
  
    def __init__(self, name: str, transforms: Callable, train: bool = False):
        self.name = name

        super().__init__(
            img_dir=os.path.join(ROOT_DIR, 'data/TACO/images'),
            annot_path=os.path.join(ROOT_DIR, 'data/TACO/annotations.json'),
            transforms=transforms,
            auto_download=train
        )

    def get_name(self) -> str:
        return self.name
    
        
########### Factory ############

def coco_dataset_factory(name: str, train: bool) -> CocoDatasetImpl:
    if name == "UAVVaste": return UAVVasteDataset("UAVVaste", get_transform(train=train), train)
    elif name == "TACO": return TacoDataset("TACO", get_transform(train=train), train)
    raise Exception(f"'{name}' is not a valid dataset name")
    