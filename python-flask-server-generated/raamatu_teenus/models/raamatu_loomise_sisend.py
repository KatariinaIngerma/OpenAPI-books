from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from raamatu_teenus.models.base_model import Model
from raamatu_teenus import util


class RaamatuLoomiseSisend(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, raamatu_id=None):  # noqa: E501
        """RaamatuLoomiseSisend - a model defined in OpenAPI

        :param raamatu_id: The raamatu_id of this RaamatuLoomiseSisend.  # noqa: E501
        :type raamatu_id: int
        """
        self.openapi_types = {
            'raamatu_id': int
        }

        self.attribute_map = {
            'raamatu_id': 'raamatu_id'
        }

        self._raamatu_id = raamatu_id

    @classmethod
    def from_dict(cls, dikt) -> 'RaamatuLoomiseSisend':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The raamatuLoomiseSisend of this RaamatuLoomiseSisend.  # noqa: E501
        :rtype: RaamatuLoomiseSisend
        """
        return util.deserialize_model(dikt, cls)

    @property
    def raamatu_id(self) -> int:
        """Gets the raamatu_id of this RaamatuLoomiseSisend.


        :return: The raamatu_id of this RaamatuLoomiseSisend.
        :rtype: int
        """
        return self._raamatu_id

    @raamatu_id.setter
    def raamatu_id(self, raamatu_id: int):
        """Sets the raamatu_id of this RaamatuLoomiseSisend.


        :param raamatu_id: The raamatu_id of this RaamatuLoomiseSisend.
        :type raamatu_id: int
        """
        if raamatu_id is None:
            raise ValueError("Invalid value for `raamatu_id`, must not be `None`")  # noqa: E501

        self._raamatu_id = raamatu_id
