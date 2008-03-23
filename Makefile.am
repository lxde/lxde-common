SUBDIRS = icon-theme

bin_SCRIPTS = startlxde lxde-logout

# Currently these paths are hardcoded.
xsessiondir=$(xsesspath)
xsession_DATA = LXDE.desktop

defaultsdir=/etc/xdg/lxsession/LXDE
defaults_DATA = default

wallpapersdir=$(datadir)/lxde/wallpapers
wallpapers_DATA=wallpapers/lxde_blue.jpg

imagesdir=$(datadir)/lxde/images
images_DATA= \
	images/logout-banner.png \
	images/lxde-icon.png

lxpaneldir=$(datadir)/lxpanel/profile/LXDE
lxpanel_DATA=lxpanel/config

openboxdir=$(datadir)/lxde/openbox
openbox_DATA= \
	openbox/rc.xml \
	openbox/menu.xml

gtkrcdir=$(datadir)/lxde
gtkrc_DATA = gtkrc-2.0

pcmanfmdir=$(datadir)/lxde/pcmanfm
pcmanfm_DATA= \
	pcmanfm/main.lxde

EXTRA_DIST = \
	LXDE.desktop.in \
	startlxde.in \
	$(wallpapers_DATA) \
	$(images_DATA) \
	icon-theme/COPYING \
	icon-theme/AUTHORS \
	openbox/rc.xml.in \
	openbox/menu.xml \
	pcmanfm/main.lxde.in \
	gtkrc-2.0

CLEANFILES = $(bin_SCRIPTS)

