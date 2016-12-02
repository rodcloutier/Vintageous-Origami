Vintageous Origami
===============

Origami is an awesome Sublime Text plugin that lets you conveniently configure your panel layout using shortcut keys.

Vintageous Origami adds pane management shortcut using Origami functionality similar to Vim's window managment. It tries to match as best as possible Vim behaviour. Origami's shortcuts are also available through the familiar Vim `ctrl+w` shortcut.


Notes
-------

* These bindings are only available in command mode (not insert mode).

To use this with Vintageous, first press `ctrl+w`, then press one of following key

* `v` `ctrl+v`: Vertical split
* `s` `S` `ctrl+s`: Horizontal split
* `c`: Close pane
* `n` `ctrl+n`: New horizontal split with empty file
* `o` `ctrl+o`: Make current pane the only one
* `l`, `<right>`: Move to right pane
* `h`, `<left>`: Move to left pane
* `k`, `<up>`: Move to up pane
* `j`, `<down>`: Move to down pane
* `L`: Exchange with right pane
* `H`: Exchange with left pane
* `K`: Exchange with up pane
* `J`: Exchange with down pane

Also adds custom bindings:

* `x`: Close window
* `X`: Close all windows


The following Origami bindings are still available after pressing `ctrl+w`.

* no modifiers: travel to an adjacent pane

The following Origami bindings will not work.

* `shift`: carry the current file to the destination
* `alt`(`option`):  clone the current file to the destination
* `super`: create an adjacent pane
* `super+shift`: destroy an adjacent pane

(Note: Windows and Linux use `ctrl` instead of `super`.)


Commands
-------
The following basic commands are implemented:
* `:sp[lit]`: Horizontal split
* `:vne[w]`: Vertical split with new file

By default, the plugin overrides the following command provided by Vintageous
to provide a behaviour that is more consistent with Vim's

* `:vs[plit]`: Vertical split
* `:new`: Horizontal split with new file
* `:on[ly]`: Make current pane the only one

Each of the override can be toggle with the appropriate settingfollowing preferences
vintageous_origami_override_command_vsplit


Settings
-------
See [Vintageous-origami/Preferences.sublime-settings](https://github.com/rodcloutier/Vintageous-Origami/blob/master/Preferences.sublime-settings) for a comprehensive list of settings.


Install
-------

Make sure you have Origami installed already:

	https://github.com/SublimeText/Origami

Make sure you have Vintageous installed already:

	https://github.com/guillermooo/Vintageous


Enable Vintageous to use ctrl keys in your preferences

	`"vintageous_use_ctrl_keys": true`



This plugin is available through [Package Control](http://wbond.net/sublime_packages/package_control).


Manual Install
--------------

First make sure Origami is already installed:

	https://github.com/SublimeText/Origami

Go to your Packages subdirectory under ST3's data directory:

* Windows: %APPDATA%\Sublime Text 3
* OS X: ~/Library/Application Support/Sublime Text 3
* Linux: ~/.config/sublime-text-3
* Portable Installation: Sublime Text 3/Data

Then clone this repository:

    git clone https://github.com/rodcloutier/Vintageous-Origami.git


Todo
--------------
* Add support for arguments to :sp :vs :new :vnew


Inspired by https://github.com/garyc40/Vintage-Origami
