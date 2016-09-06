import cv2
import numpy as np
from matplotlib import pyplot as plt

import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
img_amazon = cv2.imread('./data/images/seasoning_images/imageFromAmazon.jpg',0)
img_shopify = cv2.imread('./data/images/seasoning_images/imageFromShopify.jpg',0)
img_1 = cv2.imread('./data/images/seasoning_images/image1.jpg',0)
img_2 = cv2.imread('./data/images/seasoning_images/image2.jpg',0)
img_3 = cv2.imread('./data/images/seasoning_images/image3.jpg',0)
img_4 = cv2.imread('./data/images/seasoning_images/image4.jpg',0)
img_5 = cv2.imread('./data/images/seasoning_images/image5.jpg',0)
img_6 = cv2.imread('./data/images/seasoning_images/image6.jpg',0)
img_7 = cv2.imread('./data/images/seasoning_images/image7.jpg',0)
img_8 = cv2.imread('./data/images/seasoning_images/image8.jpg',0)
img_9 = cv2.imread('./data/images/seasoning_images/image9.jpg',0)
img_10 = cv2.imread('./data/images/seasoning_images/image10.jpg',0)
img_11 = cv2.imread('./data/images/seasoning_images/image11.jpg',0)

def auto_canny(image, sigma = 0.33):
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged

edges_amazon = auto_canny(img_amazon)
plt.imsave('./data/images/seasoning_images/edgesFromAmazon.jpg',edges_amazon,cmap='gray')
edges_shopify = auto_canny(img_shopify)
plt.imsave('./data/images/seasoning_images/edgesFromShopify.jpg',edges_shopify,cmap='gray')
edges_im_1 = auto_canny(img_1)
plt.imsave('./data/images/seasoning_images/edgesFromImg1.jpg',edges_shopify,cmap='gray')
edges_im_2 = auto_canny(img_2)
plt.imsave('./data/images/seasoning_images/edgesFromImg2.jpg',edges_amazon,cmap='gray')
edges_im_3 = auto_canny(img_3)
plt.imsave('./data/images/seasoning_images/edgesFromImg3.jpg',edges_shopify,cmap='gray')
edges_im_4 = auto_canny(img_4)
plt.imsave('./data/images/seasoning_images/edgesFromImg4.jpg',edges_amazon,cmap='gray')
edges_im_5 = auto_canny(img_5)
plt.imsave('./data/images/seasoning_images/edgesFromImg5.jpg',edges_shopify,cmap='gray')
edges_im_6 = auto_canny(img_6)
plt.imsave('./data/images/seasoning_images/edgesFromImg6.jpg',edges_amazon,cmap='gray')
edges_im_7 = auto_canny(img_7)
plt.imsave('./data/images/seasoning_images/edgesFromImg7.jpg',edges_shopify,cmap='gray')
edges_im_8 = auto_canny(img_8)
plt.imsave('./data/images/seasoning_images/edgesFromImg8.jpg',edges_amazon,cmap='gray')
edges_im_9 = auto_canny(img_9)
plt.imsave('./data/images/seasoning_images/edgesFromImg9.jpg',edges_shopify,cmap='gray')
edges_im_10 = auto_canny(img_10)
plt.imsave('./data/images/seasoning_images/edgesFromImg10.jpg',edges_shopify,cmap='gray')
edges_im_11 = auto_canny(img_11)
plt.imsave('./data/images/seasoning_images/edgesFromImg11.jpg',edges_amazon,cmap='gray')

plt.subplot(120),plt.imshow(edges_amazon,cmap = 'gray')
plt.title('Amazon'), plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(edges_shopify,cmap = 'gray')
plt.title('Shopify'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(edges_im_1,cmap = 'gray')
plt.title('Img1'), plt.xticks([]), plt.yticks([])

plt.subplot(123),plt.imshow(edges_im_2,cmap = 'gray')
plt.title('Img2'), plt.xticks([]), plt.yticks([])

plt.subplot(124),plt.imshow(edges_im_3,cmap = 'gray')
plt.title('Img3'), plt.xticks([]), plt.yticks([])

plt.subplot(125),plt.imshow(edges_im_4,cmap = 'gray')
plt.title('Img4'), plt.xticks([]), plt.yticks([])

plt.subplot(126),plt.imshow(edges_im_5,cmap = 'gray')
plt.title('Img5'), plt.xticks([]), plt.yticks([])

plt.subplot(127),plt.imshow(edges_im_6,cmap = 'gray')
plt.title('Img6'), plt.xticks([]), plt.yticks([])

plt.subplot(128),plt.imshow(edges_im_7,cmap = 'gray')
plt.title('Img7'), plt.xticks([]), plt.yticks([])

plt.subplot(129),plt.imshow(edges_im_8,cmap = 'gray')
plt.title('Img8'), plt.xticks([]), plt.yticks([])

plt.subplot(130),plt.imshow(edges_im_9,cmap = 'gray')
plt.title('Img9'), plt.xticks([]), plt.yticks([])

plt.subplot(131),plt.imshow(edges_im_10,cmap = 'gray')
plt.title('Img10'), plt.xticks([]), plt.yticks([])

plt.subplot(131),plt.imshow(edges_im_11,cmap = 'gray')
plt.title('Img11'), plt.xticks([]), plt.yticks([])

plt.show()

##hansen algo start
def get(s):
    data = imread(s)
    data = sp.inner(data, [0.299, 0.587, 0.114])
    return (data - data.mean()) / data.std()

imAmz = get('./data/images/seasoning_images/edgesFromAmazon.jpg')
imSpy = get('./data/images/seasoning_images/edgesFromShopify.jpg')
im1 = get('./data/images/seasoning_images/edgesFromImg1.jpg')
im2 = get('./data/images/seasoning_images/edgesFromImg2.jpg')
im3 = get('./data/images/seasoning_images/edgesFromImg3.jpg')
im4 = get('./data/images/seasoning_images/edgesFromImg4.jpg')
im5 = get('./data/images/seasoning_images/edgesFromImg5.jpg')
im6 = get('./data/images/seasoning_images/edgesFromImg6.jpg')
im7 = get('./data/images/seasoning_images/edgesFromImg7.jpg')
im8 = get('./data/images/seasoning_images/edgesFromImg8.jpg')
im9 = get('./data/images/seasoning_images/edgesFromImg9.jpg')
im10 = get('./data/images/seasoning_images/edgesFromImg10.jpg')
im11 = get('./data/images/seasoning_images/edgesFromImg11.jpg')


imAmzAmz = c2d(imAmz, imAmz, mode='same')
imAmzSpy = c2d(imAmz, imSpy, mode='same')

print 'Image From Amazon vs Image From Amazon %f' % imAmzAmz.max()
print 'Image From Amazon vs Image From Shopify %f' % imAmzSpy.max()

