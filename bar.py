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

class Bar(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.license_link = Text(
            spans=[
                TextSpan(
                    "<https://www.gnu.org/licenses/>",
                    url="https://www.gnu.org/licenses/",
                ),
            ]
        )

        self.details = AlertDialog(
            content=Column(
                controls=[
                    Container(
                        content=ElevatedButton(
                            height=30,
                            width=30,
                            data="ABOUT",
                            style=ButtonStyle(
                                padding={"": 0},
                                elevation={"": 0},
                                color={"": "WHITE", "DISABLED": "GREY"},
                                shape={"": CircleBorder()},
                                bgcolor={
                                    "": "TRANSPARENT",
                                    "DISABLED": "#282828",
                                },
                                overlay_color={
                                    "": "#3A3B3C",
                                    "PRESSED": "#292929",
                                },
                            ),
                            content=Icon("ARROW_BACK_IOS_ROUNDED", size=16),
                            on_click=self.toggle_about,
                        ),
                        alignment=Alignment(x=-1, y=1),
                        padding=10,
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(
                                    spans=[
                                        TextSpan("Datastair Calculator"),
                                    ],
                                    size="18",
                                    font_family="M",
                                    text_align="CENTER",
                                ),
                                Text(
                                    spans=[
                                        TextSpan("A statistical calculator.\n"),
                                        TextSpan("Powerful and simple to use."),
                                    ],
                                    size="16",
                                    font_family="R",
                                    text_align="CENTER",
                                ),
                            ],
                            alignment="CENTER",
                            horizontal_alignment="CENTER",
                        ),
                        padding=16,
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(
                                    spans=[
                                        TextSpan(
                                            "Code and Design by\n",
                                            style=TextStyle(
                                                size=16,
                                                font_family="R",
                                            ),
                                        ),
                                        TextSpan(
                                            "Federico Lencina",
                                            style=TextStyle(
                                                size=16,
                                                font_family="L",
                                            ),
                                        ),
                                    ],
                                    text_align="CENTER",
                                ),
                            ],
                            alignment="CENTER",
                            horizontal_alignment="CENTER",
                        ),
                        padding=16,
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(
                                    spans=[
                                        TextSpan(
                                            "Contact\n",
                                            style=TextStyle(
                                                size=16,
                                                font_family="R",
                                            ),
                                        ),
                                        TextSpan(
                                            "fede.lensch@gmail.com",
                                            style=TextStyle(
                                                size=16,
                                                font_family="L",
                                            ),
                                        ),
                                    ],
                                    selectable=True,
                                    text_align="CENTER",
                                ),
                            ],
                            alignment="CENTER",
                            horizontal_alignment="CENTER",
                        ),
                        padding=16,
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(
                                    spans=[
                                        TextSpan(
                                            "Source Code\n",
                                            style=TextStyle(
                                                size=16,
                                                font_family="R",
                                            ),
                                        ),
                                        TextSpan(
                                            "github.com/datastair-calculator",
                                            style=TextStyle(
                                                size=16,
                                                font_family="L",
                                            ),
                                            url="https://github.com/fedelensch/datastair-calculator",
                                        ),
                                    ],
                                    text_align="CENTER",
                                ),
                            ],
                            alignment="CENTER",
                            horizontal_alignment="CENTER",
                        ),
                        padding=16,
                    ),
                ],
                spacing=2,
                horizontal_alignment="CENTER",
            ),
            inset_padding=20,
            content_padding=1,
            bgcolor="#222222",
            surface_tint_color="#202020",
            shape=RoundedRectangleBorder(radius=10),
        )
        self.about = AlertDialog(
            content=Column(
                controls=[
                    Container(
                        content=ElevatedButton(
                            height=30,
                            width=30,
                            data="ABOUT",
                            style=ButtonStyle(
                                padding={"": 0},
                                elevation={"": 0},
                                color={"": "WHITE", "DISABLED": "GREY"},
                                shape={"": CircleBorder()},
                                bgcolor={
                                    "": "TRANSPARENT",
                                    "DISABLED": "#282828",
                                },
                                overlay_color={
                                    "": "#3A3B3C",
                                    "PRESSED": "#292929",
                                },
                            ),
                            content=Icon("CLOSE_ROUNDED", size=20),
                            on_click=self.toggle_about,
                        ),
                        alignment=Alignment(x=-1, y=1),
                        padding=10,
                    ),
                    Column(
                        controls=[
                            Image("assets/icon.png", height=100, width=100),
                            Text("Datastair Calculator", size=20, font_family="M"),
                            Text("Federico Lencina", size=16, font_family="L"),
                            ElevatedButton(
                                height=35,
                                width=60,
                                style=ButtonStyle(
                                    padding={"": 0},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={"": RoundedRectangleBorder(radius=12)},
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#313233",
                                    },
                                ),
                                content=Text(
                                    "1.0.0",
                                    size=16,
                                    font_family="R",
                                ),
                            ),
                        ],
                        horizontal_alignment="CENTER",
                    ),
                    Container(height=18),
                    Column(
                        controls=[
                            ElevatedButton(
                                height=56,
                                width=250,
                                data="DETAILS",
                                style=ButtonStyle(
                                    padding={"": 10},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={"": RoundedRectangleBorder(radius=10)},
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#313233",
                                    },
                                ),
                                content=Row(
                                    controls=[
                                        Text("Details", size=15.1),
                                        Container(width=147),
                                        Icon("ARROW_FORWARD_IOS_ROUNDED", size=16),
                                    ],
                                    alignment="START",
                                ),
                                on_click=self.toggle_details,
                            ),
                            ElevatedButton(
                                height=56,
                                width=250,
                                data="LICENSE",
                                style=ButtonStyle(
                                    padding={"": 10},
                                    elevation={"": 0},
                                    color={"": "WHITE", "DISABLED": "GREY"},
                                    shape={"": RoundedRectangleBorder(radius=10)},
                                    bgcolor={
                                        "": "#3A3B3C",
                                        "DISABLED": "#282828",
                                    },
                                    overlay_color={
                                        "": "#313233",
                                        "PRESSED": "#313233",
                                    },
                                ),
                                content=Row(
                                    controls=[
                                        Text("License", size=15.1),
                                        Container(width=145),
                                        Icon("ARROW_FORWARD_IOS_ROUNDED", size=16),
                                    ],
                                    alignment="START",
                                ),
                                on_click=self.toggle_license,
                            ),
                        ],
                        spacing=2,
                        horizontal_alignment="CENTER",
                    ),
                ],
                spacing=2,
                horizontal_alignment="CENTER",
            ),
            inset_padding=20,
            content_padding=1,
            bgcolor="#222222",
            surface_tint_color="#202020",
            shape=RoundedRectangleBorder(radius=10),
        )

        self.license = AlertDialog(
            content=Container(
                content=Column(
                    controls=[
                        Text(
                            spans=[
                                TextSpan("GNU General Public License"),
                            ],
                            size="16",
                            font_family="L",
                        ),
                        Text(
                            spans=[
                                TextSpan(
                                    "This program is free software; you can redistribute it and/or "
                                ),
                                TextSpan(
                                    "modify it under the terms of the GNU General Public License as "
                                ),
                                TextSpan(
                                    "published by the Free Software Foundation; either version 3 of "
                                ),
                                TextSpan(
                                    "the License, or at your option any later version."
                                ),
                            ],
                            size="16",
                            font_family="L",
                        ),
                        Text(
                            spans=[
                                TextSpan(
                                    "This program is distributed in the hope that it will be useful, but "
                                ),
                                TextSpan(
                                    "WITHOUT ANY WARRANTY; without even the implied warranty "
                                ),
                                TextSpan(
                                    "of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. "
                                ),
                                TextSpan(
                                    "See the GNU General Public License for more details. "
                                ),
                            ],
                            size="16",
                            font_family="L",
                        ),
                        Text(
                            spans=[
                                TextSpan(
                                    "You should have received a copy of the GNU General Public License "
                                ),
                                TextSpan("along with this program. If not, see\n"),
                                TextSpan(
                                    "<https://www.gnu.org/licenses/>",
                                    url="https://www.gnu.org/licenses/",
                                ),
                            ],
                            size="16",
                            font_family="L",
                        ),
                    ],
                    alignment="CENTER",
                    horizontal_alignment="CENTER",
                ),
                padding=15,
                width=340,
                height=546,
                border_radius=1,
            ),
            actions=[
                ElevatedButton(
                    height=38,
                    width=62,
                    data="OK",
                    style=ButtonStyle(
                        padding={"": 1},
                        elevation={"": 0},
                        color={"": "WHITE", "DISABLED": "GREY"},
                        shape={"": RoundedRectangleBorder(radius=10)},
                        bgcolor={
                            "": "#3A3B3C",
                            "DISABLED": "#282828",
                        },
                        overlay_color={
                            "": "#313233",
                            "PRESSED": "#313233",
                        },
                    ),
                    content=Text("OK"),
                    on_click=self.toggle_license,
                )
            ],
            elevation=0,
            inset_padding=0,
            content_padding=0,
            bgcolor="#202020",
            actions_alignment="CENTER",
            surface_tint_color="#202020",
            shape=RoundedRectangleBorder(radius=1),
        )

        self.page.overlay.append(self.about)

    def build(self):
        return Row(
            controls=[
                ElevatedButton(
                    height=40,
                    width=40,
                    data="TUTORIAL",
                    style=ButtonStyle(
                        padding={"": 0},
                        elevation={"": 0},
                        bgcolor={"": "TRANSPARENT"},
                        color={"": "#EFEFEF", "DISABLED": "GREY"},
                        shape={"": RoundedRectangleBorder(radius=4)},
                        overlay_color={"": "#3A3B3C", "PRESSED": "#292929"},
                    ),
                    url="https://www.youtube.com/shorts/SXHMnicI6Pg",
                    content=Icon("ONDEMAND_VIDEO"),
                ),
                ElevatedButton(
                    height=40,
                    width=40,
                    data="ABOUT",
                    style=ButtonStyle(
                        padding={"": 0},
                        elevation={"": 0},
                        bgcolor={"": "TRANSPARENT"},
                        color={"": "#EFEFEF", "DISABLED": "GREY"},
                        shape={"": RoundedRectangleBorder(radius=4)},
                        overlay_color={"": "#3A3B3C", "PRESSED": "#292929"},
                    ),
                    content=Icon("INFO_OUTLINED"),
                    on_click=self.toggle_about,
                ),
                Container(width=154),
                ElevatedButton(
                    height=40,
                    width=40,
                    data="HISTORY",
                    style=ButtonStyle(
                        padding={"": 0},
                        elevation={"": 0},
                        bgcolor={"": "TRANSPARENT"},
                        color={"": "#EFEFEF", "DISABLED": "GREY"},
                        shape={"": RoundedRectangleBorder(radius=4)},
                        overlay_color={"": "#3A3B3C", "PRESSED": "#292929"},
                    ),
                    content=Icon("HISTORY_OUTLINED"),
                    disabled=True,
                ),
            ]
        )

    def toggle_about(self, e: ControlEvent):
        if self.about.open == False:
            self.about.open = True
        else:
            self.about.open = False

        self.page.update()

    def toggle_license(self, e: ControlEvent):
        if self.license.open == False:
            self.page.overlay.append(self.license)
            self.license.open = True
        else:
            self.about.open = True
            self.license.open = False

        self.page.update()

    def toggle_details(self, e: ControlEvent):
        if self.details.open == False:
            self.page.overlay.append(self.details)
            self.details.open = True
        else:
            self.about.open = True
            self.details.open = False

        self.page.update()
