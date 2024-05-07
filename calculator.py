#=======================================================================#
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
#=======================================================================#

from flet import *
from interface import Handler

class Calculator(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.handler = Handler(page)

        self.result = Column(
            controls=[Column(ref=self.handler.output)],
            scroll=ScrollMode.ALWAYS
        )

        self.result_sheet = BottomSheet(
            content=Container(
                content=self.result,
                padding=8,
                width=324,
                height=274,
                border_radius=8,
                bgcolor="#222222"
            ),
            ref=self.handler.sheet,
            on_dismiss=self.handler.clear_output
        )

        self.page.overlay.append(self.result_sheet)

    def build(self):
        return Container(
            content=Column(
                controls=[
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    TextField(
                                        value="",
                                        width=150,
                                        dense=True,
                                        read_only=True,
                                        show_cursor=False,
                                        text_align="RIGHT",
                                        selection_color="#9AC5F8",
                                        border_color="TRANSPARENT",
                                        text_style=TextStyle(
                                            size=20,
                                            color="WHITE",
                                            font_family="R",
                                        ),
                                        ref=self.handler.x_input,
                                    ),
                                    TextField(
                                        value="",
                                        width=150,
                                        dense=True,
                                        read_only=True,
                                        show_cursor=False,
                                        text_align="RIGHT",
                                        selection_color="#9AC5F8",
                                        border_color="TRANSPARENT",
                                        text_style=TextStyle(
                                            size=20,
                                            color="WHITE",
                                            font_family="R",
                                        ),
                                        ref=self.handler.y_input,
                                    ),
                                ],
                                spacing=0,
                                alignment="CENTER",
                            ),
                            Column(
                                controls=[
                                    TextField(
                                        value="0",
                                        width=300,
                                        dense=True,
                                        show_cursor=False,
                                        text_align="RIGHT",
                                        border_color="TRANSPARENT",
                                        text_style=TextStyle(
                                            size=45,
                                            color="WHITE",
                                            font_family="M",
                                        ),
                                        input_filter=InputFilter(
                                            allow=True,
                                            regex_string="[0-9,. ]",
                                            replacement_string=" ",
                                        ),
                                        ref=self.handler.input,
                                    )
                                ]
                            ),
                        ],
                    spacing=0,
                    horizontal_alignment="CENTER",
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                height=32,
                                width=77.2,
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={"": "TRANSPARENT",},
                                    overlay_color={
                                        "": "#333333",
                                        "PRESSED": "#303030",
                                    },
                                ),
                                content=Text(
                                    "X+",
                                    style=TextStyle(
                                        size=14,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                                disabled=True,
                            ),
                            ElevatedButton(
                                height=32,
                                width=77.2,
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={"": "TRANSPARENT",},
                                    overlay_color={
                                        "": "#333333",
                                        "PRESSED": "#303030",
                                    },
                                ),
                                content=Text(
                                    "X-",
                                    style=TextStyle(
                                        size=14,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                                disabled=True,
                            ),
                            ElevatedButton(
                                height=32,
                                width=77.2,
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={"": "TRANSPARENT",},
                                    overlay_color={
                                        "": "#333333",
                                        "PRESSED": "#303030",
                                    },
                                ),
                                content=Text(
                                    "Y+",
                                    style=TextStyle(
                                        size=14,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                                disabled=True,
                            ),
                            ElevatedButton(
                                height=32,
                                width=77.2,
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={"": "TRANSPARENT",},
                                    overlay_color={
                                        "": "#333333",
                                        "PRESSED": "#303030",
                                    },
                                ),
                                content=Text(
                                    "Y-",
                                    style=TextStyle(
                                        size=14,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                                disabled=True,
                            ),
                        ],
                        spacing=2,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("Clear"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#313233",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#3A3B3C",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "C",
                                    style=TextStyle(
                                        size=16,
                                        font_family="M",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("Backspace"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#313233",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#3A3B3C",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Icon(
                                    "BACKSPACE_OUTLINED",
                                    size=14,
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("Submit"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#79B8FF",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#6FA7E6",
                                        "PRESSED": "#79B8FF",
                                    },
                                ),
                                content=Icon(
                                    "CHECK_OUTLINED",
                                    size=16,
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.submit_clicked,
                            ),
                        ],
                        spacing=2,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("7"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "7",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("8"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "8",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("9"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "9",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                        ],
                        spacing=2,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("4"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "4",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("5"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "5",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                width=104,
                                height=52,
                                data=("6"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "6",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                        ],
                        spacing=2,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("1"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "1",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("2"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "2",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("3"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "3",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                        ],
                        spacing=2,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("."),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#313233",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#3A3B3C",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    ".",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=("0"),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                         "": "#313233",
                                        "PRESSED": "#292929",
                                    },
                                ),
                                content=Text(
                                    "0",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                            ElevatedButton(
                                height=52,
                                width=104,
                                data=(","),
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={
                                        "": RoundedRectangleBorder(radius=4)
                                    },
                                    bgcolor={
                                        "": "#313233",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#3A3B3C",
                                        "PRESSED": "#303030",
                                    },
                                ),
                                content=Text(
                                    ",",
                                    style=TextStyle(
                                        size=20,
                                        font_family="L",
                                    ),
                                ),
                                ref=self.handler.button,
                                on_click=self.handler.keyboard_clicked,
                            ),
                        ],
                        spacing=2,
                    ),
                ],
                spacing=2,
            ),
            padding=-6,
        )