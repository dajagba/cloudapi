# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class PlateCandidate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PlateCandidate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'plate': 'str',
            'confidence': 'float',
            'matches_template': 'int'
        }

        self.attribute_map = {
            'plate': 'plate',
            'confidence': 'confidence',
            'matches_template': 'matches_template'
        }

        self._plate = None
        self._confidence = None
        self._matches_template = None

    @property
    def plate(self):
        """
        Gets the plate of this PlateCandidate.
        Plate number

        :return: The plate of this PlateCandidate.
        :rtype: str
        """
        return self._plate

    @plate.setter
    def plate(self, plate):
        """
        Sets the plate of this PlateCandidate.
        Plate number

        :param plate: The plate of this PlateCandidate.
        :type: str
        """
        self._plate = plate

    @property
    def confidence(self):
        """
        Gets the confidence of this PlateCandidate.
        Confidence percentage that the plate number is correct

        :return: The confidence of this PlateCandidate.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this PlateCandidate.
        Confidence percentage that the plate number is correct

        :param confidence: The confidence of this PlateCandidate.
        :type: float
        """
        self._confidence = confidence

    @property
    def matches_template(self):
        """
        Gets the matches_template of this PlateCandidate.
        Indicates whether the plate matched a regional text pattern

        :return: The matches_template of this PlateCandidate.
        :rtype: int
        """
        return self._matches_template

    @matches_template.setter
    def matches_template(self, matches_template):
        """
        Sets the matches_template of this PlateCandidate.
        Indicates whether the plate matched a regional text pattern

        :param matches_template: The matches_template of this PlateCandidate.
        :type: int
        """
        self._matches_template = matches_template

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

