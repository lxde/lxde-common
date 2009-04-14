
dist_man_MANS = lxde-logout.1 startlxde.1 lxde-settings.1 openbox-lxde.1

EXTRA_DIST = lxde-settings.sgml openbox-lxde.sgml

dist-hook: lxde-settings.1 openbox-lxde.1

lxde-settings.1: lxde-settings.sgml
	(test -f "`which docbook-to-man`" && docbook-to-man $< > $@) || \
	(test -f "`which db2man`" && db2man $< > $@) || \
	(test -f "`which docbook2man`" && docbook2man $< > $@)

openbox-lxde.1: openbox-lxde.sgml
	(test -f "`which docbook-to-man`" && docbook-to-man $< > $@) || \
	(test -f "`which db2man`" && db2man $< > $@) || \
	(test -f "`which docbook2man`" && docbook2man $< > $@)
