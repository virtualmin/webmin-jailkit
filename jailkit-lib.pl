#!/usr/bin/perl

use strict;
use warnings;
use Error qw(:try);

our %config;

=head1 jailkit-lib.pl

Functions for the Jailkit Webmin module

  foreign_require("jailkit", "jailkit-lib.pl");
  $jk_init_ini = jailkit::get_jk_init_ini();

$jk_init_ini will contain a list of hashrefs of configuration
directives from jk_init.ini.

=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
init_config();

=head2 get_jk_init_ini()

Returns the jailkit configuration as a list of hash references with name and key value keys.

=cut

sub get_jk_init_ini {
	use Config::Simple;

	my $jk_init_ini = new Config::Simple('/etc/jailkit/jk_init.ini');
		#"$config{'jailkit_config_dir'}/$config{'jk_init_ini'}");
	return \%$jk_init_ini;
}

=head2 write_jk_init_ini(\%jk_init_ini)

Write configuration file array to config file. May return an error object, if write fails.

=cut

sub write_jk_init_ini {
	use Config::INI::Writer;
	my ($jk_init_ini) = @_;
	Config::INI::Writer->write_file($jk_init_ini, $config{'jk_init_ini'});
	return;
}

1;
