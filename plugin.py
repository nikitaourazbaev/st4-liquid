import sublime
import sublime_plugin

# Uncomment the key bindings in Default.sublime-keymap to enable

class LiquidHandleSpaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not self.view.settings().get("is_widget", False):
            # print("Space was pressed in LiquidHandleSpace")

            view = self.view

            if view.match_selector(0, "text.html.liquid"):
                selectedRegions = view.sel()

                for region in selectedRegions:
                    prevThreeCharacters = view.substr(sublime.Region(region.a - 3, region.a))
                    prevTwoCharacters = view.substr(sublime.Region(region.a - 2, region.a))

                    if prevThreeCharacters == '{%-' or prevThreeCharacters == '{{-' or prevTwoCharacters == '{%' or prevTwoCharacters == '{{':
                        nextThreeCharacters = view.substr(sublime.Region(region.a, region.a + 3))
                        nextTwoCharacters = view.substr(sublime.Region(region.a, region.a + 2))

                        if nextTwoCharacters == '%}' or nextTwoCharacters == '}}' or nextThreeCharacters == '-%}' or nextThreeCharacters == '-}}':
                            view.run_command("insert", {"characters": '  '})
                            for x in range(0, 1):
                                view.run_command("move", {"by": "characters", "forward": False})
                            return

        self.view.run_command("insert", {"characters": " "})

class LiquidHandlePercentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not self.view.settings().get("is_widget", False):
            # print("Percent was pressed in LiquidHandlePercent")

            view = self.view

            if view.match_selector(0, "text.html.liquid"):
                selectedRegions = view.sel()

                for region in selectedRegions:
                    prevCharacter = view.substr(sublime.Region(region.a - 1, region.a))

                    lineContents = view.substr(view.line(view.sel()[0]))

                    if prevCharacter == '{':
                        nextChar = view.substr(sublime.Region(region.a, region.a + 1))
                        if nextChar == '}':
                            view.run_command("insert", {"characters": '%'})
                            for x in range(0, 1):
                                view.run_command("move", {"by": "characters", "forward": False})
                        elif not '%}' in lineContents:
                            view.run_command("insert", {"characters": '%}'})
                            for x in range(0, 2):
                                view.run_command("move", {"by": "characters", "forward": False})

        self.view.run_command("insert", {"characters": "%"})

class LiquidHandleMinusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not self.view.settings().get("is_widget", False):
            # print("Minus was pressed in LiquidHandleMinus")

            view = self.view

            if view.match_selector(0, "text.html.liquid"):
                selectedRegions = view.sel()

                for region in selectedRegions:
                    prevTwoCharacters = view.substr(sublime.Region(region.a - 2, region.a))

                    if prevTwoCharacters == '{%' or prevTwoCharacters == '{{':
                        nextTwoCharacters = view.substr(sublime.Region(region.a, region.a + 2))

                        if nextTwoCharacters == '%}' or nextTwoCharacters == '}}':
                            view.run_command("insert", {"characters": '--'})
                            for x in range(0, 1):
                                view.run_command("move", {"by": "characters", "forward": False})
                            return

        self.view.run_command("insert", {"characters": "-"})

class LiquidHandleBraceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not self.view.settings().get("is_widget", False):
            # print("Brace was pressed in LiquidHandleBrace")

            view = self.view

            if view.match_selector(0, "text.html.liquid"):
                selectedRegions = view.sel()

                for region in selectedRegions:
                    prevCharacter = view.substr(sublime.Region(region.a - 1, region.a))

                    if prevCharacter == '{':
                        nextCharacter = view.substr(sublime.Region(region.a, region.a + 1))

                        if nextCharacter != '}':
                            view.run_command("insert", {"characters": '{}}'})
                            for x in range(0, 2):
                                view.run_command("move", {"by": "characters", "forward": False})
                            return

        self.view.run_command("insert", {"characters": "{"})
