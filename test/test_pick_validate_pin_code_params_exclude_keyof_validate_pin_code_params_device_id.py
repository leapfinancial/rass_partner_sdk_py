# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.pick_validate_pin_code_params_exclude_keyof_validate_pin_code_params_device_id import PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId  # noqa: E501

class TestPickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId(unittest.TestCase):
    """PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId:
        """Test PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId`
        """
        model = PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId()  # noqa: E501
        if include_optional:
            return PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId(
                phone = '',
                pincode = ''
            )
        else:
            return PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId(
                phone = '',
                pincode = '',
        )
        """

    def testPickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId(self):
        """Test PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
