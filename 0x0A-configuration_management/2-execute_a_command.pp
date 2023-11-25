# Using Puppet, create a manifest that kills a process named killmenow
# pkill and exec must be used

exec { 'pkill -f killmenow':
  path => '/usr/bin/:usr/localbin/:bin/'
}
