# step 1
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

# step 2
package { 'nginx':
  ensure => installed,
}

# step 3
file_line { 'add_custom_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "    add_header X-Served-By \${hostname};",
  match  => '^\s+location / {',
}

# step 4
exec { 'restart_nginx_service':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => Package['nginx'],
}
