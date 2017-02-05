#!/usr/bin/perl
use strict;
use warnings;

our (%text, %in);
require './jailkit-lib.pl';
ReadParse();

my $jk_init_ini = get_jk_init_ini();
my @sections = $jk_init_ini->Sections();
my %jail_params;

# Make a new section?
if($in{'new'}) {
  ui_print_header(undef, $text{'index_create_jail'}, '', 'create_jail');
  # Keep new defined so we add a new section on save
  print ui_hidden("new", $in{'new'});
}
else {
  ui_print_header(undef, $text{'index_edit_jail'}, '', 'edit_jail');
  unless ( $jk_init_ini->SectionExists( $in{'jail'} )) {
    error( $text{'edit_jail_not_found'} );
  };
  # Populate the jail hash
  my @params = $jk_init_ini->Parameters( $in{'jail'} );
  foreach my $param (@params){
    $jail_params{$param} = $jk_init_ini->val( $in{'jail'}, $param );
  }
}

print ui_form_start("save_jail.cgi");
print ui_hidden("orig_jail", $in{'jail'});

print ui_
print ui_hidden_table_start($text{'edit_jail_metadata'}, undef, 1, 'metadata', 1);
# name
print ui_table_row( hlink($text{'edit_jail_name'}, 'name'),
  ui_textbox('jail', $in{'jail'}));
# comment/description
print ui_table_row( hlink($text{'edit_jail_comment'}, 'comment'),
  ui_textbox('comment', $jail_params{'comment'}));
print ui_hidden_table_end('metadata');

print ui_hidden_table_start($text{'edit_jail_includes'}, undef, 1, 'includes', 1);
# paths
print ui_table_row( hlink($text{'edit_jail_paths'}, 'paths'),
  ui_textarea('paths', $jail_params{'paths'}));
print ui_table_row( hlink($text{'edit_jail_paths_w_owner'}, 'paths_w_owner'),
  ui_textarea('paths_w_owner', $jail_params{'paths_w_owner'}));
print ui_table_row( hlink($text{'edit_jail_paths_w_setuid'}, 'paths_w_setuid'),
  ui_textarea('paths_w_setuid', $jail_params{'paths_w_setuid'}));
print ui_table_row( hlink($text{'edit_jail_includesections'}, 'includesections'),
  ui_textarea('includesections'), $jail_params{'includesections'});
print ui_table_row( hlink($text{'edit_jail_emptydirs'}, 'emptydirs'),
  ui_textarea('emptydirs', $jail_params{'emptydirs'}));
print ui_table_row( hlink($text{'edit_jail_devices'}, 'devices'),
  ui_textbox('devices', $jail_params{'devices'}));
print ui_table_row( hlink($text{'edit_jail_need_logsocket'}, 'need_logsocket'),
  ui_checkbox('need_logsocket', 1,
  undef, $jail_params{'need_logsocket'} ? 1 : 0));
print ui_hidden_table_end('includes');

print ui_hidden_table_start($text{'edit_jail_ug'}, undef, 1, 'usergroups', 1);
print ui_table_row( hlink($text{'edit_jail_users'}, 'users'),
  ui_textarea('users', $jail_params{'users'}));
print ui_table_row( hlink($text{'edit_jail_groups'}, 'groups'),
  ui_textarea('groups', $jail_params{'groups'}));
print ui_hidden_table_end('usergroups');

print ui_form_end([ [undef, $text{'save_jail'}] ]);

&ui_print_footer("index.cgi", $text{'edit_jail_return'});
