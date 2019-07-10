#!/usr/bin/env python
"""
  This module tests the function of Polygon vertices Generation.
  TODO test_concavePolygon and test_convexPolygon
"""


import os
import unittest
import sys
from set_para import filename, root
from set_para import polygonOutputPath
from set_para import get_image, get_path, validate

if not os.path.exists(polygonOutputPath):
    os.makedirs(polygonOutputPath)

try:
    # try using the installed blocksWorld if available
    from blocksWorld import *
except ImportError:
    # blocksWorld not installed
    blocksWorldPath = os.path.join(root, "..")
    blocksWorldPath = os.path.abspath(blocksWorldPath)
    sys.path.append(blocksWorldPath)
    from blocksWorld import *


class test_polygon(unittest.TestCase):
    """
    Plotting Images for different types of polygons.
    """

    # Result images for regularPolygon.
    def test_regularPolygon(self):
        # Result image for regularPolygon
        regularImage, regularCanvas = get_image('L', (480, 640), 'white')

        draw(regularCanvas, regularPolygon(3, np.array([160, 120]), 50), '3')
        draw(regularCanvas, regularPolygon(4, np.array([480, 120]), 90), '4')
        draw(regularCanvas, regularPolygon(5, np.array([420, 360]), 60), '5')
        draw(regularCanvas, regularPolygon(6, np.array([160, 360]), 80), '6')
        draw(regularCanvas, regularPolygon(7, np.array([320, 160]), 70), '7')

        image_name = filename(sys._getframe().f_code.co_name)

        regularImage.save(image_name)
        regularImage.close()

        result_file, reference_file = get_path(image_name)

        # compare results against reference data
        validate(reference_file,result_file)

    def test_regularRotatedPolygon(self):
        # Result image for regularPolygon with rotated points
        regularRotatedImage, regularRotatedCanvas = get_image('L', (480, 640), 'white')

        center = np.array([320, 240])
        draw(regularRotatedCanvas, [center], 'center')
        draw(regularRotatedCanvas, (rotate((regularPolygon(3, np.array([160, 120]), 50)), center, 45.0)), '3r')
        draw(regularRotatedCanvas, (rotate((regularPolygon(4, np.array([480, 120]), 90)), center, 45.0)), '4r')
        draw(regularRotatedCanvas, (rotate((regularPolygon(5, np.array([420, 360]), 60)), center, 45.0)), '5r')
        draw(regularRotatedCanvas, (rotate((regularPolygon(6, np.array([160, 360]), 80)), center, 45.0)), '6r')
        draw(regularRotatedCanvas, (rotate((regularPolygon(7, np.array([320, 160]), 70)), center, 45.0)), '7r')

        image_name = filename(sys._getframe().f_code.co_name)

        regularRotatedImage.save(image_name)
        regularRotatedImage.close()

        result_file, reference_file = get_path(image_name)
        # compare results against reference data
        validate(reference_file, result_file)

    def test_regularWiredPolygon(self):
        # Result image for regularPolygon with wire
        regularWiredImage, regularWiredCanvas = get_image('L', (480, 640), 'white')

        drawWire(regularWiredCanvas, regularPolygon(3, np.array([160, 120]), 50))
        drawWire(regularWiredCanvas, regularPolygon(4, np.array([480, 120]), 90))
        drawWire(regularWiredCanvas, regularPolygon(5, np.array([420, 360]), 60))
        drawWire(regularWiredCanvas, regularPolygon(6, np.array([160, 360]), 80))
        drawWire(regularWiredCanvas, regularPolygon(7, np.array([320, 160]), 70))

        image_name = filename(sys._getframe().f_code.co_name)

        regularWiredImage.save(image_name)
        regularWiredImage.close()

        result_file, reference_file = get_path(image_name)
        # compare results against reference data
        validate(reference_file, result_file)

    def test_regularRotatedWiredPolygon(self):
        # Result image for regularPolygon using rotated points with wire
        regularRotatedWiredImage, regularRotatedWiredCanvas = get_image('L', (480, 640), 'white')
        center = np.array([320, 240])
        draw(regularRotatedWiredCanvas, [center], 'center')

        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(3, np.array([160, 120]), 50)), center, 45.0)))
        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(4, np.array([480, 120]), 90)), center, 45.0)))
        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(5, np.array([420, 360]), 60)), center, 45.0)))
        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(6, np.array([160, 360]), 80)), center, 45.0)))
        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(7, np.array([320, 160]), 70)), center, 45.0)))

        image_name = filename(sys._getframe().f_code.co_name)

        regularRotatedWiredImage.save(image_name)
        regularRotatedWiredImage.close()

        result_file, reference_file = get_path(image_name)
        # compare results against reference data
        validate(reference_file, result_file)

    def test_polygonshape(self):
        # Result image for combined shapes
        shapeImage, shapeCanvas = get_image('L', (480, 640), 'white')
        center = np.array([320, 240])

        drawWire(shapeCanvas, (rotate((regularPolygon(3, np.array([320, 240]), 110)), np.array([450, 200]), 30.0)))
        drawWire(shapeCanvas, (rotate((regularPolygon(4, np.array([320, 240]), 120)), center, 45.0)))

        image_name = filename(sys._getframe().f_code.co_name)

        shapeImage.save(image_name)
        shapeImage.close()

        result_file, reference_file = get_path(image_name)
        # compare results against reference data
        validate(reference_file, result_file)

    def test_convexPolygon(self):
        pass
        # TODO

    def test_concavePolygon(self):
        pass
        # TODO

    def test_randomPolygon(self):

        randomImage, randomCanvas= get_image('L', (480, 640), 'white')
        seed = 5
        draw(randomCanvas, randomPolygon(seed, 3, np.array([160, 120]), 200), '3r')
        draw(randomCanvas, randomPolygon(seed, 4, np.array([480, 120]), 200), '4r')
        draw(randomCanvas, randomPolygon(seed, 5, np.array([480, 360]), 200), '5r')
        draw(randomCanvas, randomPolygon(seed, 6, np.array([160, 360]), 200), '6r')
        draw(randomCanvas, randomPolygon(seed, 7, np.array([320, 240]), 200), '7r')

        image_name = filename(sys._getframe().f_code.co_name)

        randomImage.save(image_name)
        randomImage.close()

        result_file, reference_file = get_path(image_name)
        # compare results against reference data
        validate(reference_file, result_file)

    def test_randomRotatedPolygon(self):

        randomRotatedImage, randomRotatedCanvas = get_image('L', (480, 640), 'white')

        center = np.array([320, 240])
        draw(randomRotatedCanvas, [center], 'center')

        seed = 5
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 3, np.array([160, 120]), 50)), center, 90.0)), '3r')
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 4, np.array([480, 120]), 90)), center, 90.0)), '4r')
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 5, np.array([420, 360]), 60)), center, 90.0)), '5r')
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 6, np.array([160, 360]), 80)), center, 90.0)), '6r')
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 7, np.array([320, 160]), 70)), center, 90.0)), '7r')

        image_name = filename(sys._getframe().f_code.co_name)

        randomRotatedImage.save(image_name)
        randomRotatedImage.close()

        result_file, reference_file = get_path(image_name)
        # compare results against reference data
        validate(reference_file, result_file)


if __name__ == '__main__':
    unittest.main()
