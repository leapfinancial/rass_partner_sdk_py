# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.validate_phone_number_request import ValidatePhoneNumberRequest  # noqa: E501

class TestValidatePhoneNumberRequest(unittest.TestCase):
    """ValidatePhoneNumberRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidatePhoneNumberRequest:
        """Test ValidatePhoneNumberRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidatePhoneNumberRequest`
        """
        model = ValidatePhoneNumberRequest()  # noqa: E501
        if include_optional:
            return ValidatePhoneNumberRequest(
                country = '',
                phone = ''
            )
        else:
            return ValidatePhoneNumberRequest(
                country = '',
                phone = '',
        )
        """

    def testValidatePhoneNumberRequest(self):
        """Test ValidatePhoneNumberRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
