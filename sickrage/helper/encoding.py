# coding=utf-8

# Author: Nic Wolfe <nic@wolfeden.ca>
# URL: https://sickrage.tv
# Git: https://github.com/SiCKRAGETV/SickRage.git
#
# This file is part of SickRage.
#
# SickRage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickRage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickRage.  If not, see <http://www.gnu.org/licenses/>.
import six
import types
import collections

from os import name

def ek(function, *args, **kwargs):
    """
    Encoding Kludge: Call function with arguments and unicode-encode output

    :param function:  Function to call
    :param args:  Arguments for function
    :param kwargs:  Arguments for function
    :return: Unicode-converted function output (string, list or tuple, depends on input)
    """

    if name == 'nt':
        result = function(*args, **kwargs)
    else:
        result = function(*[ss(x) if isinstance(x, (six.text_type, six.binary_type)) and not isinstance(x, types.GeneratorType) else x for x in args], **kwargs)

    try:
        return type(result)(map(uu,result)) if isinstance(result, collections.Iterable) and not isinstance(result, six.string_types) else uu(result)
    except:
        return result

def uu(s):
    """ Convert, at all consts, 'text' to a `unicode` object.
    """

    if isinstance(s, six.text_type):
        return s

    if not isinstance(s, six.string_types):
        if hasattr(s, '__unicode__'):
            s = s.__unicode__()
        else:
            if six.PY3:
                if isinstance(s, six.binary_type):
                    s = six.text_type(s, 'utf-8', 'strict')
                else:
                    s = six.text_type(s)
            else:
                s = six.text_type(six.binary_type(s), 'utf-8', 'strict')
    else:
        s = s.decode('utf-8', 'strict')

    return s

def ss(s):
    """ Convert 'text' to a `str` object.
    """

    if isinstance(s, six.binary_type):
        return s

    if not isinstance(s, six.string_types):
        try:
            if six.PY3:
                return six.text_type(s).encode('utf-8')
            else:
                return six.binary_type(s)
        except UnicodeEncodeError:
            return six.text_type(s).encode('utf-8', 'strict')
    else:
        return s.encode('utf-8', 'strict')