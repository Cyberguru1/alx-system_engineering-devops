# 0x12. Web stack debugging #2
## | DevOps | SysAdmin | Scripting | Debugging

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/287/99littlebugsinthecode-holberton.jpg)



## 0. [Run software as another user](0-iamsomeoneelse)

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/eaeff07a715ff880b1ceb8e863a1d141a74a7f85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230201%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230201T195106Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c53fd6ab65fc093227f22e0221aa76c81da340f6bc3317355237710b413fa9c0)



The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.

For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

Requirements:

    - write a Bash script that accepts one argument
    - the script should run the whoami command under the user passed as an argument
    - make sure to try your script by passing different users
Example:

```
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#

```