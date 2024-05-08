# =========================================================================#
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
# =========================================================================#

import re
import statistics
from flet import *


class Dataset:
    def __init__(self):
        pass

    @staticmethod # given a string -> return a list separating each element by commas.
    def get(**vars):
        if len(vars) == 1:
            x = vars["x"]
            return [float(data) for data in x.split(",")]
        else:
            x = vars["x"]
            y = vars["y"]
            return (
                [float(xdata) for xdata in x.split(",")],
                [float(ydata) for ydata in y.split(",")],
            )

    @staticmethod # given a tuple -> split in x and y variables it's two elements to return calculations with two variables | given a list -> return calculations with one variable.
    def calculate(dataset):
        if type(dataset) == tuple:
            x, y = dataset[0], dataset[1]
            return {
                "COVARIANCE": str(statistics.covariance(x, y)),
                "CORRELATION": str(statistics.correlation(x, y)),
            }
        elif type(dataset) == list:
            x = dataset
            return {
                "MEAN": str(statistics.fmean(x)),
                "HARMONIC MEAN": str(statistics.harmonic_mean(x)),
                "GEOMETRIC MEAN": str(statistics.geometric_mean(x)),
                "MODAL": str(statistics.mode(x)),
                "MEDIAN": str(statistics.median(x)),
                "MEDIAN LOW": str(statistics.median_low(x)),
                "MEDIAN HIGH": str(statistics.median_high(x)),
                "MEDIAN GROUPED": str(statistics.median_grouped(x)),
                "SAMPLE VARIANCE": str(statistics.variance(x)),
                "SAMPLE STANDARD DEVIATION": str(statistics.stdev(x)),
                "POPULATION VARIANCE": str(statistics.pvariance(x)),
                "POPULATION STANDARD DEVIATION": str(statistics.pstdev(x)),
            }


class Handler:
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.about = Ref[AlertDialog]()
        self.details = Ref[AlertDialog]()
        self.license = Ref[AlertDialog]()

        self.input = Ref[TextField]()
        self.button = Ref[ElevatedButton]()

        self.output = Ref[Column]()
        self.sheet = Ref[BottomSheet]()

        self.dataset = Dataset()
        self.validator = re.compile(r"^\d+(\.?\d+)?+(,\s?\d+(\.?\d+)?)+$")

    def keyboard_clicked(self, e: ControlEvent): # handles the keyboard using references and data properties of keys (buttons).
        data = e.control.data
        if (data in "Clear") or (self.input.current.value == "Input Error"):
            if data in ("Clear", "Backspace", "Submit", ".", ","):
                self.input.current.value = "0"
            else:
                self.input.current.value = data

        elif data in ("Backspace"):
            if len(self.input.current.value) == 1:
                self.input.current.value = "0"
            else:
                self.input.current.value = self.input.current.value[0:-1]

        elif data in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if self.input.current.value == "0":
                self.input.current.value = data
            else:
                self.input.current.value = self.input.current.value + data

        elif data in (".", ","):
            if self.input.current.value == "0":
                self.input.current.value = "0"
            else:
                self.input.current.value = (
                    self.input.current.value + data
                    if (data in ".")
                    else (self.input.current.value + data + " ")
                )

        self.input.current.focus()
        self.page.update()

    def submit_clicked(self, e: ControlEvent): # validates the calculation input and appends the result and size of the dataset given to input, uses references system too --see <https://flet.dev/blog/control-refs/> for details about references system.
        validator = re.compile(r"^\d+(\.?\d+)?+(,\s?\d+(\.?\d+)?)+$")
        if validator.search(self.input.current.value) == None:
            self.input.current.value = "Input Error"
        else:
            dataset = self.dataset.get(x=self.input.current.value)
            calculation_result = self.dataset.calculate(dataset)

            datasize = len(dataset)
            self.output.current.controls.append(
                Row(
                    controls=[
                        Text(
                            "DATA SIZE:",
                            font_family="M",
                        ),
                        Text(
                            f"{datasize}",
                            font_family="M",
                            selectable=True,
                        ),
                    ],
                    spacing=4,
                )
            )
            for key, value in calculation_result.items():
                self.output.current.controls.append(
                    Column(
                        controls=[
                            Text(f"{key}", font_family="M"),
                            Text(
                                f"{value}",
                                font_family="M",
                                selectable=True,
                            ),
                        ],
                        spacing=0,
                    )
                )
            self.sheet.current.open = True

        self.page.update()

    def clear_output(self, e: ControlEvent): # clear the result (output) when "on_dismiss" event is triggered
        self.output.current.controls.clear()

    def toggle_dialogs(self, e: ControlEvent): # handles the about, details and license dialogs.
        data = e.control.data
        if data in ("Info", "Close", "Back"):
            if self.about.current.open == False:
                self.about.current.open = True
            else:
                self.about.current.open = False

        elif data in "Details":
            details = self.details.current
            if self.details.current.open == False:
                self.details.current.open = True
                self.page.overlay.append(details)
            else:
                self.about.current.open = False

        elif data in "License":
            license = self.license.current
            if self.license.current.open == False:
                self.license.current.open = True
                self.page.overlay.append(license)
            else:
                self.license.current.open = False

        self.page.update()
