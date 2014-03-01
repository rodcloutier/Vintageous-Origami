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

Also adds custom bindings:

* `x`: Close window
* `X`: Close all windows

The following Origami bindings are still available after pressing `ctrl+w`.

* no modifiers: travel to an adjacent pane

Unfortunately, Vintageous does not provide access to the modifiers with directional arrows under `ctrl+w`.
The following Origami bindings will not work.

* `shift`: carry the current file to the destination
* `alt`(`option`):  clone the current file to the destination
* `super`: create an adjacent pane
* `super+shift`: destroy an adjacent pane

(Note: Windows and Linux use `ctrl` instead of `super`.)


Commands
-------
The following basic commands are implemented:
* `:vs[plit]`: Vertical split
* `:sp[lit]`: Horizontal split
* `:new`: Horizontal split with new file
* `:vne[w]`: Vertical split with new file



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
