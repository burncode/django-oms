# -*- coding: utf-8 -*-
# author: itimor

import os
from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, file):
        filename = os.path.splitext(file)
        last_filename = "%s-%s%s" % (filename[0], instance.create_time, filename[1])
        return os.path.join(self.path, instance.archive, last_filename)
        # archive = instance.archive.split('/')
        # if len(archive)>2:
        #     return os.path.join(self.path, archive[1], archive[2], filename)
        # else:
        #     return os.path.join(self.path, archive[1], filename)



# def path_and_rename(path):
#     def wrapper(instance, filename):
#         ext = os.path.splitext(filename)[1]
#         if ext:
#             filename = "%s-%s%s" % (instance.username, instance.create_time, ext)
#         else:
#             filename = "%s-%s%s" % (instance.username, instance.create_time, '.png')
#
#         archive = instance.archive.split('/')
#         if len(archive)>2:
#             return os.path.join(path, archive[1], archive[2], filename)
#         else:
#             return os.path.join(path, archive[1], filename)
#     return wrapper