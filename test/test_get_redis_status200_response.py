# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.get_redis_status200_response import GetRedisStatus200Response  # noqa: E501

class TestGetRedisStatus200Response(unittest.TestCase):
    """GetRedisStatus200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRedisStatus200Response:
        """Test GetRedisStatus200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRedisStatus200Response`
        """
        model = GetRedisStatus200Response()  # noqa: E501
        if include_optional:
            return GetRedisStatus200Response(
                reason = '',
                status = True
            )
        else:
            return GetRedisStatus200Response(
                status = True,
        )
        """

    def testGetRedisStatus200Response(self):
        """Test GetRedisStatus200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
