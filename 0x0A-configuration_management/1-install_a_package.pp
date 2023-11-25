# Using Puppet, install flask from pip3 with version of `2.1.0`

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
