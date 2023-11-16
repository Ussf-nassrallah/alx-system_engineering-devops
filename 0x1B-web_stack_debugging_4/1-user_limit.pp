# task 1 advanced

exec { 'increase-hard-file-limits':
    command  => 'sudo sed -i "/holberton hard/s/5/4096/" /etc/security/limits.conf',
    provider => shell
}

exec { 'increase-soft-file-limits':
    command  => 'sudo sed -i "/holberton soft/s/4/4096/" /etc/security/limits.conf',
    provider => shell
}