
dist_man_MANS = lxde-logout.1 startlxde.1 lxde-settings.1 openbox-lxde.1

EXTRA_DIST = lxde-settings.sgml openbox-lxde.sgml

dist-hook: lxde-settings.1 openbox-lxde.1

lxde-settings.1: lxde-settings.sgml
	docbook-to-man $< > $@

openbox-lxde.1: openbox-lxde.sgml
	docbook-to-man $< > $@

