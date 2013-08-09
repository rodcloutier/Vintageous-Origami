Vintageous Origami
===============

Origami is an awesome Sublime Text plugin that lets you conveniently configure your panel layout using shortcut keys.

Vintageous Origami adds pane management shortcut using Origami functionality similar to Vim's window managment. It tries to match as best as possible Vim behaviour. Origami's shortcuts are also available through the familiar Vim `ctrl+w` shortcut.


Notes
-------

* These bindings are only available in command mode (not insert mode).

To use this with Vintageous, first press `ctrl+w`, then press one of following key

* `v` `ctrl_v`: Vertical split
* `s` `S` `ctrl+s`: Horizontal split
* `c`: Close pane
* `n`: New horizontal split with empty file
* `o` `ctrl+o`: Make current pane the only one

The default Origami binding are still available after pressing `ctrl+w`

* no modifiers: travel to an adjacent pane
* `shift`: carry the current file to the destination
* `alt`(`option`):  clone the current file to the destination
* `super`: create an adjacent pane
* `super+shift`: destroy an adjacent pane

(Note: Windows and Linux use `ctrl` instead of `super`.)


Commands
-------
The following basic commands are implemented:
* `:vs(plit)`: Vertical split
* `:s(plit)`: Horizontal split



Install
-------

Make sure you have Origami installed already:

	https://github.com/SublimeText/Origami

Make sure you have Vintageous installed already:

	https://github.com/guillermooo/Vintageous



This plugin will soon be available through [Package Control](http://wbond.net/sublime_packages/package_control).


Manual Install
--------------

First make sure Origami is already installed:

	https://github.com/SublimeText/Origami

Go to your Packages subdirectory under ST2's data directory:

* Windows: %APPDATA%\Sublime Text 3
* OS X: ~/Library/Application Support/Sublime Text 3
* Linux: ~/.config/sublime-text-3
* Portable Installation: Sublime Text 3/Data

Then clone this repository:

    git clone https://github.com/rodcloutier/Vintageous-Origami.git


Inspired by https://github.com/garyc40/Vintage-Origami