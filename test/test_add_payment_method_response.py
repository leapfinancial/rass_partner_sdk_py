# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.add_payment_method_response import AddPaymentMethodResponse  # noqa: E501

class TestAddPaymentMethodResponse(unittest.TestCase):
    """AddPaymentMethodResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddPaymentMethodResponse:
        """Test AddPaymentMethodResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddPaymentMethodResponse`
        """
        model = AddPaymentMethodResponse()  # noqa: E501
        if include_optional:
            return AddPaymentMethodResponse(
                id = ''
            )
        else:
            return AddPaymentMethodResponse(
                id = '',
        )
        """

    def testAddPaymentMethodResponse(self):
        """Test AddPaymentMethodResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
