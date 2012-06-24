Summary:	A parallel multiprocess password cracking system
Summary(pl):	R�wnoleg�y wieloprocesorowy system �amania hase�
Summary(es):	Un sistema escalable de obtenci�n de contrase�as en paralelo
Name:		cisilia
Version:	0.7.3
Release:	0.1
License:	GNU GPL version 2
URL:		http://www.cisiar.org
Group:		Applications/System
Source0:	http://www.cisiar.org/proyectos/cisilia/files/versiones/tar/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is a scalable multiprocess password cracking system. The
current version of %{name} (%{version}) recovers Windows NT/2000/XP
and Samba user account passwords computing DES/MD4 password hashes.

Though %{name} includes a dictionary password recovery scheme, the
main goal of this system is to perform "parallel-brute-force" attacks.

This is why it is designed as a multiprocess parallel system with the
ability to run in multiprocessor (SMP) or load-balancing cluster
systems. %{name} divides the password ranges among subprocesses and
then creates the "n" child processes themselves.

If %{name} is executed on a load-balancing cluster, the child
processes are migrated to the other nodes increasing the computational
speed.

Works with Mosix and openMosix.

%description -l pl
%{name} to skalowalny multiprocesorowy system �amania hase�. Bierz�ca
wersja - %{name} (%{version}), odtwarza has�a Windows NT/2000/XP i
Samba user zaszyfrowane algorytmem DES/MD4.

I dlatego jest zaprojektowany jako system r�wnoleglych wielu procesow,
z mozliwoscia pracy wieloprocesorowej (SMP) oraz rozlozeniem
obciazenia w systemach clustrowych. %{name} dzieli zakresy hasla
pomiedzy podprocesy i wtedy tworzy "n" procesow dzieci.

Je�eli %{name} jest wykonywany na load-balancing cluster, procesy
potomne migruj� na inne w�z�y zwi�kszaj� w ten spos�b szybko��
�amania.

Wsp�pracuje z Mosix'em i openMosix'em.

%description -l es
%{name} es un sistema escalable de obtenci�n de contrase�as en
paralelo. La versi�n actual de %{name} (%{version}) obtiene
contrase�as de sistemas Windows NT/2000/XP y de Samba mediante el
c�lculo de hashes DES/MD4.

Si bien %{name} incluye un esquema de obtenci�n de contrase�as
mediante diccionario, la meta principal del sistema es realizar
ataques de fuerza bruta en paralelo.

%{name} puede correr en sistemas multiprocesadores (SMP) o en
"clusters" de balanceo de carga, ya que los rangos de contrase�as se
pueden distribuir y migrar entre "n" subprocesos. De esta manera se
puede incrementar la velocidad total de procesamiento.

%prep
%setup -q

%build
%configure

%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}
%{_includedir}/%{name}/*
%{_mandir}/man1/%{name}.*
%doc %{_prefix}/doc/%{name}/*
