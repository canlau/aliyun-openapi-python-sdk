# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ReceiveNotifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'ReceiveNotify','rtc')

	def get_TraceId(self):
		return self.get_query_params().get('TraceId')

	def set_TraceId(self,TraceId):
		self.add_query_param('TraceId',TraceId)

	def get_Content(self):
		return self.get_query_params().get('Content')

	def set_Content(self,Content):
		self.add_query_param('Content',Content)

	def get_Event(self):
		return self.get_query_params().get('Event')

	def set_Event(self,Event):
		self.add_query_param('Event',Event)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ContentType(self):
		return self.get_query_params().get('ContentType')

	def set_ContentType(self,ContentType):
		self.add_query_param('ContentType',ContentType)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)