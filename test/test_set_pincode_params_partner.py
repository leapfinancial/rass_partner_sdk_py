# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpyv2.models.set_pincode_params_partner import SetPincodeParamsPartner  # noqa: E501

class TestSetPincodeParamsPartner(unittest.TestCase):
    """SetPincodeParamsPartner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetPincodeParamsPartner:
        """Test SetPincodeParamsPartner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetPincodeParamsPartner`
        """
        model = SetPincodeParamsPartner()  # noqa: E501
        if include_optional:
            return SetPincodeParamsPartner(
                pincode = '',
                phone = ''
            )
        else:
            return SetPincodeParamsPartner(
                pincode = '',
                phone = '',
        )
        """

    def testSetPincodeParamsPartner(self):
        """Test SetPincodeParamsPartner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
