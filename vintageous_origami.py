import sublime_plugin

from Origami.origami import PaneCommand as OrigamiPaneCommand

from .vi import cmd_defs
from .vi import actions
from .vi import keys

cmd_defs.patch()
actions.patch()
keys.patch()










# from Vintageous.ex.ex_command_parser import ex_cmd_data, EX_COMMANDS


# #TODO: Add support for filename, args, etc.

# EX_COMMANDS[('split', 'sp')] = ex_cmd_data(command="vio_ex_split",
#                                            invocations=(),
#                                            error_on=())
# EX_COMMANDS[('vsplit', 'vs')] = ex_cmd_data(command="vio_ex_vsplit",
#                                             invocations=(),
#                                             error_on=())


# class VioExVsplitCommand(sublime_plugin.WindowCommand):
#     def run(self, line_range=None):
#         VioVsplitCommand.run(self)


# class VioExSplitCommand(sublime_plugin.WindowCommand):
#     def run(self, line_range=None):
#         VioSplitCommand.run(self)


# class VioVsplitCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         self.window.run_command("create_pane", {"direction": "right"})
#         self.window.run_command("clone_file_to_pane", {"direction": "right"})


# class VioSplitCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         self.window.run_command("create_pane", {"direction": "down"}_)
#         self.window.run_command("clone_file_to_pane", {"direction": "down"})


# class VioExchangeCarryAndExchangeFiletoPane(sublime_plugin.WindowCommand):
#     def run(self):
#         #
#         self.window.run_command("carry_file_to_pane", {"direction": "right"})


# def find_duplicate(l):
#     seen = set()
#     seen_add = seen.add
#     # adds all elements it doesn't know yet to seen and all other to seen_twice
#     return list(x for x in l if x in seen or seen_add(x))


# class VioCloseCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         self.window.run_command("close_pane")

#         # Now remove the duplicates
#         views = self.window.views_in_group(self.window.active_group())
#         buffers = [v.buffer_id() for v in views]
#         duplicates = find_duplicate(buffers)
#         for v in reversed(views):
#             buffer_id = v.buffer_id()
#             if buffer_id in duplicates:
#                 duplicates.pop(duplicates.index(buffer_id))
#                 self.window.focus_view(v)
#                 # Set scratch?
#                 self.window.run_command('close')


# class VioNewCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         self.window.run_command("create_pane", {"direction": "up"})
#         self.window.run_command("travel_to_pane", {"direction": "up"})
#         self.window.run_command("new_file")


# class VioOnlyCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         self.window.run_command("set_layout", {"cells": [[0, 0, 1, 1]], "cols": [0.0, 1.0], "rows": [0.0, 1.0]})


# def opposite_direction(direction):
#         opposites = {"up":"down", "right":"left", "down":"up", "left":"right"}
#         return opposites[direction]


# class VioExchangeFilesWithPane(OrigamiPaneCommand):
#     def run(self, direction):
#         window = self.window
#         window.run_command("carry_file_to_pane", {'direction': direction})
#         active_group = window.active_group()
#         views = window.views_in_group(active_group)
#         active_view = window.active_view()
#         if views:
#             window.focus_view(views[1])
#             window.run_command("carry_file_to_pane", {'direction': opposite_direction(direction)})
#             window.focus_view(active_view)

