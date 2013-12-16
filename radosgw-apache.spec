
#################################################################################
# common
#################################################################################
Name:           radosgw-apache
Version:        1.0
Release:        1%{?dist}
Summary:        Configure Apache and radosgw
License:        GPL
Group:          System/Filesystems
URL:            http://ceph.com/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

#
#  Require ceph and any packages needed to
#  bring up radosgw.
Requires:       librbd1 = %{version}-%{release}
Requires:       librados1 = %{version}-%{release}
Requires:	radosgw
Requires:	httpd
Requires:	mod_fastcgi

%description
Meta package for calamari-agent and calamari-restapi packages.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version}

%build
echo "Build"

%install
install -m 0755 -D rgw.conf  $RPM_BUILD_ROOT/%{_sysconfdir}/apache/sites-enabled/rgw.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/apache/sites-enabled/rgw.conf

%post
echo "Post install"
#/sbin/ldconfig
#/sbin/chkconfig --add ceph
#mkdir -p %{_localstatedir}/run/ceph/

%preun
echo "Pre-uninstall"
#%if %{defined suse_version}
#%stop_on_removal ceph
#%endif
#if [ $1 = 0 ] ; then
#    /sbin/service ceph stop >/dev/null 2>&1
#    /sbin/chkconfig --del ceph
#fi

%postun
echo "Post uninstall"
#/sbin/ldconfig
#if [ "$1" -ge "1" ] ; then
#    /sbin/service ceph condrestart >/dev/null 2>&1 || :
#fi
#%if %{defined suse_version}
#%restart_on_update ceph
#%insserv_cleanup
#%endif
# Package removal cleanup
#if [ "$1" -eq "0" ] ; then
#    rm -rf /var/log/ceph
#    rm -rf /etc/ceph
#fi

