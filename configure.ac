AC_PREREQ([2.57])
AC_INIT(lxde-common,[0.2.99], [],lxde-common)
AM_INIT_AUTOMAKE([dist-bzip2 no-dist-gzip])
dnl AC_PROG_INTLTOOL(, [no-xml])
AM_MAINTAINER_MODE

dnl AM_CONFIG_HEADER(config.h)

AC_PROG_INSTALL
AC_PROG_LN_S
dnl AM_PROG_CC_C_O

dnl GETTEXT_PACKAGE=lxde
dnl AM_GNU_GETTEXT([external])
dnl AM_GNU_GETTEXT_VERSION(0.14.1)
dnl AC_SUBST(GETTEXT_PACKAGE)
dnl AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE,"$GETTEXT_PACKAGE", [Gettext package.])

dnl ALL_LINGUAS="zh_TW hu es sk pl"
dnl AM_GLIB_GNU_GETTEXT

# xsessions data of path for GDM
AC_ARG_WITH([xsession-path],
    AS_HELP_STRING(
        [--with-xsession-path=PATH],
        [set the install path of xsession data (default=/usr/share/xsessions)]),
        [test x$withval != x && xsesspath="$withval"],
        [xsesspath=/usr/share/xsessions])
AC_SUBST(xsesspath)

AC_OUTPUT([
  Makefile
  icon-theme/Makefile
  startlxde
  default
  lxde-logout
  LXDE.desktop
  lxpanel/config
  openbox/rc.xml
  pcmanfm/main.lxde
])

