# Setup New Ubuntu server with nginx

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'configure redirect_me':
  command => "sed -i '/listen 80/a \\ \trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default",
  provider => 'shell',
  require  => Package['nginx'],
  notify   => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
