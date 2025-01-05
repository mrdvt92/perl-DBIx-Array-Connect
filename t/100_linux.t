# -*- perl -*-
use strict;
use warnings;
use Test::More tests => 4;

BEGIN { use_ok( 'DBIx::Array::Connect' ); }

my $dac = DBIx::Array::Connect->new;
is($dac->path->[0], ".");
is($dac->path->[2], "/etc");
is($dac->file, "/etc/database-connections-config.ini");
