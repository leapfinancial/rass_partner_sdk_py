# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpyv2.models.tenant_op_status_hook import TenantOpStatusHook  # noqa: E501

class TestTenantOpStatusHook(unittest.TestCase):
    """TenantOpStatusHook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantOpStatusHook:
        """Test TenantOpStatusHook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantOpStatusHook`
        """
        model = TenantOpStatusHook()  # noqa: E501
        if include_optional:
            return TenantOpStatusHook(
                operation_status_hook = [
                    ''
                    ]
            )
        else:
            return TenantOpStatusHook(
                operation_status_hook = [
                    ''
                    ],
        )
        """

    def testTenantOpStatusHook(self):
        """Test TenantOpStatusHook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
