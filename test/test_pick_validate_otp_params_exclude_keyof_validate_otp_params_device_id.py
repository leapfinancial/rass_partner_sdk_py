# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.pick_validate_otp_params_exclude_keyof_validate_otp_params_device_id import PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId  # noqa: E501

class TestPickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId(unittest.TestCase):
    """PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId:
        """Test PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId`
        """
        model = PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId()  # noqa: E501
        if include_optional:
            return PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId(
                phone = '',
                otp_code = ''
            )
        else:
            return PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId(
                phone = '',
                otp_code = '',
        )
        """

    def testPickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId(self):
        """Test PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
