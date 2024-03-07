# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from raassdkpy.models.quote_transaction_partners_base import QuoteTransactionPartnersBase  # noqa: E501

class TestQuoteTransactionPartnersBase(unittest.TestCase):
    """QuoteTransactionPartnersBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteTransactionPartnersBase:
        """Test QuoteTransactionPartnersBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteTransactionPartnersBase`
        """
        model = QuoteTransactionPartnersBase()  # noqa: E501
        if include_optional:
            return QuoteTransactionPartnersBase(
                recipient_user_id = '',
                currency = '',
                amount = 1.337,
                source_payment_method_id = '',
                destination_payment_method_id = ''
            )
        else:
            return QuoteTransactionPartnersBase(
                recipient_user_id = '',
                currency = '',
                amount = 1.337,
                source_payment_method_id = '',
        )
        """

    def testQuoteTransactionPartnersBase(self):
        """Test QuoteTransactionPartnersBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
