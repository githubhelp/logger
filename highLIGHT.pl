use strict;
use vars qw($VERSION %IRSSI);

use Irssi;
$VERSION = '0.1';
%IRSSI = (
	authors     => 'Simon Norberg',
	contact     => 'simon@dackbrann.net',
	name        => 'highLIGTH',
	description => 'Sends a signal to external hardware to light up on highligth and off on dehighligt',
	license     => 'BSD',
);

my $highlighted = 0;

sub highLIGHT 
{
	my $dest = shift;
	$highlighted = 1;
	if ($dest->{level} & MSGLEVEL_HILIGHT)
	{
		system("python /home/simon/logger/writeLED.py green on");
	}
}

sub dehighLIGHT 
{
	if ($highlighted == 1)
	{
		$highlighted = 0;
		system("python /home/simon/logger/writeLED.py green off");
		system("python /home/simon/logger/writeLED.py blue off");
	}
}

sub priv_msg
{
	system("python /home/simon/logger/writeLED.py blue on");
}
#--------------------------------------------------------------------
# Irssi::signal_add_last / Irssi::command_bind
#--------------------------------------------------------------------
Irssi::signal_add_last("message private", "priv_msg");
Irssi::signal_add_last("print text", "highLIGHT");
Irssi::signal_add_last("window changed", "dehighLIGHT");
Irssi::signal_add_last("send text", "dehighLIGHT");

#- end
