# By using puppet we create a file in /tmp

file { '/tmp/school':
  ensure  => 'present',
  content => 'I love puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
