use Test::More;
eval "use Test::Spelling";
plan skip_all => "Test::Spelling required for testing POD spelling" if $@;
add_stopwords(<DATA>);
all_pod_files_spelling_ok();

__DATA__
10g
11g
24x7
CSV
DBI
INI
SQL
Win32
cfg
filename
ini
ora
tnsnames
