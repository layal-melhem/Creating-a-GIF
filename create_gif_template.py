import imageio.v3 as iio

filenames = [] # list of image filenames
images = [] # empty list

for filename in filenames:
  images.append(iio.imread(filename))

# (filename of the gif you want to create, empty list name, duration in milliseconds, loop)
iio.imwrite('', images, duration = 150, loop = 0) # loop = 0 allows for infinite looping