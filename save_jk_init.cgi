#!/usr/bin/perl
# save_config.cgi
# Write updated settings.ini for bloctweet

use warnings;
use strict;

our %in;
our %text;

require './jailkit-lib.pl';

my $jk_init_config = get_jk_init_config();

ReadParse();

#ui_print_header(undef, $text{'index_title'}, "". undef, 1, 1);

# Keys
if (defined $in{'keys_access_token_secret'}) {
	$bloctweet_config->{'keys'}{'access_token_secret'} = $in{'keys_access_token_secret'};
}

if (defined $in{'keys_access_token'}) {
	$bloctweet_config->{'keys'}{'access_token'} = $in{'keys_access_token'};
}

if (defined $in{'keys_consumer_secret'}) {
	$bloctweet_config->{'keys'}{'consumer_secret'} = $in{'keys_consumer_secret'};
}

if (defined $in{'keys_consumer_key'}) {
	$bloctweet_config->{'keys'}{'consumer_key'} = $in{'keys_consumer_key'};
}

# Settings
if (defined $in{'settings_refresh_rate'}) {
	$bloctweet_config->{'settings'}{'refresh_rate'} = $in{'settings_refresh_rate'};
}

if (defined $in{'settings_dm_refresh_rate'}) {
	$bloctweet_config->{'settings'}{'dm_refresh_rate'} = $in{'settings_dm_refresh_rate'};
}

if (defined $in{'settings_search_hash'}) {
	$bloctweet_config->{'settings'}{'search_hash'} = $in{'settings_search_hash'};
}

if (defined $in{'settings_hashtag_enabled'}) {
	$bloctweet_config->{'settings'}{'hashtag_enabled'} = $in{'settings_search_hash'};
}

if (defined $in{'settings_dm_enabled'}) {
	$bloctweet_config->{'settings'}{'dm_enabled'} = $in{'settings_dm_enabled'};
}

# Contributors
if (defined $in{'contributors'}) {
	my @contributors = split(' ', $in{'contributors'});
	foreach my $contributor (@contributors) {
		$bloctweet_config->{'contributors'}{$contributor} = '0';
	}
}

#Config::INI::Writer->write_file($bloctweet_config, $config{'bloctweet_config'});
write_bloctweet_config($bloctweet_config);

redirect("");

