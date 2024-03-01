#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner
from modules.pipeline import init_local_pipeline
from modules.components import init_components
import pandas as pd


# In[4]:


dataset = pd.read_csv('./data/train_fix.csv')


# In[5]:


dataset


# # Set Variabel

# In[7]:


PIPELINE_NAME = 'stroke-pipeline'

DATA_ROOT = 'data'
TRANSFORM_MODULE_FILE = 'modules/transform.py'
TRAINER_MODULE_FILE = 'modules/trainer.py'

OUTPUT_BASE = 'output'
serving_model_dir = os.path.join(OUTPUT_BASE, 'serving_model')
pipeline_root = os.path.join(OUTPUT_BASE, PIPELINE_NAME)
metadata_path = os.path.join(pipeline_root, 'metadata.sqlite')


# # Running

# In[8]:


components = init_components(
    data_dir=DATA_ROOT,
    transform_module=TRANSFORM_MODULE_FILE,
    training_module=TRAINER_MODULE_FILE,
    training_steps=4000,
    eval_steps=500,
    serving_model_dir=serving_model_dir
)

pipeline = init_local_pipeline(components, pipeline_root)
BeamDagRunner().run(pipeline)


# In[ ]:




