# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:32:21 2016

@author: a
"""
import numpy as np
import cv2
import os

kernelWidth = 10
kernelHeight = 80
stepX = 10
stepY = 0
'''
XXX:
     startPoint:Left-Top point 
'''
def GetPixes(img,startPointY,startPointX,width,height):
    #img_roi = np.array([])
    img_roi = img[startPointY:startPointY+height,startPointX:startPointX+width]
    return img_roi

'''
'''
def GetSlices(img_name,img,step_x,step_y,destination):
    loopNum = int(img.shape[1])/step_x
    #assert step_y != 0, ("Step_y should not be 0...")
    if step_y == 0:
        loopNumVertical = 1
    else:
        loopNumVertical = int(img.shape[0])/step_y
    startX = 0
    startY = 0
    
    for loopOuter in xrange(loopNumVertical):
        startX  =0
        for loop in xrange(loopNum):
            img_slice = GetPixes(img,startY,startX,kernelWidth,kernelHeight)
            startX += step_x
            #name_slice = "/%d.jpg"%(loopOuter*1000+loop)
            name_slice = "/%s.jpg"%(img_name+"_"+str(loopOuter*1000+loop))
            cv2.imwrite(destination+name_slice,img_slice)
        startY += step_y
            #cv2.imwrite()

def ScanFile(sourcePath,targetPath):
    for image in os.listdir(sourcePath):
        img_name = image.split('.')[0]
        img_ = cv2.imread(sourcePath+"/"+image,-1)
        #targetPath_ = targetPath+"/"+image.split('.')[0]
        #if not os.path.exists(targetPath_):
        #    os.mkdir(targetPath_)
        GetSlices(img_name,img_,stepX,stepY,targetPath)
#img = cv2.imread("D:/workspace/tensorflow/udacity/b.png",-1)
#path = "D:/workspace/tensorflow/train_slice"

if __name__ == '__main__':
    source = "D:/workspace/ubuntu/workspace/ocr/datasets"
    target = "D:/workspace/ubuntu/workspace/ocr/slice"
    ScanFile(source,target)

