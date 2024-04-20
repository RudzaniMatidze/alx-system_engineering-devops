# Using Puppet, install flask from pip3.

package {'flask':
  ensure   => '2.0.2',
  provider => 'pip3',
}
