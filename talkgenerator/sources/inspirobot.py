import random

from talkgenerator.util import os_util


def get_random_inspirobot_image(_):
    # Generate a random url to access inspirobot
    dd = str(random.randint(1, 73)).zfill(2)
    nnnn = random.randint(0, 9998)
    inspirobot_url = ('http://generated.inspirobot.me/'
                      '0{}/aXm{}xjU.jpg').format(dd, nnnn)

    # Download the image
    image_url = os_util.to_actual_file('../downloads/inspirobot/{}-{}.jpg'.format(dd, nnnn), __file__)
    os_util.download_image(inspirobot_url, image_url)

    return image_url
