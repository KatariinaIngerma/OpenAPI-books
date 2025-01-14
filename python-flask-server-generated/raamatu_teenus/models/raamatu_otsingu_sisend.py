from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from raamatu_teenus.models.base_model import Model
from raamatu_teenus import util


class RaamatuOtsinguSisend(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sone=None, raamatu_id=None):  # noqa: E501
        """RaamatuOtsinguSisend - a model defined in OpenAPI

        :param sone: The sone of this RaamatuOtsinguSisend.  # noqa: E501
        :type sone: str
        :param raamatu_id: The raamatu_id of this RaamatuOtsinguSisend.  # noqa: E501
        :type raamatu_id: int
        """
        self.openapi_types = {
            'sone': str,
            'raamatu_id': int
        }

        self.attribute_map = {
            'sone': 'sone',
            'raamatu_id': 'raamatu_id'
        }

        self._sone = sone
        self._raamatu_id = raamatu_id

    @classmethod
    def from_dict(cls, dikt) -> 'RaamatuOtsinguSisend':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The raamatuOtsinguSisend of this RaamatuOtsinguSisend.  # noqa: E501
        :rtype: RaamatuOtsinguSisend
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sone(self) -> str:
        """Gets the sone of this RaamatuOtsinguSisend.


        :return: The sone of this RaamatuOtsinguSisend.
        :rtype: str
        """
        return self._sone

    @sone.setter
    def sone(self, sone: str):
        """Sets the sone of this RaamatuOtsinguSisend.


        :param sone: The sone of this RaamatuOtsinguSisend.
        :type sone: str
        """
        if sone is None:
            raise ValueError("Invalid value for `sone`, must not be `None`")  # noqa: E501

        self._sone = sone

    @property
    def raamatu_id(self) -> int:
        """Gets the raamatu_id of this RaamatuOtsinguSisend.


        :return: The raamatu_id of this RaamatuOtsinguSisend.
        :rtype: int
        """
        return self._raamatu_id

    @raamatu_id.setter
    def raamatu_id(self, raamatu_id: int):
        """Sets the raamatu_id of this RaamatuOtsinguSisend.


        :param raamatu_id: The raamatu_id of this RaamatuOtsinguSisend.
        :type raamatu_id: int
        """
        if raamatu_id is None:
            raise ValueError("Invalid value for `raamatu_id`, must not be `None`")  # noqa: E501

        self._raamatu_id = raamatu_id
