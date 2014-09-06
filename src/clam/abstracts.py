# coding: utf-8
#
# Copyright 2014, Kong Luoxing<kong.luoxing@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# import python libs
import logging


class Sample(object):
    def __init__(self, timestamp, resource, name, type, value, attribute=None):
        pass

    def __str__(self):
        pass


class SampleResponsitory(object):
    def select(self, resource, descriptor, resolution, start=None, end=None):
        pass

    def insert(self, samples):
        pass


class Resource(object):
    def __init__(self, resource_id, attribute=None):
        self.resource_id = resource_id
        self.attribute = attribute

    def __str__(self):
        pass

    def __eq__(self, other):
        pass


class Index(object):
    def __init__(self, user=None):
        pass

    def search(self, path):
        pass


class ResourcePath(object):
    def __init__(self, name, resource_index, parent=None):
        self.name = name
        self.index = resource_index
        self.parent = parent

    def get_children(self):
        pass

    def get_metrics(self):
        pass

    @staticmethod
    def get_full_name(path):
        pass

    @staticmethod
    def is_root(path):
        pass

    def __str__(self):
        return self.name

    def __add__(self, other):
        pass


class ResourceIndex(object):
    DELEMETER = '/'
    ROOT_KEY = '<|> ROOT RESOURCE PATH <|>'
    TTL = None

    def __init__(self, index_state, registry):
        pass

    def get_children(self):
        pass

    def search(self, path):
        pass

    def get_metrics(self, resource_name):
        pass

    def index(self, data):
        pass

    def __add__(self, other):
        pass


class IndexState(object):
    def put(self, resource, metric):
        pass

    def put_all(self, data):
        pass

    def exists(self, resource, metric):
        pass


class SampleProcessor(object):
    log = logging.getLogger(__name__)

    def __init__(self, resource_index):
        pass

    def submit(self, samples):
        pass

    def collate(self, samples):
        pass
