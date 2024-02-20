# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:05:21 2024

@author: sbbk034
"""
# The path can also be read from a config file, etc.
OPENSLIDE_PATH = r'C:\Users\sbbk034\OneDrive - City, University of London\Acad\temp\openslide-win64-20231011\bin'

import os
if hasattr(os, 'add_dll_directory'):
    # Windows
    with os.add_dll_directory(OPENSLIDE_PATH):
        import openslide
else:
    import openslide

from openslide import OpenSlide


# Clear logger to use tiatoolbox.logger
import logging
import warnings

if logging.getLogger().hasHandlers():
    logging.getLogger().handlers.clear()
    
# Pretty print for nice dictionary printing
from pprint import pprint
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import torch
import tiatoolbox

#import sys
#sys.path.insert(0, r'C:\Users\sbbk034\OneDrive - City, University of London\Acad\temp\tiatoolbox-develop\tiatoolbox\models\engine')
#os.system("C:\Users\sbbk034\OneDrive - City, University of London\Acad\temp\tiatoolbox-develop\tiatoolbox\models\engine\semantic_segmentor.py")

from semantic_segmentor import SemanticSegmentor

from matplotlib import cm

from tiatoolbox import logger

#from tiatoolbox.data import small_svs
#from tiatoolbox.wsicore.wsireader import WSIReader

#from tiatoolbox.utils.misc import download_data, imread
#from tiatoolbox.utils.visualization import overlay_prediction_mask
#from tiatoolbox.models.architecture.unet import UNetModel
#from tiatoolbox.models.engine.semantic_segmentor import (
#    IOSegmentorConfig,
#    SemanticSegmentor,
#)



mpl.rcParams["figure.dpi"] = 300  # for high resolution figure in notebook
mpl.rcParams["figure.facecolor"] = "white"  # To make sure text is visible in dark mode
warnings.filterwarnings("ignore")
plt.rcParams.update({"font.size": 5})


file_path = '/content/TCGA-A1-A0SK-DX1_xmin45749_ymin25055_MPP-0.2500D.png'
logger.info(file_path)

reader = WSIReader.open(file_path)
print(reader)  # noqa: T201