#=========================================================================#
 #                                                                       #
 #     Copyright 2024 Federico Lencina - GNU General Public License      #
 #                                                                       #
 #     This program is free software; you can redistribute it and/or     #
 #    modify it under the terms of the GNU General Public License as     #
 #    published by the Free Software Foundation; either version 3 of     #
 #          the License, or at your option any later version.            #
 #                                                                       #
 #  This program is distributed in the hope that it will be useful, but  #
 #       WITHOUT ANY WARRANTY; without even the implied warranty of      #
 #          MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.         #
 #          See the GNU General Public License for more details.         #
 #                                                                       #
 #        You should have received a copy of the GNU General Public      #
 #              License along with this program. If not, see             #
 #                    <https://www.gnu.org/licenses/>.                   #
 #                                                                       #
#=========================================================================#

from flet import *
from views._menu import Menu
from views.calculator import Calculator


class Layout(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.menu = Menu(page)
        self.calculator = Calculator(page)

    def build(self):
        return Column([self.menu, self.calculator])
