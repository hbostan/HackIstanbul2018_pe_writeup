# the-count-of-monte-cisco

We are given a config file of some Cisco Router. After reading a bit about cisco configs I have found that you use `enable password <password>` command to create a password. Here is the relevant [cisco page](https://www.cisco.com/c/en/us/td/docs/ios/12_2/security/configuration/guide/fsecur_c/scfpass.html). It says:
```Setting or Changing a Static Enable Password
To set or change a static password that controls access to privileged EXEC (enable) mode, use the following command in global configuration mode:

Command
Purpose
Router(config)# enable password password

Establishes a new password or change an existing password for the privileged command level.
```

Well let's search our config for passwords:
```
$ cat cisco.txt | grep "enable password"
enable password no-password-created
```

It seems a bit odd at first but `no-password-created` is our password/flag.


