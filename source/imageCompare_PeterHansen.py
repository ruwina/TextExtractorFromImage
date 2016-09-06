import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d

def getWolves(s):
    data = imread('./data/images/wolves/' + s)
    data = sp.inner(data, [0.299, 0.587, 0.114])
    return (data - data.mean()) / data.std()
wl1 = getWolves('wolfOne.jpg')
wl2 = getWolves('wolfTwo.jpg')
wl3 = getWolves('wolfThree.jpg')
wl4 = getWolves('wolfFour.jpg')
wl5 = getWolves('wolfFive.jpg')
wl6 = getWolves('wolfSix.jpg')

# w11 = c2d(wl1, wl1, mode='same')
# w12 = c2d(wl1, wl2, mode='same')
# w13 = c2d(wl1, wl3, mode='same')
# w14 = c2d(wl1, wl4, mode='same')
# w15 = c2d(wl1, wl5, mode='same')
# w16 = c2d(wl1, wl6, mode='same')
#
# w23 = c2d(wl2, wl3, mode='same')
# w24 = c2d(wl2, wl4, mode='same')
# w25 = c2d(wl2, wl5, mode='same')
# w26 = c2d(wl2, wl6, mode='same')
#
# w34 = c2d(wl3, wl4, mode='same')
# w35 = c2d(wl3, wl5, mode='same')
# w36 = c2d(wl3, wl6, mode='same')
#
# w45 = c2d(wl4, wl5, mode='same')
# w46 = c2d(wl4, wl6, mode='same')
#
# w56 = c2d(wl5, wl6, mode='same')

# print 'Wolf 1 vs Wolf 1 %f' % w11.max()
# print 'Wolf 1 vs Wolf 2 %f' % w12.max()
# print 'Wolf 1 vs Wolf 3 %f' % w13.max()
# print 'Wolf 1 vs Wolf 4 %f' % w14.max()
# print 'Wolf 1 vs Wolf 5 %f' % w15.max()
# print 'Wolf 1 vs Wolf 6 %f' % w16.max()
#
# print 'Wolf 2 vs Wolf 3 %f' % w23.max()
# print 'Wolf 2 vs Wolf 4 %f' % w24.max()
# print 'Wolf 2 vs Wolf 5 %f' % w25.max()
# print 'Wolf 2 vs Wolf 6 %f' % w26.max()
#
# print 'Wolf 3 vs Wolf 4 %f' % w34.max()
# print 'Wolf 3 vs Wolf 5 %f' % w35.max()
# print 'Wolf 3 vs Wolf 6 %f' % w36.max()
#
# print 'Wolf 4 vs Wolf 5 %f' % w45.max()
# print 'Wolf 4 vs Wolf 6 %f' % w46.max()
#
# print 'Wolf 5 vs Wolf 6 %f' % w56.max()


def getDogs(s):
    data = imread('./data/images/dogs/'+s)
    data = sp.inner(data, [0.299, 0.587, 0.114])
    return (data - data.mean()) / data.std()

im1 = getDogs('dogOne.jpg')
im2 = getDogs('dogTwo.jpg')
im3 = getDogs('dogThree.jpg')
im4 = getDogs('dogFour.jpg')
im5 = getDogs('dogFive.jpg')
im6 = getDogs('dogSix.jpg')

# c11 = c2d(im1, im1, mode='same')
# c12 = c2d(im1, im2, mode='same')
# c13 = c2d(im1, im3, mode='same')
# c14 = c2d(im1, im4, mode='same')
# c15 = c2d(im1, im5, mode='same')
# c16 = c2d(im1, im6, mode='same')
#
# c23 = c2d(im2, im3, mode='same')
# c24 = c2d(im2, im4, mode='same')
# c25 = c2d(im2, im5, mode='same')
# c26 = c2d(im2, im6, mode='same')
#
# c34 = c2d(im3, im4, mode='same')
# c35 = c2d(im3, im5, mode='same')
# c36 = c2d(im3, im6, mode='same')
#
# c45 = c2d(im4, im5, mode='same')
# c46 = c2d(im4, im6, mode='same')
#
# c56 = c2d(im5, im6, mode='same')

dog1wolf1 = c2d(im1, wl1, mode='same')
dog1wolf2 = c2d(im1, wl2, mode='same')
dog1wolf3 = c2d(im1, wl3, mode='same')
dog1wolf4 = c2d(im1, wl4, mode='same')
dog1wolf5 = c2d(im1, wl5, mode='same')
dog1wolf6 = c2d(im1, wl6, mode='same')

dog4wolf1 = c2d(im4, wl1, mode='same')
dog4wolf2 = c2d(im4, wl2, mode='same')
dog4wolf3 = c2d(im4, wl3, mode='same')
dog4wolf4 = c2d(im4, wl4, mode='same')
dog4wolf5 = c2d(im4, wl5, mode='same')
dog4wolf6 = c2d(im4, wl6, mode='same')


print 'Dog 1 vs Wolf 1 %f' % dog1wolf1.max()
print 'Dog 1 vs Wolf 2 %f' % dog1wolf2.max()
print 'Dog 1 vs Wolf 3 %f' % dog1wolf3.max()
print 'Dog 1 vs Wolf 4 %f' % dog1wolf4.max()
print 'Dog 1 vs Wolf 5 %f' % dog1wolf5.max()
print 'Dog 1 vs Wolf 6 %f' % dog1wolf6.max()

print 'Dog 4 vs Wolf 3 %f' % dog4wolf1.max()
print 'Dog 4 vs Wolf 4 %f' % dog4wolf2.max()
print 'Dog 4 vs Wolf 5 %f' % dog4wolf3.max()
print 'Dog 4 vs Wolf 6 %f' % dog4wolf4.max()
print 'Dog 4 vs Wolf 5 %f' % dog4wolf5.max()
print 'Dog 4 vs Wolf 6 %f' % dog4wolf6.max()


# def getFlags(s):
#     data = imread('./data/images/nepal_flags/' + s)
#     data = sp.inner(data, [0.299, 0.587, 0.114])
#     return (data - data.mean()) / data.std()
# fl1 = getFlags('flagOne.jpg')
# fl2 = getFlags('flagTwo.jpg')
# fl3 = getFlags('flagThree.jpg')
# fl4 = getFlags('flagFour.jpg')
# fl5 = getFlags('flagFive.jpg')
#
# f11 = c2d(fl1, fl1, mode='same')
# f12 = c2d(fl1, fl2, mode='same')
# f13 = c2d(fl1, fl3, mode='same')
# f14 = c2d(fl1, fl4, mode='same')
# f15 = c2d(fl1, fl5, mode='same')
#
# f23 = c2d(fl2, fl3, mode='same')
# f24 = c2d(fl2, fl4, mode='same')
# f25 = c2d(fl2, fl5, mode='same')
#
# f34 = c2d(fl3, fl4, mode='same')
# f35 = c2d(fl3, fl5, mode='same')
#
# f45 = c2d(fl4, fl5, mode='same')
#
# print 'Flag 1 vs Flag 1 %f' % f11.max()
# print 'Flag 1 vs Flag 2 %f' % f12.max()
# print 'Flag 1 vs Flag 3 %f' % f13.max()
# print 'Flag 1 vs Flag 4 %f' % f14.max()
# print 'Flag 1 vs Flag 5 %f' % f15.max()
#
# print 'Flag 2 vs Flag 3 %f' % f23.max()
# print 'Flag 2 vs Flag 4 %f' % f24.max()
# print 'Flag 2 vs Flag 5 %f' % f25.max()
#
# print 'Flag 3 vs Flag 4 %f' % f34.max()
# print 'Flag 3 vs Flag 5 %f' % f35.max()
#
# print 'Flag 4 vs Flag 5 %f' % f45.max()
#
# def get(s):
#     data = imread('./data/images/' + s)
#     data = sp.inner(data, [0.299, 0.587, 0.114])
#     return (data - data.mean()) / data.std()
# img1 = get('imageFromAmazon.jpg')
# img2 = get('imageFromShopify.jpg')
# img3 = get('games.jpg')
#
#
# img11 = c2d(img1, img1, mode='same')
# img12 = c2d(img1, img2, mode='same')
# img13 = c2d(img1, img3, mode='same')
#
# img23 = c2d(img2, img3, mode='same')
#
# print 'Image From Amazon vs Image From Amazon %f' % img11.max()
# print 'Image From Amazon vs Image From Shopify %f' % img12.max()
# print 'Image From Amazon vs Random Image %f' % img13.max()
#
# print 'Image From Shopify vs Random Image %f' % img23.max()
