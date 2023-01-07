# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/

Name:           python-xrst
Version:        2023.0.3
Release:        1%{?dist}
Summary:        Extract Sphinx RST Files

License:        GPL-3.0-or-later
URL:            https://github.com/bradbell/xrst
Source:         %{url}/releases/refs/tags/%{version}.tar.gz
# The tarball for this github project is in the location above.
# Even thought this tarball is named %{version}.tar.gz, it will create
# the xrst-%{version} directory with a copy of the source.
#
# The example spec file suggests the location
# %{url}/archive/v%{version}/xrst-%{version}.tar.gz
# but that does not seem to work.

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a sphinx wrapper that extracts RST file from source code
and then runs sphinx to obtain html, tex, or pdf output files.
It includes automatic processing and commands that make sphinx easier to use.}

%description %_description
# First %description command.

%package -n python3-xrst
Summary:        %{summary}

%description -n python3-xrst %_description
# Second %description command.
# What is the difference between the two %description commands ?


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
#
# build/rst
# Use xrst source code to create build/rst. We could change this locaion
# by changing htm_directory in xrst.toml.
if [ -e build/rst ]
then
   rm -r build/rst
fi
%{python3} -m xrst \
   --local_toc \
   --index_page_name user-guide \
   --config_file xrst.toml \
   --group_list default user dev \
   --html_theme sphinx_rtd_theme \
   --rst_only
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
# %{_bindir}/...
# The line below was in the empty spec file, not sure what it is suppsed to do.
# http://ftp.rpm.org/max-rpm/s1-rpm-inside-files-list-directives.html 
# It appears from the page above that is a documentation file and it gets
# stored in /usr/bin (so it is an executable) ?.

%changelog
