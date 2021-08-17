exec { 'sed -i "s/   PasswordAuthentication yes/   PasswordAuthentication no/g /etc/ssh/ssh_config"':
    path => '/bin'
}
exec { 'sed "/^anothervalue=    IdentityFile ~/.ssh/holberton after=#   IdentityFile ~/.ssh/id_ed25519 /etc/ssh/ssh_config"':
    path => '/bin'
}