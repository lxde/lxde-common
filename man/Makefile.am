dist_man_MANS = lxde-logout.1 startlxde.1 openbox-lxde.1

man_MANS = \
	openbox-lxde.1

man_XMANS = \
	openbox-lxde.xml

EXTRA_DIST = \
	$(man_MANS) \
	$(man_XMANS)


if ENABLE_REGENERATE_MAN

openbox-lxde.1: openbox-lxde.xml
	$(XSLTPROC) -nonet http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl $<        

CLEANFILES = $(man_MANS) 
else

$(man_MANS):
	@echo ""
	@echo "Error: you need to run configure with '--enable-man'"
	@echo "       in order to regenerate man pages."
	@echo ""
	@false
endif
