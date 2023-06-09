# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

powerline_right = {
    "decorations": [
        PowerLineDecoration(path='rounded_left')
    ]
}

powerline_left = {
    "decorations": [
        PowerLineDecoration(path='rounded_right')
    ]
}

theme_colors = ["#0006b1",
				"#ffffff",
				"#272727"]

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": theme_colors[0]
                }


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
	# Custom keybindings
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Spawn rofi launcher"),
    Key([mod, "shift"], "p", lazy.spawn("rofi -show run"), desc="Spawn rofi launcher"),
	Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "f", lazy.spawn("setxkbmap fr"), desc="Change layout to FR"),
	Key([mod], "comma",lazy.spawn(f"{terminal} -e ranger"), desc="Open ranger"),
]

groups = []
group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave"]
group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

layouts = [
    layout.Columns(**layout_theme),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(background=theme_colors[0],
					filename='/home/tim/Pictures/Icons/161-1613315_transparent-hinduism-symbol-png-golden-om-png-png.png',
					mouse_callbacks={
						'Button1': lazy.spawn('rofi -show drun'),
						'Button3': lazy.spawn('systemctl suspend')}),
                widget.GroupBox(highlight_method='block', inactive='#000000', background=theme_colors[0]),
                widget.CurrentLayout(background=theme_colors[0], **powerline_right),
                widget.Prompt(),
                widget.WindowName(background=theme_colors[2], **powerline_left),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.ALSAWidget(),
#				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
                widget.CPU(format="CPU {load_percent}%", background=theme_colors[0]),
                widget.ThermalSensor(format="{temp:.1f}{unit}", background=theme_colors[0]),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
                widget.NvidiaSensors(background=theme_colors[0], format='GPU {temp}°C'),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
                widget.Memory(format='RAM {MemUsed: .1f}{mm}/{MemTotal: .1f}{mm}', background=theme_colors[0], measure_mem="G" ),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
				widget.Backlight(background=theme_colors[0], fmt = 'LT: {}', backlight_name='nvidia_0',
					change_command='brightnessctl set {0}',
					mouse_callbacks={
								'Button1': lazy.spawn('brightnessctl set 100'),
								'Button2': lazy.spawn('brightnessctl set 50'),
								'Button3': lazy.spawn('brightnessctl set 75')}),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
				widget.Volume(background=theme_colors[0], fmt = 'VOL: {}'),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
				widget.KeyboardLayout(background=theme_colors[0], configured_keyboards=['fr', 'us']),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
                widget.BatteryIcon(background=theme_colors[0]),
                widget.Battery(format='{percent:2.0%}', background=theme_colors[0]),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
                widget.Clock(format="%H:%M - %d/%m/%Y", background=theme_colors[0]),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
                widget.Systray(background=theme_colors[0]),
				widget.Sep(background=theme_colors[0], foreground=theme_colors[1]),
            ],
            24,
            border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            border_color=[theme_colors[0], "000000", theme_colors[0], "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
	commands = ["xrandr --dpi '96 x 96'",
				"nitrogen --restore",
				]

	for c in commands:
		os.system(c)

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
