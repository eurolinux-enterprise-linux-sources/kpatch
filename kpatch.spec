Name:		kpatch
Version:	0.6.1
Release:	1%{?dist}
Summary:	Dynamic kernel patch manager

Group:		System Environment/Kernel
License:	GPLv2
URL:		https://github.com/dynup/kpatch
Source0:	https://github.com/dynup/kpatch/archive/v%{version}.tar.gz
Patch0:		0001-contrib-disable-upstart-kpatch.conf-install.patch

Requires:	bash kmod binutils

BuildArch:	noarch


%description
kpatch is a dynamic kernel patch module manager.  It allows the user to manage
a collection of binary kernel patch modules which can be used to dynamically
patch the kernel without rebooting.


%prep
%setup -q
%patch0 -p1


%build
make -C man


%install
make install PREFIX=/usr DESTDIR=%{buildroot} -C kpatch
make install PREFIX=/usr DESTDIR=%{buildroot} -C man
make install PREFIX=/usr DESTDIR=%{buildroot} -C contrib
rm -f %{buildroot}/usr/share/man/man1/kpatch-build.1.gz


%files
%{_sbindir}/kpatch
%{_usr}/lib/systemd/system/kpatch.service
%doc %{_mandir}/man1/kpatch.1.gz


%changelog
* Thu Jun 21 2018 Joe Lawrence <joe.lawrence@redhat.com> 0.6.1-1
- update to 0.6.1 (rhbz#1562976)

* Thu Nov 16 2017 Joe Lawrence <joe.lawrence@redhat.com> 0.4.0-3
- kpatch: better livepatch module support (rhbz#1504066)

* Wed Oct 18 2017 Josh Poimboeuf <jpoimboe@redhat.com> 0.4.0-2
- fix backwards compatibility with RHEL 7.3 patches (rhbz#1497735)

* Mon Mar 13 2017 Josh Poimboeuf <jpoimboe@redhat.com> 0.4.0-1
- update to 0.4.0 (rhbz#1427642)

* Wed Jun 15 2016 Josh Poimboeuf <jpoimboe@redhat.com> 0.3.2-1
- update to 0.3.2 (rhbz#1282508)

* Wed Nov 18 2015 Josh Poimboeuf <jpoimboe@redhat.com> 0.3.1-1
- update to 0.3.1 (rhbz#1282508)

* Tue Sep 16 2014 Seth Jennings <sjenning@redhat.com> 0.1.10-4
- fix dracut dependencies (rhbz#1170369)

* Tue Sep 16 2014 Seth Jennings <sjenning@redhat.com> 0.1.10-3
- support re-enabling forced modules (rhbz#1140268)

* Thu Sep 11 2014 Seth Jennings <sjenning@redhat.com> 0.1.10-2
- support modprobe format names (rhbz#1133045)

* Thu Jul 31 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.1.10-1
- update to kpatch 0.1.10

* Wed Jul 23 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.1.9-1
- update to kpatch 0.1.9

* Tue Jul 15 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.1.8-1
- update to kpatch 0.1.8

* Wed May 21 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.1.2-1
- update to kpatch 0.1.2

* Mon May 19 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.1.1-2
- fix initramfs core module path

* Mon May 19 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.1.1-1
- rebase to kpatch 0.1.1

* Fri May 9 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.1.0-2
- modprobe core module

* Tue May 6 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.1.0-1
- Initial kpatch release 0.1.0

* Thu Jan 30 2014 Josh Poimboeuf <jpoimboe@redhat.com> 0.0-1
- Initial build
