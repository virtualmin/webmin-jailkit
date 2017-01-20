#!/usr/bin/perl

use warnings;
use strict;

our %text;

require 'jailkit-lib.pl';

my $jk_init_ini = get_jk_init_ini();

ui_print_header(undef, $text{'index_title'}, "", "index", 1, 1, 0,
    undef, undef, undef, undef);

my @table;
foreach my $jail (keys %$jk_init_ini) {
  push(@table, [
    { 'type' => 'checkbox', 'name' => 'd',
      'value' => $jail,
      'comment' => "$jk_init_ini->{$jail}{'comment'}"
    }
  ]);
}

my @buttons;
push(@buttons, [
  [ "delete", $text{'jk_delete'} ]
]);

my @actions;
push(@actions, [
  [ "create", $text{'jk_create'} ]
]);

ui_form_columns_table('delete_jk_init.cgi', @buttons, 1, @actions, \@table);

print ui_form_end([ [ "save", $text{'form_save'} ] ]); # save_config

ui_print_footer("/", $text{'index'});
