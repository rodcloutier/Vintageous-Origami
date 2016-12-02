import sublime
import sublime_plugin

from Origami.origami import PaneCommand as OrigamiPaneCommand


def find_duplicate(l):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    return list(x for x in l if x in seen or seen_add(x))


SPLIT_COMMANDS = {
    'clone': 'clone_file_to_pane',
    'carry': 'carry_file_to_pane'
}

def split_command_from_settings():
    prefs = sublime.load_settings('Preferences.sublime-settings')
    command = prefs.get('vintageous_origami_split_command')
    if command not in SPLIT_COMMANDS:
        if command is not None:
            print('"vintageous_origami_split_command" option must be in %s' % SPLIT_COMMANDS.keys())
        command = 'clone'
    return SPLIT_COMMANDS[command]


class _vio_ctrl_w_s(sublime_plugin.WindowCommand):
    """
    Split pane horizontally
    """
    def run(self):
        self.window.run_command("create_pane", {"direction": "down"})
        self.window.run_command(split_command_from_settings(), {"direction": "down"})


class _vio_ctrl_w_v(sublime_plugin.WindowCommand):
    # TODO There is already a command for this in Vintageous, find it...
    """
    Split pane vertically
    """
    def run(self):
        self.window.run_command("create_pane", {"direction": "right"})
        self.window.run_command(split_command_from_settings(), {"direction": "right"})


class _vio_ctrl_w_c(sublime_plugin.WindowCommand):
    """
    Close pane
    """
    def run(self):
        self.window.run_command("close_pane")

        # Now remove the duplicates
        views = self.window.views_in_group(self.window.active_group())
        buffers = [v.buffer_id() for v in views]
        duplicates = find_duplicate(buffers)
        for v in reversed(views):
            buffer_id = v.buffer_id()
            if buffer_id in duplicates:
                duplicates.pop(duplicates.index(buffer_id))
                self.window.focus_view(v)
                # Set scratch?
                self.window.run_command('close')


class _vio_ctrl_w_n(sublime_plugin.WindowCommand):
    """
    Create new file in new horizontal pane
    """
    def run(self):
        self.window.run_command("create_pane", {"direction": "up"})
        self.window.run_command("travel_to_pane", {"direction": "up"})
        self.window.run_command("new_file")


def opposite_direction(direction):
        opposites = {"up": "down", "right": "left", "down": "up", "left": "right"}
        return opposites[direction]


class _vio_exchange_files_with_pane(OrigamiPaneCommand):
    def run(self, direction):
        window = self.window
        window.run_command("carry_file_to_pane", {'direction': direction})
        active_group = window.active_group()
        views = window.views_in_group(active_group)
        active_view = window.active_view()
        if views:
            window.focus_view(views[1])
            window.run_command("carry_file_to_pane", {'direction': opposite_direction(direction)})
            window.focus_view(active_view)


class _vio_ctrl_w_o(sublime_plugin.WindowCommand):
    """
    Set current pane to be the only pane
    """
    def run(self):
        self.window.run_command("set_layout", {"cells": [[0, 0, 1, 1]], "cols": [0.0, 1.0], "rows": [0.0, 1.0]})
        # TODO: Remove duplicate tabs
