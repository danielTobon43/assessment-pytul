import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid


def visualize(raw_images, predictions, labelmap):
    # pyplot object to display an image
    fig = plt.figure(figsize=(7.0, 4.0))

    # grid object to store each image
    grid = ImageGrid(fig, 111, nrows_ncols=(3, 4), axes_pad=0.5)

    # display 12 images in a grid
    for i, (ax, im) in enumerate(zip(grid, raw_images)):
        ax.set_title(labelmap[predictions[i]])
        ax.imshow(im)
