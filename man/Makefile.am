
dist_man_MANS = lxde-logout.1 startlxde.1 lxde-settings-daemon.1 openbox-lxde.1

EXTRA_DIST = lxde-settings-daemon.sgml openbox-lxde.sgml

dist-hook: lxde-settings-daemon.1 openbox-lxde.1

lxde-settings-daemon.1: lxde-settings-daemon.sgml
	docbook-to-man $< > $@

openbox-lxde.1: openbox-lxde.sgml
	docbook-to-man $< > $@

