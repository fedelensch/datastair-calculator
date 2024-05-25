#=========================================================================#
 #               This file is part of Datastair Calculator               #
 #        https://github.com/federicolencina/datastair-calculator        #
 #                                                                       #
 #                      GNU General Public License                       #
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
 #                    Copyright 2024 Federico Lencina                    #
#=========================================================================#


from flet import *
from layout import Layout


class Program(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.page.bgcolor = "#202020"
        self.page.title = "Datastair Calculator"

        self.page.window_width = 340
        self.page.window_height = 546
        self.page.window_resizable = False
        self.page.window_maximizable = False
        self.page.window_always_on_top = True

        self.page.fonts = {
            "L": "/fonts/Light.ttf",
            "R": "/fonts/Regular.ttf",
            "M": "/fonts/Medium.ttf",
        }

    def build(self):
        return Layout(self.page)


def main(page: Page):

    pgrm = Program(page)
    page.add(pgrm)


if __name__ == "__main__":
    app(main, "../assets")
