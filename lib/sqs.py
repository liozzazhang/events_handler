#!/Users/lio/PycharmProjects/events_handler/bin/python3
# -*- coding:utf-8 _*-  
""" 
@author: lizzano 
@license: Apache Licence 
@file: sqs.py 
@time: 2019/07/19
@contact: zlprasy@gmail.com
@site:  
@software: PyCharm 
"""


class SQS(object):

    def __init__(self, client):
        pass


def events_handler(*args, **kwargs):
    return getattr(SQS(kwargs.get('client')), kwargs.get('state'))(kwargs.get('instance-id'))