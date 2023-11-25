# Using Puppet, install flask from pip3
# Version must be 2.1.0

  class install_flask {
  # ensure that python3_pip package is installed
  package {'python3-pip':
    ensure => installed,
}

# install Flask using pip3
  package { 'flask':
    ensure   => 's.1.0',
    provider => 'pip3',
    require  => package['python3-pip']
}
}
