#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# In[ ]:


def make_img(model, image):
    image = tf.cast(image[np.newaxis, ...], tf.float32)
    sr = model.predict(image)
    sr = tf.clip_by_value(sr, 0, 255)
    sr = tf.round(sr)
    sr = tf.cast(sr, tf.uint8)
    return np.array(sr)[0]


# In[ ]:


def main(target_img_path):
    
    model_file = 'srgan/models/srgan_G.h5'
    model = tf.keras.models.load_model(model_file)
    
    img = pilimg.open(target_img_path)
    npimg = make_img(model, img)
    reformed_img = Image.fromarray(npimg)
    
    result_img_name = target_img_path.split('.')[0].split('/')[-1]
    result_prefix = 'srgan/images/reformed_'+result_img_name
    
    
    fname = result_prefix + '.png'
    reformed_img.save(fname)
    
    
    return fname


# In[ ]:


if __name__ == "__main__":
    main()


# In[ ]:




