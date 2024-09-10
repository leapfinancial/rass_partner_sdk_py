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

class RaasQuoteTransactionResponse(BaseModel):
    """
    RaasQuoteTransactionResponse
    """ # noqa: E501
    id: Optional[StrictStr] = None
    source_currency: StrictStr = Field(alias="sourceCurrency")
    destination_currency: StrictStr = Field(alias="destinationCurrency")
    reason: StrictStr = Field(...)
    reason_detail: Optional[StrictStr] = Field(..., alias="reasonDetail")
    source_amount: Union[StrictFloat, StrictInt] = Field(alias="sourceAmount")
    amount: Union[StrictFloat, StrictInt]
    destination_amount: Union[StrictFloat, StrictInt] = Field(alias="destinationAmount")
    exchange_rate: Union[StrictFloat, StrictInt] = Field(alias="exchangeRate")
    tax: Union[StrictFloat, StrictInt]
    source_fee: Union[StrictFloat, StrictInt] = Field(alias="sourceFee")
    destination_fee: Union[StrictFloat, StrictInt] = Field(alias="destinationFee")
    transaction_fee: Union[StrictFloat, StrictInt] = Field(alias="transactionFee")
    partner_fee: Union[StrictFloat, StrictInt] = Field(alias="partnerFee")
    sender_charge_back: Union[StrictFloat, StrictInt] = Field(alias="senderChargeBack")
    recipient_charge_back: Union[StrictFloat, StrictInt] = Field(alias="recipientChargeBack")
    is_executable: StrictBool = Field(alias="isExecutable")
    valid_time_in_minutes: Union[StrictFloat, StrictInt] = Field(alias="validTimeInMinutes")
    operation_type: Optional[StrictStr] = Field(alias="operationType")
    tenant_fee: Union[StrictFloat, StrictInt] = Field(alias="tenantFee")
    sender_user_id: Optional[StrictStr] = Field(default=None, alias="senderUserId")
    total_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalAmount")
    __properties: ClassVar[List[str]] = ["id", "sourceCurrency", "destinationCurrency", "reason", "reasonDetail", "sourceAmount", "amount", "destinationAmount", "exchangeRate", "tax", "sourceFee", "destinationFee", "transactionFee", "partnerFee", "senderChargeBack", "recipientChargeBack", "isExecutable", "validTimeInMinutes", "operationType", "tenantFee", "senderUserId", "totalAmount"]

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
        """Create an instance of RaasQuoteTransactionResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RaasQuoteTransactionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "sourceCurrency": obj.get("sourceCurrency"),
            "destinationCurrency": obj.get("destinationCurrency"),
            "reason": obj.get("reason"),
            "reasonDetail": obj.get("reasonDetail"),
            "sourceAmount": obj.get("sourceAmount"),
            "amount": obj.get("amount"),
            "destinationAmount": obj.get("destinationAmount"),
            "exchangeRate": obj.get("exchangeRate"),
            "tax": obj.get("tax"),
            "sourceFee": obj.get("sourceFee"),
            "destinationFee": obj.get("destinationFee"),
            "transactionFee": obj.get("transactionFee"),
            "partnerFee": obj.get("partnerFee"),
            "senderChargeBack": obj.get("senderChargeBack"),
            "recipientChargeBack": obj.get("recipientChargeBack"),
            "isExecutable": obj.get("isExecutable"),
            "validTimeInMinutes": obj.get("validTimeInMinutes"),
            "operationType": obj.get("operationType"),
            "tenantFee": obj.get("tenantFee"),
            "senderUserId": obj.get("senderUserId"),
            "totalAmount": obj.get("totalAmount")
        })
        return _obj


