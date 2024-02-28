from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

MOD = "mod4"
terminal = "alacritty"

def growUp(layout):
    layout.grow_up()
    layout.grow_main()

def growDown(layout):
    layout.grow_down()
    layout.shrink_main()

keys = [
	# MOVEMENT
    Key([MOD], "h", lazy.layout.left()),
	Key([MOD], "j", lazy.layout.down()),
	Key([MOD], "k", lazy.layout.up()),
	Key([MOD], "l", lazy.layout.right()),
	Key([MOD, "shift"], "h", lazy.layout.grow_left()),
    Key([MOD, "shift"], "j", lazy.layout.function(lambda x : growDown(x))),
    Key([MOD, "shift"], "k", lazy.layout.function(lambda x : growUp(x))),
	Key([MOD, "shift"], "l", lazy.layout.grow_right()),
	Key([MOD, "control"], "h", lazy.layout.shuffle_left()),
	Key([MOD, "control"], "j", lazy.layout.shuffle_down()),
	Key([MOD, "control"], "k", lazy.layout.shuffle_up()),
	Key([MOD, "control"], "l", lazy.layout.shuffle_right()),
    Key([MOD, "control"], "1", lazy.window.toscreen(0)),
    Key([MOD, "control"], "2", lazy.window.toscreen(1)),


	# SPAWN/KILL
    Key([MOD], "return", lazy.spawn(terminal)),
    Key([MOD], "space", lazy.spawn('rofi -modi "drun,window,ssh,run" -show drun -show-icons')),
    Key([MOD], "Escape", lazy.spawn('rofi -modi "power-menu:rofi-power-menu" -show power-menu')),
	Key([MOD], "w", lazy.window.kill()),

	# OTHER
    Key([MOD], "F4", lazy.spawn('alacritty -e nvim ~/.config/qtile/config.py')),
    Key([MOD], "F5", lazy.reload_config()),
    Key([MOD], "Tab", lazy.next_layout()),
    Key([MOD], "m", lazy.group.setlayout("monadthreecol")),

]

layouts = [
    layout.MonadThreeCol(margin=8),
    layout.Columns(),
	layout.Max(),
]

screens = [
	Screen(
		top=bar.Bar(
			[
                widget.TextBox("1"),
				widget.WindowName(),
				widget.Spacer(),
                widget.Clock(format="%h:%m"),
			], 24
		)
	),
    Screen(
        top=bar.Bar(
            [
                widget.WindowName(),
                widget.Spacer(),
                widget.Clock(),
            ], 24
        )
    )
]

groups = [Group("Main")]

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    subprocess.run("/home/reudy/.config/qtile/autostart.sh")
