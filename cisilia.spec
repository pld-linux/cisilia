Summary:	A parallel multiprocess password cracking system
Summary(pl):	Równoleg³y wieloprocesowy system ³amania hase³
Summary(es):	Un sistema escalable de obtención de contraseñas en paralelo
Name:		cisilia
Version:	0.7.3
Release:	1
License:	GNU GPL version 2
URL:		http://www.cisiar.org
Group:		Applications/System
Source0:	http://www.cisiar.org/proyectos/cisilia/files/versiones/tar/%{name}-%{version}.tar.gz
# Source0-md5:	c36824988a86da60b01081a8b3082699
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
%{name} to skalowalny wieloprocesowy system ³amania hase³. Bie¿±ca
wersja - %{name} (%{version}), odtwarza has³a kont u¿ytkowników
Windows NT/2000/XP i Samby zaszyfrowane algorytmem DES/MD4.

Pomimo, ¿e %{name} zawiera s³ownikowy schemat odtwarzania hase³,
g³ównym celem tego systemu jest przeprowadzanie ataków
"parallel-brute-force".

W³a¶nie dlatego jest zaprojektowany jako system wielu równoleg³ych
procesów, z mo¿liwo¶ci± pracy wieloprocesorowej (SMP) oraz roz³o¿eniem
obci±¿enia w systemach klastrowych. %{name} dzieli zakresy has³a
pomiêdzy podprocesy i wtedy tworzy "n" procesów potomnych.

Je¿eli %{name} jest wykonywany na klastrze rozk³adaj±cym obci±¿enie,
procesy potomne migruj± na inne wêz³y zwiêkszaj± w ten sposób szybko¶æ
³amania.

Wspó³pracuje z Mosiksem i openMosiksem.

%description -l es
%{name} es un sistema escalable de obtención de contraseñas en
paralelo. La versión actual de %{name} (%{version}) obtiene
contraseñas de sistemas Windows NT/2000/XP y de Samba mediante el
cálculo de hashes DES/MD4.

Si bien %{name} incluye un esquema de obtención de contraseñas
mediante diccionario, la meta principal del sistema es realizar
ataques de fuerza bruta en paralelo.

%{name} puede correr en sistemas multiprocesadores (SMP) o en
"clusters" de balanceo de carga, ya que los rangos de contraseñas se
pueden distribuir y migrar entre "n" subprocesos. De esta manera se
puede incrementar la velocidad total de procesamiento.

%prep
%setup -q

%build
%configure

%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_includedir}/%{name}
%{_mandir}/man1/%{name}.*
%doc %{_prefix}/doc/%{name}
