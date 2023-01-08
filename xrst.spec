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
# pyspellchecker is not available on fedora. enchant is but can't seem
# to get it to work in tox.ini and passes test without it. Seems like the
# tox virtual environment has python3-enchant installed.
sed \
   -i tox.ini \
   -e '/^ *pyspellchecker$/d' \
   -e '/^ *enchant$/d'
#
# pytest/test_rst.py
# this is not a git repository, so use different technique to check top
sed \
   -i pytest/test_rst.py \
   -e "s|os.path.exists('.git')|os.path.exists('xrst.toml')|"

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
# build/rst
# remove files that are not *.rst files
rm build/rst/conf.py
rm -r build/rst/_sources
#
# check
# Make sure that build/rst is the same as test_rst
diff build/rst test_rst

%files -n python3-xrst -f %{pyproject_files}
%doc readme.md

# The line below was in the empty spec file, not sure what it is suppsed to do.
# http://ftp.rpm.org/max-rpm/s1-rpm-inside-files-list-directives.html 
# It appears from the page above that is a documentation file and it gets
# stored in /usr/bin (so it is an executable) ?.
%{_bindir}/xrst

%changelog
