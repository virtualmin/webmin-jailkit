#!/usr/bin/perl
use strict;
use warnings;

our (%text, %in);
require './jailkit-lib.pl';
ReadParse();

my $jk_init_ini = get_jk_init_ini();
my @sections = $jk_init_ini->Sections();
my %jail_params;

my @d = split(/\0/, $in{'d'});

# If we've already confirmed go ahead an delete it
if (defined $in{'confirmed'}) {
  foreach my $jail (@d) {
    if ($jk_init_ini->SectionExists($jail)) {
      $jk_init_ini->DeleteSection($jail);
    }
    else {
      # Does this jail exist?
      error( text('error_jail_not_found', "$jail", "<br>\n"));
    }
  }
  write_jk_init_ini($jk_init_ini);
  redirect('');
}
else {
  ui_print_header(undef, $text{'index_delete_jail'}, "");
  print "<center>\n";

  # Check to be sure we really want these jails gone
  print ui_form_start("delete_jail.cgi", "post");
  foreach my $jail (@d) {
    # Re-send all of the d_* items with a confirmed field
    print ui_hidden("d", $jail);
  }

  print $text{'delete_are_you_sure'};
  print "<p>\n";
  foreach my $del_jail (@d) {
    print "<i>$del_jail</i><br>\n";
  }
  print "</p>\n";

  print ui_hidden("confirmed", "1");
  #print ui_submit($text{delete_confirm}, "confirm");
  print ui_form_end([ [ "confirm", $text{'delete_confirm'} ] ]);
  print "</center>\n";
  ui_print_footer("");
}
