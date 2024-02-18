# web stack debugging that debug wordpress website running on a LAMP stack.

$file_to_update = '/var/www/html/wp-settings.php'

#replace line that containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_update}",
  path    => ['/bin','/usr/bin']
}
