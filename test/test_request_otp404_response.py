# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.request_otp404_response import RequestOtp404Response  # noqa: E501

class TestRequestOtp404Response(unittest.TestCase):
    """RequestOtp404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestOtp404Response:
        """Test RequestOtp404Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestOtp404Response`
        """
        model = RequestOtp404Response()  # noqa: E501
        if include_optional:
            return RequestOtp404Response(
                code = '',
                reason = ''
            )
        else:
            return RequestOtp404Response(
                reason = '',
        )
        """

    def testRequestOtp404Response(self):
        """Test RequestOtp404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
