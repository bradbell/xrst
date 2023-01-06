# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/

Name:           python-xrst
Version:        2023.0.3
Release:        1%{?dist}
Summary:        Extract Sphinx RST Files

License:        GPL-3.0-or-later
URL:            https://github.com/bradbell/xrst
Source:         %{url}/releases/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a sphinx wrapper that extracts RST file from source code
and then runs sphinx to obtain html, tex, or pdf output files.
It includes automatic processing and commands that make sphinx easier to use.}

%description %_description

%package -n python3-xrst
Summary:        %{summary}

%description -n python3-xrst %_description


%prep
%autosetup -p1 -n xrst-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files xrst


%check
python3 -m xrst \
   --local_toc \
   --index_page_name user-guide \
   --config_file xrst.toml \
   --group_list default user dev \
   --html_theme sphinx_rtd_theme


%files -n python3-... -f %{pyproject_files}
%doc README.*
%{_bindir}/...


%changelog
