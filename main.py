#!/Users/lio/PycharmProjects/events_handler/bin/python3
# -*- coding:utf-8 _*-  
""" 
@author: lizzano 
@license: Apache Licence 
@file: main.py 
@time: 2019/07/19
@contact: zlprasy@gmail.com
@site:  
@software: PyCharm 
"""
from lib.base import *


def events_entrance(event, context):
    event = format_event(event)
    _client = boto3_client('hk')
    for _event in event.get('Records'):

        print("start to process message: {}".format(_event))  # 实际应用应以logger代替print方法
        try:

            _aws_service = _event.get('body').get('Message').get('source')
            if _aws_service:
                _aws_service = _aws_service.split('.')[-1]

            else:
                continue
            _detail = _event.get('body').get('Message').get('detail')
            _detail.update({'client': _client.get(_aws_service)})
            response = getattr(__import__('lib.' + _aws_service, fromlist=True), 'events_handler')(**_detail)
            notification(response)
        except Exception as err:
            print(err)
            raise err


if __name__ == '__main__':
    sample_events = {
        'Records': [{
            'body': {
                'Message': {
                    "id": "7bf73129-1428-4cd3-a780-95db273d1602",
                    "detail-type": "EC2 Instance State-change Notification",
                    "source": "aws.ec2",
                    "account": "123456789012",
                    "time": "2015-11-11T21:29:54Z",
                    "region": "us-east-1",
                    "resources": [
                        "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"
                    ],
                    "detail": {
                        "instance-id": "i-abcd1111",
                        "state": "running"
                    }
                }
            }
        }]
    }
    events_entrance(sample_events, context='')
