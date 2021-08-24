# Automate Create a server and Add a custom HTTP header with Puppet

exec { 'Update':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo apt-get update -y',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'Install_nginx':
  require  => Exec['Update'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo apt-get install nginx -y',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'header':
  require  => Exec['Install_nginx'],
  path     => ['/usr/bin', '/sbin', '/usr/sbin'],
  command  => 'sudo sed -i "s/http {/http {\n\tadd_header X-Served-By \$hostname;\n/" /etc/nginx/nginx.conf',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'start_server':
  require  => Exec['header'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo service nginx start',
  provider => 'shell',
  returns  => [0,1],
}
