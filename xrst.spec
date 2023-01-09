# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/

Name:           python-xrst
Version:        2023.1.8
Release:        1%{?dist}
Summary:        Extract Sphinx RST Files

License:        GPL-3.0-or-later
URL:            https://github.com/bradbell/xrst
Source:         %{url}/archive/%{version}/xrst-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-enchant

%global _description %{expand:
This is a sphinx wrapper that extracts RST file from source code
and then runs sphinx to obtain html, tex, or pdf output files.
It includes automatic processing and commands that make sphinx easier to use.}

# First %%description command.
%description %_description

%package -n python3-xrst
Summary:        %{summary}

# Second %%description command.
# What is the difference between the two %description commands ?
%description -n python3-xrst %_description


%prep
%autosetup -p1 -n xrst-%{version}

# tox.ini
# Using rmpbuild -ba SPECS/xrst.spec on 6.0.15-200.fc36.x86_64:
# .1 If we do not remove pyspellchecker from tox.ini we get errror the message
#    python3dist(pyspellchecker) is needed by python-xrst ...
# 2. If we try dnf install 'python3dist(pyspellchecker)' we get the message
#    No match for argument: python3dist(pyspellchecker)
# 3. If we try pip install pyspellchecker we get the message
#    Requirement already satisfied: ...
sed -i tox.ini -e '/^ *pyspellchecker$/d' 

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files xrst


%check
%tox
#

%files -n python3-xrst -f %{pyproject_files}
%doc readme.md

# install the xrst executable
%{_bindir}/xrst

%changelog
