# Copyright (c) 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.
#

import unittest
import gtk

from subscription_manager.gui.widgets import MachineTypeColumn, MultiEntitlementColumn

class BaseColumnTest(unittest.TestCase):

    def _assert_column_value(self, column_class, model_bool_val, expected_text):
        model = gtk.ListStore(bool)
        model.append([model_bool_val])

        column = column_class(0)
        column._render_cell(None, column.renderer, model, model.get_iter_first())
        self.assertEquals(expected_text, column.renderer.get_property("text"))

class TestMachineTypeColumn(BaseColumnTest):

    def test_render_virtual_when_virt_only(self):
        self._assert_column_value(MachineTypeColumn, True,
                                  MachineTypeColumn.VIRTUAL_MACHINE)

    def test_render_physical_when_not_virt_only(self):
        self._assert_column_value(MachineTypeColumn, False,
                                   MachineTypeColumn.PHYSICAL_MACHINE)


class TestMultiEntitlementColumn(BaseColumnTest):

    def test_render_astrisk_when_multi_entitled(self):
        self._assert_column_value(MultiEntitlementColumn, True,
                                  MultiEntitlementColumn.MULTI_ENTITLEMENT_STRING)

    def test_render_empty_string_when_not_multi_entitled(self):
        self._assert_column_value(MultiEntitlementColumn, False,
                                  MultiEntitlementColumn.NOT_MULTI_ENTITLEMENT_STRING)
