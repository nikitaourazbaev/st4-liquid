import sublime
import sublime_plugin

# Enable key bindings to turn on

class LiquidHandleSpaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert", {"characters": " "})

        if not self.view.settings().get("is_widget", False):
            # print("Space was pressed in LiquidHandleSpace")

            view = self.view

            selectedRegions = view.sel()

            for region in selectedRegions:
                prevThreeCharacters = view.substr(sublime.Region(region.a - 4, region.a - 1))
                prevTwoCharacters = view.substr(sublime.Region(region.a - 3, region.a - 1))
                prevCharacter = view.substr(sublime.Region(region.a - 2, region.a - 1))
                nextFourCharacters = view.substr(sublime.Region(region.a, region.a + 4))
                nextThreeCharacters = view.substr(sublime.Region(region.a, region.a + 3))
                nextTwoCharacters = view.substr(sublime.Region(region.a, region.a + 2))

                if prevThreeCharacters == '{%-' or prevThreeCharacters == '{{-' or prevTwoCharacters == '{%' or prevTwoCharacters == '{{':


                    if nextTwoCharacters == '%}' or nextTwoCharacters == '}}' or nextThreeCharacters == '-%}' or nextThreeCharacters == '-}}':
                        view.run_command("insert", {"characters": ' '})
                        for x in range(0, 1):
                            view.run_command("move", {"by": "characters", "forward": False})

                # if prevCharacter == ' ':
                #     if nextFourCharacters == ' -%}' or nextThreeCharacters == ' %}' or nextFourCharacters == ' -}}' or nextThreeCharacters == ' }}':
                #         view.run_command("move", {"by": "characters", "forward": True})
                #         for x in range(0, 2):
                #             view.run_command("left_delete")


class LiquidHandlePercentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert", {"characters": "%"})

        if not self.view.settings().get("is_widget", False):
            # print("Percent was pressed in LiquidHandlePercent")

            view = self.view

            selectedRegions = view.sel()

            for region in selectedRegions:
                prevCharacter = view.substr(sublime.Region(region.a - 2, region.a - 1))
                nextChar = view.substr(sublime.Region(region.a, region.a + 1))
                nextTwoCharacters = view.substr(sublime.Region(region.a, region.a + 2))
                nextThreeCharacters = view.substr(sublime.Region(region.a, region.a + 3))

                lineContents = view.substr(view.line(view.sel()[0]))

                if prevCharacter == '{':
                    if nextChar == '}':
                        view.run_command("insert", {"characters": '%'})
                        for x in range(0, 1):
                            view.run_command("move", {"by": "characters", "forward": False})
                    elif not '%}' in lineContents:
                        view.run_command("insert", {"characters": '%}'})
                        for x in range(0, 2):
                            view.run_command("move", {"by": "characters", "forward": False})
                if nextTwoCharacters == '%}':
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")
                if nextThreeCharacters == ' %}' and prevCharacter == ' ':
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")




class LiquidHandleMinusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert", {"characters": "-"})

        if not self.view.settings().get("is_widget", False):
            # print("Minus was pressed in LiquidHandleMinus")

            view = self.view

            selectedRegions = view.sel()

            for region in selectedRegions:
                prevTwoCharacters = view.substr(sublime.Region(region.a - 3, region.a - 1))
                prevCharacter = view.substr(sublime.Region(region.a - 2, region.a - 1))
                nextFourCharacters = view.substr(sublime.Region(region.a, region.a + 4))
                nextThreeCharacters = view.substr(sublime.Region(region.a, region.a + 3))
                nextTwoCharacters = view.substr(sublime.Region(region.a, region.a + 2))

                if prevTwoCharacters == '{%' or prevTwoCharacters == '{{':
                    if nextTwoCharacters == '%}' or nextTwoCharacters == '}}':
                        view.run_command("insert", {"characters": '-'})
                        for x in range(0, 1):
                            view.run_command("move", {"by": "characters", "forward": False})
                if nextThreeCharacters == '-%}' or nextThreeCharacters == '-}}':
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")

                if (nextFourCharacters == ' -}}' or nextFourCharacters == ' -%}') and prevCharacter == ' ':
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")



class LiquidHandleLeftBraceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert", {"characters": "{"})

        if not self.view.settings().get("is_widget", False):
            # print("LeftBrace was pressed in LiquidHandleLeftBrace")

            view = self.view

            selectedRegions = view.sel()

            for region in selectedRegions:
                prevCharacter = view.substr(sublime.Region(region.a - 2, region.a - 1))

                lineContents = view.substr(view.line(view.sel()[0]))

                if not '}' in lineContents:
                    view.run_command("insert", {"characters": '}'})
                    view.run_command("move", {"by": "characters", "forward": False})
                elif prevCharacter == '{':
                    if not '}}' in lineContents:
                        view.run_command("insert", {"characters": '}'})
                        view.run_command("move", {"by": "characters", "forward": False})


class LiquidHandleRightBraceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert", {"characters": "}"})

        if not self.view.settings().get("is_widget", False):
            # print("RightBrace was pressed in LiquidHandleRightBrace")

            view = self.view

            selectedRegions = view.sel()

            for region in selectedRegions:
                prevCharacter = view.substr(sublime.Region(region.a - 2, region.a - 1))
                nextCharacter = view.substr(sublime.Region(region.a, region.a + 1))
                nextThreeCharacters = view.substr(sublime.Region(region.a, region.a + 3))

                lineContents = view.substr(view.line(view.sel()[0]))

                if nextCharacter == '}':
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")

                if nextThreeCharacters == ' }}' and prevCharacter == ' ':
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")
                    view.run_command("move", {"by": "characters", "forward": True})
                    view.run_command("left_delete")
