Summary: Atomic ELK
Name:    atomic-elk
Version: 0.1
Release: 1
#Source0: LICENSE
Source1: atomic-elk-setup
Source2: logstash-ossec.conf
#Source3: README
License: AGPL
URL: http://www.atomicorp.com
Group: Application/Internet
Vendor: Atomicorp
Packager: Scott R. Shinn <scott@atomicorp.com>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}

Requires: elasticsearch logstash kibana
Requires: java-1.8.0-openjdk
# Planned
Requires: GeoIP
# When we get to json output
#Requires: ossec-hids-server >= 2.9
Requires: ossec-hids-server

 
%description
Atomic ELK is an OSSEC server console based on Elasticsearch,
Logstash, and Kibana


%prep

%build

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/doc/atomic-elk/
mkdir -p %{buildroot}/etc/logstash/conf.d
#install -m0644 %{SOURCE0} %{buildroot}/usr/share/doc/atomic-elk/README
install -m0644 %{SOURCE1} %{buildroot}/etc/logstash/conf.d/ossec.conf
install -m0755 %{SOURCE2} %{buildroot}/usr/bin/atomic-elk-setup





%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#/usr/share/doc/atomic-elk/README
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/logstash/conf.d/ossec.conf
/usr/bin/atomic-elk-setup

%changelog
* Tue May 3 2016 Scott R. Shinn <scott@atomicorp.com> - 0.1-1
- Initialize
