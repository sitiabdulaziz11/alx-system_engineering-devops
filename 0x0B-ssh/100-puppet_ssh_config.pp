# practice using Puppet set up your client SSH configuration file that used to
# coonnect to a server without typing a password.

host { 'Alx_server':
  hostname               => '54.87.172.4',
  user                   => 'ubuntu',
  identityfile           => '~/.ssh/school',
  passwordauthentication => 'no',
}

