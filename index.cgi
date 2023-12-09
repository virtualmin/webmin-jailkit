#!/usr/bin/perl

use warnings;
use strict;

our %text;

require './jailkit-lib.pl';

my $jk_init_ini = get_jk_init_ini();

my @sections = $jk_init_ini->Sections();

ui_print_header(undef, $text{'index_title'}, "", "index", 1, 1, 0, undef,
  undef, undef, undef);

my @table;
foreach my $jail (@sections) {
  push(
    @table,
    [
      {'type' => 'checkbox', 'name' => 'd', 'value' => $jail},
      "<a href=\"edit_jail.cgi?jail=$jail\">" . &html_escape($jail) . "</a>",
      $jk_init_ini->val("$jail", 'comment') || ""
    ]
  );
}

my @buttons;
push(@buttons, [["delete", $text{'index_delete_jail'}]]);

my @actions;
push(@actions, [["edit_jail.cgi?new=1", $text{'index_create_jail'}]]);

#use Data::Dumper;
#print "<!-- " . Dumper(@table) . " -->\n";

print ui_form_columns_table(
  'delete_jail.cgi', @buttons, 1, @actions, undef,
  [$text{'index_delete'}, $text{'index_jail_id'}, $text{'index_comment'}],
  undef, \@table, undef, 1, $text{'index_jail_list'}, $text{'index_no_jails'}
);

ui_print_footer("");
