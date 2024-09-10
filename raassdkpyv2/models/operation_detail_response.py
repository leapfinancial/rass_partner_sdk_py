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
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from raassdkpyv2.models.ignored_operation_data import IgnoredOperationData
from raassdkpyv2.models.operation_user_detail import OperationUserDetail
from raassdkpyv2.models.payment_method_response import PaymentMethodResponse
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return super().default(o)

class OperationDetailResponse(BaseModel):
    """
    OperationDetailResponse
    """ # noqa: E501
    landing_port_url: Optional[StrictStr] = Field(default=None, alias="landingPortUrl")
    is_landing_port_flow: Optional[StrictBool] = Field(default=None, alias="isLandingPortFlow")
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    tax: Optional[Union[StrictFloat, StrictInt]] = None
    total_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalAmount")
    tenantfee: Optional[Union[StrictFloat, StrictInt]] = None
    ignored_data: Optional[IgnoredOperationData] = Field(default=None, alias="ignoredData")
    is_ignored: Optional[StrictBool] = Field(default=None, alias="isIgnored")
    attribution_link: Optional[StrictStr] = Field(default=None, alias="attributionLink")
    to_user: OperationUserDetail = Field(alias="toUser")
    from_user: OperationUserDetail = Field(alias="fromUser")
    has_reference_code: Optional[StrictBool] = Field(default=None, alias="hasReferenceCode")
    estimated_exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="estimatedExchangeRate")
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="exchangeRate")
    destination_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="destinationFee")
    transaction_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="transactionFee")
    source_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sourceFee")
    destination_payment_method: Optional[PaymentMethodResponse] = Field(default=None, alias="destinationPaymentMethod")
    source_payment_method: Optional[PaymentMethodResponse] = Field(default=None, alias="sourcePaymentMethod")
    recipient_currency: Optional[StrictStr] = Field(default=None, alias="recipientCurrency")
    sender_currency: Optional[StrictStr] = Field(default=None, alias="senderCurrency")
    currency: Optional[StrictStr] = None
    show_warning_screen: StrictBool = Field(alias="showWarningScreen")
    sender_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="senderAmount")
    recipient_amout: Union[StrictFloat, StrictInt] = Field(alias="recipientAmout")
    code: StrictStr
    reason: Optional[StrictStr] = None
    mobile_status: Optional[StrictStr] = Field(default=None, alias="mobileStatus")
    status_details: Optional[StrictStr] = Field(default=None, alias="statusDetails")
    status: StrictStr
    amount: Union[StrictFloat, StrictInt]
    created_at: datetime = Field(alias="createdAt")
    type: StrictStr
    correlation_id: StrictStr = Field(alias="correlationId")
    plat_id: Optional[StrictStr] = Field(default=None, alias="platId")
    id: StrictStr
    __properties: ClassVar[List[str]] = ["landingPortUrl", "isLandingPortFlow", "userId", "tax", "totalAmount", "tenantfee", "ignoredData", "isIgnored", "attributionLink", "toUser", "fromUser", "hasReferenceCode", "estimatedExchangeRate", "exchangeRate", "destinationFee", "transactionFee", "sourceFee", "destinationPaymentMethod", "sourcePaymentMethod", "recipientCurrency", "senderCurrency", "currency", "showWarningScreen", "senderAmount", "recipientAmout", "code", "reason", "mobileStatus", "statusDetails", "status", "amount", "createdAt", "type", "correlationId", "platId", "id"]

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
        return json.dumps(self.to_dict(), cls=DateTimeEncoder)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OperationDetailResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ignored_data
        if self.ignored_data:
            _dict['ignoredData'] = self.ignored_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_user
        if self.to_user:
            _dict['toUser'] = self.to_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of from_user
        if self.from_user:
            _dict['fromUser'] = self.from_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_payment_method
        if self.destination_payment_method:
            _dict['destinationPaymentMethod'] = self.destination_payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_payment_method
        if self.source_payment_method:
            _dict['sourcePaymentMethod'] = self.source_payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OperationDetailResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "landingPortUrl": obj.get("landingPortUrl"),
            "isLandingPortFlow": obj.get("isLandingPortFlow"),
            "userId": obj.get("userId"),
            "tax": obj.get("tax"),
            "totalAmount": obj.get("totalAmount"),
            "tenantfee": obj.get("tenantfee"),
            "ignoredData": IgnoredOperationData.from_dict(obj.get("ignoredData")) if obj.get("ignoredData") is not None else None,
            "isIgnored": obj.get("isIgnored"),
            "attributionLink": obj.get("attributionLink"),
            "toUser": OperationUserDetail.from_dict(obj.get("toUser")) if obj.get("toUser") is not None else None,
            "fromUser": OperationUserDetail.from_dict(obj.get("fromUser")) if obj.get("fromUser") is not None else None,
            "hasReferenceCode": obj.get("hasReferenceCode"),
            "estimatedExchangeRate": obj.get("estimatedExchangeRate"),
            "exchangeRate": obj.get("exchangeRate"),
            "destinationFee": obj.get("destinationFee"),
            "transactionFee": obj.get("transactionFee"),
            "sourceFee": obj.get("sourceFee"),
            "destinationPaymentMethod": PaymentMethodResponse.from_dict(obj.get("destinationPaymentMethod")) if obj.get("destinationPaymentMethod") is not None else None,
            "sourcePaymentMethod": PaymentMethodResponse.from_dict(obj.get("sourcePaymentMethod")) if obj.get("sourcePaymentMethod") is not None else None,
            "recipientCurrency": obj.get("recipientCurrency"),
            "senderCurrency": obj.get("senderCurrency"),
            "currency": obj.get("currency"),
            "showWarningScreen": obj.get("showWarningScreen"),
            "senderAmount": obj.get("senderAmount"),
            "recipientAmout": obj.get("recipientAmout"),
            "code": obj.get("code"),
            "reason": obj.get("reason"),
            "mobileStatus": obj.get("mobileStatus"),
            "statusDetails": obj.get("statusDetails"),
            "status": obj.get("status"),
            "amount": obj.get("amount"),
            "createdAt": obj.get("createdAt"),
            "type": obj.get("type"),
            "correlationId": obj.get("correlationId"),
            "platId": obj.get("platId"),
            "id": obj.get("id")
        })
        return _obj


