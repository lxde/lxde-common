
dist_man_MANS = lxde-logout.1 startlxde.1 openbox-lxde.1

EXTRA_DIST = openbox-lxde.sgml

dist-hook: openbox-lxde.1

openbox-lxde.1: openbox-lxde.sgml
	(test -f "`which docbook-to-man`" && docbook-to-man $< > $@) || \
	(test -f "`which db2man`" && db2man $< > $@) || \
	(test -f "`which docbook2man`" && docbook2man $< > $@)
