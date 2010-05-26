AC_PREREQ([2.57])
AC_INIT(lxde-common,[0.5.5], [],lxde-common)
AM_INIT_AUTOMAKE()
dnl AC_PROG_INTLTOOL(, [no-xml])
dnl AM_MAINTAINER_MODE

# Checks for programs.
AC_PROG_INSTALL
AC_PROG_LN_S

AC_ARG_ENABLE(man,
       [AC_HELP_STRING([--enable-man],
               [regenerate roff man pages from Docbook @<:@default=no@:>@])],
       [enable_man="${enableval}"],
       [enable_man=no]
)
# xsessions data of path for GDM
AC_ARG_WITH([xsession-path],
    AS_HELP_STRING(
        [--with-xsession-path=PATH],
        [set the install path of xsession data [[DATAROOTDIR/xsessions]]]),
        [test x$withval != x && xsesspath="$withval"],
        [xsesspath="\${datarootdir}/xsessions"])
AC_SUBST(xsesspath)


if test x"$enable_man" = x"yes"; then
	AC_PATH_PROG([XSLTPROC], [xsltproc])
	if test -z "$XSLTPROC"; then
		enable_man=no
	fi

	dnl check for DocBook DTD and stylesheets in the local catalog.
	JH_CHECK_XML_CATALOG([-//OASIS//DTD DocBook XML V4.1.2//EN],
		[DocBook XML DTD V4.1.2], [], enable_man=no)
	JH_CHECK_XML_CATALOG([http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl],
		[DocBook XSL Stylesheets >= 1.70.1], [], enable_man=no)
fi

AM_CONDITIONAL(ENABLE_REGENERATE_MAN, test "x$enable_man" != "xno")

AC_OUTPUT([
  Makefile
  startlxde
  lxde-logout
  LXDE.desktop
  lxde-logout.desktop
  lxpanel/panel
  openbox/rc.xml
  openbox-lxde
  pcmanfm/LXDE.conf
  man/Makefile
])

if test x"$sysconfdir" != x'/etc'; then
    echo
    echo
    echo 'Error: sysconfdir is not /etc.'
    echo 'Please consider passing --sysconfdir=/etc to configure.';
    echo 'Otherwise default config files will be installed to wrong place.'
    echo
    echo
fi
