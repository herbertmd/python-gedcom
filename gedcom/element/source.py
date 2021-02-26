# -*- coding: utf-8 -*-

# Python GEDCOM Parser
#
# Copyright (C) 2018 Damon Brodie (damon.brodie at gmail.com)
# Copyright (C) 2018-2019 Nicklas Reincke (contact at reynke.com)
# Copyright (C) 2016 Andreas Oberritter
# Copyright (C) 2012 Madeleine Price Ball
# Copyright (C) 2005 Daniel Zappala (zappala at cs.byu.edu)
# Copyright (C) 2005 Brigham Young University
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Further information about the license: http://www.gnu.org/licenses/gpl-2.0.html

"""GEDCOM element consisting of tag `gedcom.tags.GEDCOM_TAG_SOURCE`"""

from gedcom.element.element import Element
import gedcom.tags


class NotAnActualSourceError(Exception):
    pass


class SourceElement(Element):

    def get_tag(self):
        return gedcom.tags.GEDCOM_TAG_SOURCE

    def get_abbreviation(self):
        """Returns the abbreviated title of a master source in string format.
        :rtype: str
        """
        abbreviation = ""

        for child in self.get_child_elements():
            if child.get_tag() == gedcom.tags.GEDCOM_TAG_ABBREVIATION:
                abbreviation = child.get_multi_line_value()

        return abbreviation

    def get_bibliography(self):
        """Returns the bibliography field of a master source in string format.
        :rtype: str
        """
        bibliography = ""

        for child in self.get_child_elements():
            if child.get_tag() == gedcom.tags.GEDCOM_PROGRAM_DEFINED_TAG_TEMPLATE_BIBLIOGRAPHY:
                bibliography = child.get_multi_line_value()

        return bibliography

    def get_reference(self):
        """Returns the reference of a master source in string format.
        :rtype: str
        """
        reference = ""

        for child in self.get_child_elements():
            if child.get_tag() == gedcom.tags.GEDCOM_TAG_REFERENCE:
                reference = child.get_multi_line_value()

        return reference

    def get_repository_pointer(self):
        """Returns the pointer to the repository of a master source in string format.
        :rtype: str
        """
        repository_pointer = ""

        for child in self.get_child_elements():
            if child.get_tag() == gedcom.tags.GEDCOM_TAG_REPOSITORY:
                reference = child.get_value()

        return repository_pointer

    def get_short_quote(self):
        """Returns the short quote field of a master source in string format.
        :rtype: str
        """
        short_quote = ""

        for child in self.get_child_elements():
            if child.get_tag() == gedcom.tags.GEDCOM_PROGRAM_DEFINED_TAG_TEMPLATE_SHORT_QUOTE:
                short_quote = child.get_multi_line_value()

        return short_quote

    def get_title(self):
        """Returns the full title of a master source in string format.
        :rtype: str
        """
        title = ""

        for child in self.get_child_elements():
            if child.get_tag() == gedcom.tags.GEDCOM_TAG_TITLE:
                title = child.get_multi_line_value()

        return title

    def get_template(self):
        """Returns the template for a master source in string format.
        :rtype: str
        """
        template = {}

        for child in self.get_child_elements():
            if child.get_tag() == gedcom.tags.GEDCOM_PROGRAM_DEFINED_TAG_SOURCE_TEMPLATE:
                for templateElement in child.get_child_elements():
                    if templateElement.get_tag() == gedcom.tags.GEDCOM_TAG_TEMPLATE_ID:
                        template['Id'] = templateElement.get_value()
                    elif templateElement.get_tag() == gedcom.tags.GEDCOM_TAG_FIELD:
                        name, value = "", ""
                        for field_element in templateElement.get_child_elements():
                            if field_element.get_tag() == gedcom.tags.GEDCOM_TAG_FIELD_NAME:
                                name = field_element.get_value()
                            elif field_element.get_tag() == gedcom.tags.GEDCOM_TAG_FIELD_VALUE:
                                value = field_element.get_multi_line_value()
                        if name:
                            template[name] = value

        return template
