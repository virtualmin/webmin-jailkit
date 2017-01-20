#!/usr/bin/perl

use warnings;
use strict;

our %text;

require 'jailkit-lib.pl';

my $jk_init_ini = get_jk_init_ini();

ui_print_header(undef, $text{'index_title'}, "", "index", 1, 1, 0,
    undef, undef, undef, undef);

my @table;
foreach my $jail (keys %{$jk_init_ini}) {
  push(@table, [
    { 'type' => 'checkbox', 'name' => 'd',
      'value' => $jail,
      'comment' => "$jk_init_ini->{$jail}{'comment'}"
    }
  ]);
}

my @buttons;
push(@buttons, [
  [ "delete", $text{'index_delete_jail'} ]
]);

my @actions;
push(@actions, [
  [ "create", $text{'index_create_jail'} ]
]);

use Data::Dumper;
print "<!-- " . Dumper($jk_init_ini) . " -->\n";

print "<!-- " . Dumper(get_jk_init_ini()) . " -->\n";

ui_form_columns_table('delete_jk_init.cgi', @buttons, 1, @actions, \@table);

ui_print_footer("/", $text{'index'});
