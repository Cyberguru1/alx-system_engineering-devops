# using puppet to config ssh_config IdentityFile
file {'ssh_config':
    content => 'Include /etc/ssh/ssh_config.d/*.conf 
Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes',
    }