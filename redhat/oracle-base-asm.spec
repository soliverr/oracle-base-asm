
Summary   :  Directory layout for Oracle ASM.
Summary(ru_RU.UTF-8)   : Иерархия каталогов для ASM Oracle.
Name      : oracle-base-asm
Version   : 1.0
Release   : 5
Group     : Database

Packager  : Kryazhevskikh Sergey, <soliverr@gmail.com>
License   : GPLv2

BuildArch : noarch
Requires  : oracle-base

Source: %name-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}

%define pkg_build_dir   %_builddir/%name-%version
%define pkg_functions   %pkg_build_dir/_pkg-functions

%description
Directory layout and system groups for Oracle ASM.

%description -l ru_RU.UTF-8
Иерархия каталогов и системные группы для ASM Oracle.

%prep

%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{__install} -d %{buildroot}/var/log/oracle/
%{__install} -D oracle-base-asm-log-dirs %{buildroot}/usr/bin/oracle-base-asm-log-dirs
ORACLE_ASM_LOG_BASE_BUILD_DST=%{buildroot} %{buildroot}/usr/bin/oracle-base-asm-log-dirs -d

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%pre
%include %{pkg_functions}

if [ $1 -eq 1 ] ; then
  action=install
else
  action=upgrade
fi

preinst "redhat" "$action"


%preun
%include %pkg_functions

if [ $1 -eq 0 ] ; then
  action=remove
else
  action=upgrade
fi

prerm "redhat" "$action"

%post
%include %pkg_functions

if [ $1 -eq 1 ] ; then
  action=configure
else
  action=upgrade
fi

postinst "redhat" "$action"

%postun
%include %pkg_functions

if [ $1 -eq 0 ] ; then
  action=purge
  #chmod -R 2755 /etc/oracle
  #chown -R oracle:oracle /etc/oracle
else
  action=upgrade
fi

postrm "redhat" "$action"


%files
%defattr(-,root,root)
%doc README
%dir %attr(2770,oracle,asmdba) /var/log/oracle/asm
%attr(2770,oracle,asmdba) /var/log/oracle/asm/*
%attr(750,oracle,asmdba) /usr/bin/*

%changelog
* Wed Apr 18 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-5  11:18:09 +0600
- Added `diag', `rdbms/audit' directories

* Tue Apr 10 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-4  11:32:52 +0600
- Added new directories

* Wed Apr 04 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-3  12:15:18 +0600
- Added `ORACLE_HOME/install/checkpoints' symlink

* Tue Apr 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-2  16:48:48 +0600
- Changed files and directories permissions

* Mon Apr 02 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-1  11:29:02 +0600
- Initial version of package

