# Puppet manifest to install nginx, configure the server and sets a custom header

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "/server_name _;/ a \  \  \  \  add_header X-Served-By $HOST;" /etc/nginx/sites-available/default',
  before      => Exec['start Nginx'],
}

exec { 'start Nginx':
  provider => shell,
  command  => 'sudo service nginx start',
  before   => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
