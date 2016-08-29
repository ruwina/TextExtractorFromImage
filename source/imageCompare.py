#import packages

from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)

	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()

# load the images of dog
dogOne = cv2.imread("./data/images/dogs/dogOne.png")
dogTwo = cv2.imread("./data/images/dogs/dogTwo.jpg")
dogThree = cv2.imread("./data/images/dogs/dogThree.jpg")
dogFour = cv2.imread("./data/images/dogs/dogFour.jpg")
dogFive = cv2.imread("./data/images/dogs/dogFive.jpg")
dogSix = cv2.imread("./data/images/dogs/dogSix.jpg")

# convert the images to grayscale
dogOne = cv2.cvtColor(dogOne, cv2.COLOR_BGR2GRAY)
dogTwo = cv2.cvtColor(dogTwo, cv2.COLOR_BGR2GRAY)
dogThree = cv2.cvtColor(dogThree, cv2.COLOR_BGR2GRAY)
dogFour = cv2.cvtColor(dogFour, cv2.COLOR_BGR2GRAY)
dogFive = cv2.cvtColor(dogFive, cv2.COLOR_BGR2GRAY)
dogSix = cv2.cvtColor(dogSix, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig_dogs = plt.figure("Dog Images")
images_dogs = ("Dog 1", dogOne), ("Dog 2", dogTwo), ("Dog 3", dogThree), ("Dog 4", dogFour), ("Dog 5", dogFive), ("Dog 6", dogSix)

# loop over the images
for (i, (name, images_dogs)) in enumerate(images_dogs):
	# show the image
	ax = fig_dogs.add_subplot(1, 6, i + 1)
	ax.set_title(name)
	plt.imshow(images_dogs, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()

# compare the dog images
compare_images(dogOne, dogOne, "Dog One vs. Dog One")
compare_images(dogOne, dogTwo, "Dog One vs. Dog Two")
compare_images(dogOne, dogThree, "Dog One vs. Dog Three")
compare_images(dogOne, dogFour, "Dog One vs. Dog Four")
compare_images(dogOne, dogFive, "Dog One vs. Dog Five")
compare_images(dogOne, dogSix, "Dog One vs. Dog Six")

# load the images of flags of nepal
flagOne = cv2.imread("./data/images/nepal_flags/flagOne.jpg")
flagTwo = cv2.imread("./data/images/nepal_flags/flagTwo.jpg")
flagThree = cv2.imread("./data/images/nepal_flags/flagThree.png")
flagFour = cv2.imread("./data/images/nepal_flags/flagFour.png")
flagFive = cv2.imread("./data/images/nepal_flags/flagFive.jpg")

# convert the images to grayscale
flagOne = cv2.cvtColor(flagOne, cv2.COLOR_BGR2GRAY)
flagTwo = cv2.cvtColor(flagTwo, cv2.COLOR_BGR2GRAY)
flagThree = cv2.cvtColor(flagThree, cv2.COLOR_BGR2GRAY)
flagFour = cv2.cvtColor(flagFour, cv2.COLOR_BGR2GRAY)
flagFive = cv2.cvtColor(flagFive, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig_flags = plt.figure("Flag Images")
images_flags = ("Flag 1", flagOne), ("Flag 2", flagTwo), ("Flag 3", flagThree), ("Flag 4", flagFour), ("Flag 5", flagFive)

# loop over the images
for (i, (name, images_flags)) in enumerate(images_flags):
	# show the image
	ax = fig_flags.add_subplot(1, 5, i + 1)
	ax.set_title(name)
	plt.imshow(images_flags, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()


# compare the dog images with flag images
compare_images(dogOne, flagOne, "Dog One vs. Flag One")
compare_images(dogOne, flagTwo, "Dog One vs. Flag Two")
compare_images(dogOne, flagThree, "Dog One vs. Flag Three")
compare_images(dogOne, flagFour, "Dog One vs. Flag Four")
compare_images(dogOne, flagFive, "Dog One vs. Flag Five")


# load the images of dog
wolfOne = cv2.imread("./data/images/wolves/wolfOne.jpg")
wolfTwo = cv2.imread("./data/images/wolves/wolfTwo.jpg")
wolfThree = cv2.imread("./data/images/wolves/wolfThree.jpg")
wolfFour = cv2.imread("./data/images/wolves/wolfFour.jpg")
wolfFive = cv2.imread("./data/images/wolves/wolfFive.jpg")
wolfSix = cv2.imread("./data/images/wolves/wolfSix.jpg")

# convert the images to grayscale
wolfOne = cv2.cvtColor(wolfOne, cv2.COLOR_BGR2GRAY)
wolfTwo = cv2.cvtColor(wolfTwo, cv2.COLOR_BGR2GRAY)
wolfThree = cv2.cvtColor(wolfThree, cv2.COLOR_BGR2GRAY)
wolfFour = cv2.cvtColor(wolfFour, cv2.COLOR_BGR2GRAY)
wolfFive = cv2.cvtColor(wolfFive, cv2.COLOR_BGR2GRAY)
wolfSix = cv2.cvtColor(wolfSix, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig_wolves = plt.figure("Wolf Images")
images_wolves = ("Wolf 1", wolfOne), ("Wolf 2", wolfTwo), ("Wolf 3", wolfThree), ("Wolf 4", wolfFour), ("Wolf 5", wolfFive), ("Wolf 6", wolfSix)

# loop over the images
for (i, (name, images_wolves)) in enumerate(images_wolves):
	# show the image
	ax = fig_wolves.add_subplot(1, 6, i + 1)
	ax.set_title(name)
	plt.imshow(images_wolves, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()

# compare the dog images with wolves
compare_images(dogOne, wolfOne, "Dog One vs. Wolf One")
compare_images(dogOne, wolfTwo, "Dog One vs. Wolf Two")
compare_images(dogOne, wolfThree, "Dog One vs. Wolf Three")
compare_images(dogOne, wolfFour, "Dog One vs. Wolf Four")
compare_images(dogOne, wolfFive, "Dog One vs. Wolf Five")
compare_images(dogOne, wolfSix, "Dog One vs. Wolf Six")

