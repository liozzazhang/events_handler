#!/Users/lio/PycharmProjects/events_handler/bin/python3
# -*- coding:utf-8 _*-  
""" 
@author: lizzano 
@license: Apache Licence 
@file: s3.py 
@time: 2019/07/19
@contact: zlprasy@gmail.com
@site:  
@software: PyCharm 
"""


class S3(object):

    def __init__(self, client):
        pass


def events_handler(*args, **kwargs):
    return getattr(S3(kwargs.get('client')), kwargs.get('state'))(kwargs.get('instance-id'))