# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.user_update_params import UserUpdateParams  # noqa: E501

class TestUserUpdateParams(unittest.TestCase):
    """UserUpdateParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserUpdateParams:
        """Test UserUpdateParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserUpdateParams`
        """
        model = UserUpdateParams()  # noqa: E501
        if include_optional:
            return UserUpdateParams(
                email = '',
                first_name = '',
                last_name = '',
                middle_name = '',
                second_last_name = '',
                address1 = '',
                address2 = '',
                place_id = '',
                country = '',
                gender = '',
                dob = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                country_id = '',
                status = 'new',
                first_time = True
            )
        else:
            return UserUpdateParams(
        )
        """

    def testUserUpdateParams(self):
        """Test UserUpdateParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
