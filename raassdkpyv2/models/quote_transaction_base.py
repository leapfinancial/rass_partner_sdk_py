# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QuoteTransactionBase(BaseModel):
    """
    QuoteTransactionBase
    """ # noqa: E501
    sender_user_id: Optional[StrictStr] = Field(default=None, alias="senderUserId")
    sender_country_code: StrictStr = Field(alias="senderCountryCode")
    recipient_user_id: StrictStr = Field(alias="recipientUserId")
    recipient_country_code: StrictStr = Field(alias="recipientCountryCode")
    recipient_currency: StrictStr = Field(alias="recipientCurrency")
    recipient_amount: Union[StrictFloat, StrictInt] = Field(alias="recipientAmount")
    is_sender_amount: StrictBool = Field(alias="isSenderAmount")
    amount_currency: StrictStr = Field(alias="amountCurrency")
    amount: Union[StrictFloat, StrictInt]
    operation_type: Optional[Any] = Field(description="\"SendFunds\"|\"RequestFunds\"|\"WalletLoad\"|\"WalletTransferOut\"|\"TopUp\"|\"RequestTopUp\"|\"SendFundsVirtualAgent\"|\"RequestFundsVirtualAgent\"|\"StorePayment\"", alias="operationType")
    source_payment_method: Optional[Any] = Field(alias="sourcePaymentMethod")
    destination_payment_method: Optional[Any] = Field(default=None, alias="destinationPaymentMethod")
    tennant_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tennantFee")
    tenant_code: Optional[StrictStr] = Field(default=None, alias="tenantCode")
    __properties: ClassVar[List[str]] = ["senderUserId", "senderCountryCode", "recipientUserId", "recipientCountryCode", "recipientCurrency", "recipientAmount", "isSenderAmount", "amountCurrency", "amount", "operationType", "sourcePaymentMethod", "destinationPaymentMethod", "tennantFee", "tenantCode"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QuoteTransactionBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if operation_type (nullable) is None
        # and model_fields_set contains the field
        if self.operation_type is None and "operation_type" in self.model_fields_set:
            _dict['operationType'] = None

        # set to None if source_payment_method (nullable) is None
        # and model_fields_set contains the field
        if self.source_payment_method is None and "source_payment_method" in self.model_fields_set:
            _dict['sourcePaymentMethod'] = None

        # set to None if destination_payment_method (nullable) is None
        # and model_fields_set contains the field
        if self.destination_payment_method is None and "destination_payment_method" in self.model_fields_set:
            _dict['destinationPaymentMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of QuoteTransactionBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "senderUserId": obj.get("senderUserId"),
            "senderCountryCode": obj.get("senderCountryCode"),
            "recipientUserId": obj.get("recipientUserId"),
            "recipientCountryCode": obj.get("recipientCountryCode"),
            "recipientCurrency": obj.get("recipientCurrency"),
            "recipientAmount": obj.get("recipientAmount"),
            "isSenderAmount": obj.get("isSenderAmount"),
            "amountCurrency": obj.get("amountCurrency"),
            "amount": obj.get("amount"),
            "operationType": obj.get("operationType"),
            "sourcePaymentMethod": obj.get("sourcePaymentMethod"),
            "destinationPaymentMethod": obj.get("destinationPaymentMethod"),
            "tennantFee": obj.get("tennantFee"),
            "tenantCode": obj.get("tenantCode")
        })
        return _obj


