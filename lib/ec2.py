#!/Users/lio/PycharmProjects/events_handler/bin/python3
# -*- coding:utf-8 _*-  
""" 
@author: lizzano 
@license: Apache Licence 
@file: ec2.py 
@time: 2019/07/19
@contact: zlprasy@gmail.com
@site:  
@software: PyCharm 
"""


class EC2(object):
    def __init__(self, client):
        self.client = client

    def terminated(self, instance_id):
        try:
            self.client.terminate_instances(InstanceIds=instance_id if isinstance(instance_id, list) else list(instance_id))
            return 'ok'
        except Exception as e:
            print(e)

    def running(self, instance_id):
        try:
            # self.client.start_instances(InstanceIds=instance_id if isinstance(instance_id, list) else list(instance_id))
            print('running instance: %s' % instance_id)
            return 'ok'
        except Exception as e:
            print(e)


def events_handler(*args, **kwargs):
    return getattr(EC2(kwargs.get('client')), kwargs.get('state'))(kwargs.get('instance-id'))
