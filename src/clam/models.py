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

from cqlengine import columns
from cqlengine import Model


class Sample(Model):
    __keyspace__ = 'clam'
    __table_name__ = 'samples'

    partition = columns.Integer(primary_key=True)
    resource = columns.Text(primary_key=True)
    collected_at = columns.DateTime(primary_key=True)
    metric_name = columns.Text(primary_key=True)
    type = columns.Text(required=True)
    value = columns.Blob()
    attributes = columns.Map(columns.Text, columns.Text)


class ResourceIndex(Model):
    __keyspace__ = 'clam'
    __table_name__ = 'resource_idx'
    parent = columns.Text(primary_key=True)
    child = columns.Text(primary_key=True)


class MetricIndex(Model):
    __keyspace__ = 'clam'
    __table_name__ = 'metric_idx'
    resource = columns.Text(primary_key=True)
    metric_name = columns.Text(primary_key=True)
