#!/usr/bin/env python
# coding=utf-8
import cv2
import numpy as np
import struct
import os
import random

ROW   = 80
COL   = 120

def read_images(train_dir):
    images = os.listdir(train_dir)
    # volume of data_set (train_dir)
    data_volume = len(images)
    # get a random list intend to shuffle the data_set 
    images_list = range(data_volume)
    random.shuffle(images_list)
    random.shuffle(images_list)
    # return to the main Call function
    # data.shape  = (volume,row,col,depth)
    data  = np.zeros((data_volume,ROW*COL))
    # label.shape = (volume,row,col,depth)
    #label = np.zeros((data_volume,1))
    #label = np.zeros((data_volume,1))
    #当label长度不是5的时候
    label = np.zeros((data_volume,2))
    for loop in xrange(data_volume):
        image_name  =  images[images_list[loop]]
        image       =  os.path.join(train_dir,image_name)
        img         =  cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        #XXX: I want to feed data by COL
        #XXX: 按列来组织图片数据

        img         =  img.transpose(1,0)
        img         =  img.reshape((ROW*COL))
        #img         =  img.reshape((ROW,COL,depth))
        data[loop]  =  img

        image_name  =  image_name.strip()
        image_name  =  image_name.split('.')[0]
        image_name  =  image_name.split('_')[1]
        #image_label =  image_name[:]
        #当label长度不是5的时候
        
        image_label = [0,0]
        length_name = len(image_name)
        for i in xrange(length_name):
            image_label[i] = image_name[i]
        if  length_name != 2:
            for j in xrange(length_name,5):
                image_label[i] = 10
        #label.append(image_label)
        
        label[loop] = image_label 
    return data,label


def read_data(train_dir,reshape=True):
    images       =    os.listdir(train_dir)
    data_volume  =    len(images)
    img_tem      =    cv2.imread(train_dir+images[0],cv2.IMREAD_GRAYSCALE)
    width,height =    img_tem.shape
    dim          =    int(width*height)
    matrix       =    np.zeros((data_volume,dim))
    loop         =    0
    for image    in   images:
        img_name =    image.split('.')[0]
        img_     =    cv2.imread(train_dir+"/"+image,cv2.IMREAD_GRAYSCALE)
        img_     =    img_.reshape((dim))
        matrix[loop]\
                 =    img_
        loop    +=    1
    return matrix,images
