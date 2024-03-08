# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpyv2.models.validate_error import ValidateError  # noqa: E501

class TestValidateError(unittest.TestCase):
    """ValidateError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateError:
        """Test ValidateError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateError`
        """
        model = ValidateError()  # noqa: E501
        if include_optional:
            return ValidateError(
                name = '',
                message = '',
                stack = '',
                status = 1.337,
                fields = {
                    'key' : raassdkpyv2.models.field_errors_value.FieldErrors_value(
                        value = null, 
                        message = '', )
                    }
            )
        else:
            return ValidateError(
                name = '',
                message = '',
                status = 1.337,
                fields = {
                    'key' : raassdkpyv2.models.field_errors_value.FieldErrors_value(
                        value = null, 
                        message = '', )
                    },
        )
        """

    def testValidateError(self):
        """Test ValidateError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
