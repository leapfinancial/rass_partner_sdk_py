# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpyv2.models.raas_pre_quote_request import RaasPreQuoteRequest  # noqa: E501

class TestRaasPreQuoteRequest(unittest.TestCase):
    """RaasPreQuoteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RaasPreQuoteRequest:
        """Test RaasPreQuoteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RaasPreQuoteRequest`
        """
        model = RaasPreQuoteRequest()  # noqa: E501
        if include_optional:
            return RaasPreQuoteRequest(
                recipient_id = '',
                subscriber_id = '',
                destination_payment_method = None,
                sender_country_code = '',
                is_sender_amount = True,
                amount = 1.337,
                operation_type = 'SendFunds',
                product_type = 'Fund',
                tennant_fee = 1.337
            )
        else:
            return RaasPreQuoteRequest(
                destination_payment_method = None,
                sender_country_code = '',
                is_sender_amount = True,
                amount = 1.337,
                operation_type = 'SendFunds',
                product_type = 'Fund',
        )
        """

    def testRaasPreQuoteRequest(self):
        """Test RaasPreQuoteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
