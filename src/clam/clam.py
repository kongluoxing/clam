# coding: utf-8
#
# Copyright 2014, Kong Luoxing<kong.luoxing@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from models import Sample
from abstracts import Index

log = logging.getLogger('Clam')


class DataValidationError(Exception):
    pass


class Clam(object):
    def __init__(self, user=None):
        log.warn('User not specified, will generate full index.')
        self.user = user
        self.index = Index(user)

    @staticmethod
    def validate(data):

        """
        validate data format

        :param data: list or dict of sample data
        :raise DataValidationError:
        """
        if not isinstance(data, list) or not isinstance(data, dict):
            err_msg = 'Clam only accept dict or list object, {} found.'.format(type(data))
            raise DataValidationError(err_msg)

        if not (data.get('timestamp') and data.get('resource') and data.get('name')
                and data.get('value') and data.get('type')):
            raise DataValidationError('Required field is not all provided.')

    def collate(self, data):
        """
        write data to cassnadra

        :param data: list or dict of sample data
        :raise DataValidationError:
        """
        self.validate(data)

        data = [data] if isinstance(data, dict) else data

        for sample in data:
            s = Sample(partition=1,
                       collect_at=sample['timestamp'],
                       resource=sample['resource'],
                       metric_name=sample['name'],
                       type=sample['type'],
                       attribute=sample.get('attribute'),
                       value=sample['value']
                       )
            s.save()

    if __name__ == '__main__':
        pass
