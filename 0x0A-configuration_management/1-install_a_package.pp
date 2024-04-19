# Install puppet-lint using the gem provider
package { 'puppet-lint':
  ensure => '2.5.0',
  provider => 'gem',
}
