# step 1
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

# step 2
package {'nginx':
  ensure => present,
}

# step 3
file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "    location / {
    add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

# step 4
exec { 'restart the service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
