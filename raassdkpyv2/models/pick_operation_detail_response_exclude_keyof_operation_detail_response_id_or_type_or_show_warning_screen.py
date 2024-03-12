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

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from raassdkpyv2.models.ignored_operation_data import IgnoredOperationData
from raassdkpyv2.models.operation_user_detail import OperationUserDetail
from raassdkpyv2.models.payment_method_response import PaymentMethodResponse

class PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K  # noqa: E501
    """
    currency: Optional[StrictStr] = None
    plat_id: Optional[StrictStr] = Field(None, alias="platId")
    correlation_id: StrictStr = Field(..., alias="correlationId")
    created_at: datetime = Field(..., alias="createdAt")
    amount: Union[StrictFloat, StrictInt] = Field(...)
    status: StrictStr = Field(...)
    status_details: Optional[StrictStr] = Field(None, alias="statusDetails")
    mobile_status: Optional[StrictStr] = Field(None, alias="mobileStatus")
    reason: Optional[StrictStr] = None
    code: StrictStr = Field(...)
    recipient_amout: Union[StrictFloat, StrictInt] = Field(..., alias="recipientAmout")
    sender_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="senderAmount")
    sender_currency: Optional[StrictStr] = Field(None, alias="senderCurrency")
    recipient_currency: Optional[StrictStr] = Field(None, alias="recipientCurrency")
    source_payment_method: Optional[PaymentMethodResponse] = Field(None, alias="sourcePaymentMethod")
    destination_payment_method: Optional[PaymentMethodResponse] = Field(None, alias="destinationPaymentMethod")
    source_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="sourceFee")
    transaction_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="transactionFee")
    destination_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="destinationFee")
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="exchangeRate")
    has_reference_code: Optional[StrictBool] = Field(None, alias="hasReferenceCode")
    from_user: OperationUserDetail = Field(..., alias="fromUser")
    to_user: OperationUserDetail = Field(..., alias="toUser")
    attribution_link: Optional[StrictStr] = Field(None, alias="attributionLink")
    is_ignored: Optional[StrictBool] = Field(None, alias="isIgnored")
    ignored_data: Optional[IgnoredOperationData] = Field(None, alias="ignoredData")
    tenantfee: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["currency", "platId", "correlationId", "createdAt", "amount", "status", "statusDetails", "mobileStatus", "reason", "code", "recipientAmout", "senderAmount", "senderCurrency", "recipientCurrency", "sourcePaymentMethod", "destinationPaymentMethod", "sourceFee", "transactionFee", "destinationFee", "exchangeRate", "hasReferenceCode", "fromUser", "toUser", "attributionLink", "isIgnored", "ignoredData", "tenantfee"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen:
        """Create an instance of PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source_payment_method
        if self.source_payment_method:
            _dict['sourcePaymentMethod'] = self.source_payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_payment_method
        if self.destination_payment_method:
            _dict['destinationPaymentMethod'] = self.destination_payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of from_user
        if self.from_user:
            _dict['fromUser'] = self.from_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_user
        if self.to_user:
            _dict['toUser'] = self.to_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ignored_data
        if self.ignored_data:
            _dict['ignoredData'] = self.ignored_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen:
        """Create an instance of PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen.parse_obj(obj)

        _obj = PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen.parse_obj({
            "currency": obj.get("currency"),
            "plat_id": obj.get("platId"),
            "platId": obj.get("platId"),
            "correlation_id": obj.get("correlationId"),
            "correlationId": obj.get("correlationId"),
            "created_at": obj.get("createdAt"),
            "createdAt": obj.get("createdAt"),
            "amount": obj.get("amount"),
            "status": obj.get("status"),
            "status_details": obj.get("statusDetails"),
            "statusDetails": obj.get("statusDetails"),
            "mobile_status": obj.get("mobileStatus"),
            "mobileStatus": obj.get("mobileStatus"),
            "reason": obj.get("reason"),
            "code": obj.get("code"),
            "recipient_amout": obj.get("recipientAmout"),
            "recipientAmout": obj.get("recipientAmout"),
            "sender_amount": obj.get("senderAmount"),
            "senderAmount": obj.get("senderAmount"),
            "sender_currency": obj.get("senderCurrency"),
            "senderCurrency": obj.get("senderCurrency"),
            "recipient_currency": obj.get("recipientCurrency"),
            "recipientCurrency": obj.get("recipientCurrency"),
            "source_payment_method": PaymentMethodResponse.from_dict(obj.get("sourcePaymentMethod")) if obj.get("sourcePaymentMethod") is not None else None,
            "sourcePaymentMethod": PaymentMethodResponse.from_dict(obj.get("sourcePaymentMethod")) if obj.get("sourcePaymentMethod") is not None else None,
            "destination_payment_method": PaymentMethodResponse.from_dict(obj.get("destinationPaymentMethod")) if obj.get("destinationPaymentMethod") is not None else None,
            "destinationPaymentMethod": PaymentMethodResponse.from_dict(obj.get("destinationPaymentMethod")) if obj.get("destinationPaymentMethod") is not None else None,
            "source_fee": obj.get("sourceFee"),
            "sourceFee": obj.get("sourceFee"),
            "transaction_fee": obj.get("transactionFee"),
            "transactionFee": obj.get("transactionFee"),
            "destination_fee": obj.get("destinationFee"),
            "destinationFee": obj.get("destinationFee"),
            "exchange_rate": obj.get("exchangeRate"),
            "exchangeRate": obj.get("exchangeRate"),
            "has_reference_code": obj.get("hasReferenceCode"),
            "hasReferenceCode": obj.get("hasReferenceCode"),
            "from_user": OperationUserDetail.from_dict(obj.get("fromUser")) if obj.get("fromUser") is not None else None,
            "from_user": OperationUserDetail.from_dict(obj.get("fromUser")) if obj.get("fromUser") is not None else None,
            "fromUser": OperationUserDetail.from_dict(obj.get("toUser")) if obj.get("toUser") is not None else None,
            "attribution_link": obj.get("attributionLink"),
            "attributionLink": obj.get("attributionLink"),
            "is_ignored": obj.get("isIgnored"),
            "isIgnored": obj.get("isIgnored"),
            "ignored_data": IgnoredOperationData.from_dict(obj.get("ignoredData")) if obj.get("ignoredData") is not None else None,
            "ignoredData": IgnoredOperationData.from_dict(obj.get("ignoredData")) if obj.get("ignoredData") is not None else None,
            "tenantfee": obj.get("tenantfee")
        })
        return _obj


