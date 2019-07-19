#!/Users/lio/PycharmProjects/events_handler/bin/python3
# -*- coding:utf-8 _*-  
""" 
@author: lizzano 
@license: Apache Licence 
@file: base.py 
@time: 2019/07/19
@contact: zlprasy@gmail.com
@site:  
@software: PyCharm 
"""
import collections
import json
import boto3
import re
import os


def format_event(event):
    try:
        if isinstance(event, dict):
            for k, v in event.items():
                if isinstance(v, (collections.Mapping, list, tuple)):
                    event[k] = format_event(v)
                else:
                    try:
                        event[k] = format_event(json.loads(v))
                    except Exception:
                        continue
        elif isinstance(event, (list, tuple)):
            for i in event:
                index = event.index(i)
                event.remove(i)
                if isinstance(i, (collections.Mapping, list, tuple)):
                    event.insert(index, format_event(i))
                else:
                    try:
                        print(i)
                        event.insert(index, format_event(json.load(i)))
                    except (AttributeError, ValueError):
                        continue
        return event
    except TypeError as e:
        raise e
    except Exception as e:
        raise e


def boto3_client(profile=None):
    _session = None
    if profile:
        _profile_config = '{}/.aws/config'.format(os.environ.get('HOME'))
        if os.path.isfile(_profile_config):
            with open(_profile_config, 'r') as f:
                content = f.readlines()
                for line in content:
                    if re.search(r'{}]'.format(profile), line):
                        _session = boto3.Session(profile_name=profile)
                        break
    if not _session:
        _session = boto3.Session()
    return {
        'elbv2': _session.client('elbv2'),
        'sns': _session.client('sns'),
        'sqs': _session.client('sqs'),
        's3': _session.client('s3'),
        'autoscaling': _session.client('autoscaling'),
        'ecs': _session.client('ecs'),
        'cw': _session.client('cloudwatch')
    }


def notification(message):
    print("notification %s" % message)