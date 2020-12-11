#
# Copyright 2018 Fiberhome
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from mogan.tests.functional.api import v1 as v1_test
from mogan.tests.unit.db import utils


class TestAvailabilityZoneAuthorization(v1_test.APITestV1):

    def setUp(self):
        super(TestAvailabilityZoneAuthorization, self).setUp()
        self.agg = utils.create_test_aggregate()
        self.metadata = {'availability_zone': 'az1'}
        self.agg_meta = utils.create_test_aggregate_metadata(
            aggregate_id=self.agg.id, metadata=self.metadata)

    def test_get_availability_zones_by_admin(self):
        headers = self.gen_headers(self.context, roles="admin")
        resp = self.get_json('/availability_zones', headers=headers)
        self.assertIn(self.metadata['availability_zone'],
                      resp['availability_zones'])
