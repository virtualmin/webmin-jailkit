#!/usr/bin/perl
# save_config.cgi
# Write updated settings.ini for bloctweet
use warnings;
use strict;

our %in;
our %text;

require './jailkit-lib.pl';

my $jk_init_ini = get_jk_init_ini();
my @sections = $jk_init_ini->Sections();
my %jail_params;

ReadParse();

# If new, create a new section
if (defined $in{'new'}) {
	if ( $jk_init_ini->SectionExists( $in{'jail'} )) {
		error( $text{'error_jail_exists'} );
	}
	$jk_init_ini->AddSection( $in{'jail'} );
}
else {
	# Not new, make sure we update the name of the jail, if
	# changed
	if ( defined($in{'orig_jail'}) && defined($in{'jail'}) &&
	 		 $in{'orig_jail'} ne $in{'jail'} ) {
		$jk_init_ini->DeleteSection($in{'orig_jail'});
		$jk_init_ini->AddSection( $in{'jail'});
	}
}

if (length $in{'comment'}) { $jk_init_ini->newval($in{'jail'},
 	'comment', $in{'comment'}); }
if (length $in{'paths'}) { $jk_init_ini->newval($in{'jail'},
	'paths', $in{'paths'}); }
if (length $in{'paths_w_owner'}) { $jk_init_ini->newval($in{'jail'},
	'paths_w_owner', $in{'paths_w_owner'}); }
if (length $in{'paths_w_setuid'}) { $jk_init_ini->newval($in{'jail'},
	'paths_w_setuid', $in{'paths_w_setuid'}); }
if (length $in{'users'}) { $jk_init_ini->newval($in{'jail'},
	'users', $in{'users'}); }
if (length $in{'groups'}) { $jk_init_ini->newval($in{'jail'},
	'groups', $in{'groups'}); }
if (length $in{'need_logsocket'}) { $jk_init_ini->newval($in{'jail'},
	'need_logsocket', $in{'need_logsocket'}); }
if (length $in{'devices'}) { $jk_init_ini->newval($in{'jail'},
	'devices', $in{'devices'}); }
if (length $in{'includesections'}) { $jk_init_ini->newval($in{'jail'},
	'includesections', $in{'includesections'}); }
if (length $in{'emptydirs'}) { $jk_init_ini->newval($in{'jail'},
	'emptydirs', $in{'emptydirs'}); }

# Contributors
#if (defined $in{'contributors'}) {
#	my @contributors = split(' ', $in{'contributors'});
#	foreach my $contributor (@contributors) {
#		$bloctweet_config->{'contributors'}{$contributor} = '0';
#	}
#}

write_jk_init_ini($jk_init_ini);

redirect('');
