AC_PREREQ([2.57])
AC_INIT(lxde-common,[0.3.1], [],lxde-common)
AM_INIT_AUTOMAKE([dist-bzip2 no-dist-gzip])
dnl AC_PROG_INTLTOOL(, [no-xml])
dnl AM_MAINTAINER_MODE

AC_CONFIG_SRCDIR([lxde-settings/lxde-settings.c])
AC_CONFIG_HEADER([config.h])

# Checks for programs.
AC_PROG_INSTALL
AC_PROG_LN_S
AM_PROG_CC_C_O

# Checks for header files.
AC_PATH_X
AC_STDC_HEADERS
AC_CHECK_HEADERS([locale.h stdlib.h string.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_MALLOC
AC_CHECK_FUNCS([setlocale])

PKG_CHECK_MODULES(GLIB, [glib-2.0 >= 2.6.0])
AC_SUBST(GLIB_CFLAGS)
AC_SUBST(GLIB_LIBS)

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
  lxde-settings/Makefile
  icon-theme/Makefile
  startlxde
  default
  lxde-logout
  LXDE.desktop
  lxpanel/config
  openbox/rc.xml
  pcmanfm/main.lxde
  man/Makefile
])

