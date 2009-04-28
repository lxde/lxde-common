AC_PREREQ([2.57])
AC_INIT(lxde-common,[0.4], [],lxde-common)
AM_INIT_AUTOMAKE([dist-bzip2 no-dist-gzip])
dnl AC_PROG_INTLTOOL(, [no-xml])
dnl AM_MAINTAINER_MODE

# Checks for programs.
AC_PROG_INSTALL
AC_PROG_LN_S

# xsessions data of path for GDM
AC_ARG_WITH([xsession-path],
    AS_HELP_STRING(
        [--with-xsession-path=PATH],
        [set the install path of xsession data [[DATAROOTDIR/xsessions]]]),
        [test x$withval != x && xsesspath="$withval"],
        [xsesspath="\${datarootdir}/xsessions"])
AC_SUBST(xsesspath)


AC_OUTPUT([
  Makefile
  icon-theme/Makefile
  startlxde
  lxde-logout
  LXDE.desktop
  lxde-logout.desktop
  lxpanel/panel
  openbox/rc.xml
  openbox-lxde
  pcmanfm/main.lxde
  man/Makefile
])

