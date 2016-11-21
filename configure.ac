AC_PREREQ([2.57])
AC_INIT(lxde-common,[0.99.2], [http://lxde.org])
AM_INIT_AUTOMAKE([-Wall -Werror foreign no-dist-gzip dist-xz])
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

dnl Fix invalid sysconfdir when --prefix=/usr
if test `eval "echo $sysconfdir"` = /usr/etc
then
    sysconfdir=/etc
fi

GETTEXT_PACKAGE=lxde-common
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [Name of default gettext domain])
AC_SUBST(GETTEXT_PACKAGE)

# Generate po/LINGUAS on the fly rather than relying on translators
# to maintain it manually. This also overcome the problem that Transifex
# cannot add a language to po/LINGUAS if a new po file is submitted.
rm -f $srcdir/po/LINGUAS
for po_file in `ls $srcdir/po/*.po | sort`;
do
    lang=`echo "$po_file" | sed "s|.*/po/\(.*\)\.po|\1|g"`
    echo $lang >> $srcdir/po/LINGUAS
done

AM_GLIB_GNU_GETTEXT

IT_PROG_INTLTOOL([0.40.0])

dnl dirty hack used to prevent the installation of useless mo files.
USE_NLS=no
AC_SUBST(USE_NLS)

AC_OUTPUT([
  Makefile
  startlxde
  lxde-logout
  LXDE.desktop.in
  lxpanel/panel
  openbox/rc.xml
  openbox-lxde
  pcmanfm/pcmanfm.conf
  man/Makefile
  po/Makefile.in
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
