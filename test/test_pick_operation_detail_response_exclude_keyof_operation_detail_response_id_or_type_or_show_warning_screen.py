# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen import PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen  # noqa: E501

class TestPickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen(unittest.TestCase):
    """PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen:
        """Test PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen`
        """
        model = PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen()  # noqa: E501
        if include_optional:
            return PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen(
                plat_id = '',
                correlation_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                amount = 1.337,
                status = '',
                status_details = '',
                mobile_status = '',
                reason = '',
                code = '',
                recipient_amout = 1.337,
                sender_amount = 1.337,
                currency = '',
                sender_currency = '',
                recipient_currency = '',
                source_payment_method = raassdkpy.models.payment_method_response.PaymentMethodResponse(
                    name = '', 
                    type = '', 
                    is_primary = True, 
                    account_number = '', 
                    currency = '', 
                    country = '', 
                    number = '', 
                    id = '', ),
                destination_payment_method = raassdkpy.models.payment_method_response.PaymentMethodResponse(
                    name = '', 
                    type = '', 
                    is_primary = True, 
                    account_number = '', 
                    currency = '', 
                    country = '', 
                    number = '', 
                    id = '', ),
                source_fee = 1.337,
                transaction_fee = 1.337,
                destination_fee = 1.337,
                exchange_rate = 1.337,
                has_reference_code = True,
                from_user = raassdkpy.models.operation_user_detail.OperationUserDetail(
                    profile_picture_url = '', 
                    country = '', 
                    image_url = '', 
                    email = '', 
                    phone_number = '', 
                    last_name = '', 
                    first_name = '', ),
                to_user = raassdkpy.models.operation_user_detail.OperationUserDetail(
                    profile_picture_url = '', 
                    country = '', 
                    image_url = '', 
                    email = '', 
                    phone_number = '', 
                    last_name = '', 
                    first_name = '', ),
                attribution_link = '',
                is_ignored = True,
                ignored_data = raassdkpy.models.ignored_operation_data.IgnoredOperationData(
                    description = '', 
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    notify_support = True, 
                    reason = 'I_DONT_RECOGNIZE_CONTACT', 
                    responsible_user_id = '', ),
                tenantfee = 1.337
            )
        else:
            return PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen(
                correlation_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                amount = 1.337,
                status = '',
                code = '',
                recipient_amout = 1.337,
                from_user = raassdkpy.models.operation_user_detail.OperationUserDetail(
                    profile_picture_url = '', 
                    country = '', 
                    image_url = '', 
                    email = '', 
                    phone_number = '', 
                    last_name = '', 
                    first_name = '', ),
                to_user = raassdkpy.models.operation_user_detail.OperationUserDetail(
                    profile_picture_url = '', 
                    country = '', 
                    image_url = '', 
                    email = '', 
                    phone_number = '', 
                    last_name = '', 
                    first_name = '', ),
        )
        """

    def testPickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen(self):
        """Test PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
