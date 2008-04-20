bin_PROGRAMS=lxde-settings

lxde_settings_CFLAGS = $(GLIB_CFLAGS) \
                   -DPACKAGE_DATA_DIR=\""$(datadir)/lxde"\" \
                   -DPACKAGE_LOCALE_DIR=\""$(datadir)/locale"\"

lxde_settings_LDADD = $(GLIB_LIBS) -lX11

lxde_settings_SOURCES = \
	lxde-settings.c \
	xsettings-common.h \
	xsettings-common.c \
	xsettings-manager.h \
	xsettings-manager.c \
	xutils.h \
	xutils.c

configdir=$(datadir)/lxde
config_DATA=\
	config

EXTRA_DIST=\
	$(config_DATA)
