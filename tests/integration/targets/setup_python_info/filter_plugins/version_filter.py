# (c) 2021, Felix Fontein <felix@fontein.de>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


def get_major_minor_version(version):
    parts = version.split('.')[:2]
    return '.'.join(parts)


class FilterModule(object):
    """ IP address and network manipulation filters """

    def filters(self):
        return {
            'internal__get_major_minor_version': get_major_minor_version,
        }
