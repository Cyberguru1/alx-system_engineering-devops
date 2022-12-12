# 0x09. Web infrastructure design

![](https://alx-intranet.hbtn.io/images/challenge2022/get-started.jpg)

## **Requirements**
> # General

1. A README.md file, at the root of the folder of the project, is mandatory
2. For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram
3. This project will be manually reviewed:
4. As each task is completed, the name of that task will turn green
Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use imgur but feel free to use anything you want).
5. For the following tasks, insert the link from of your screenshot into the answer file
6. After pushing your answer file to GitHub, insert the GitHub file link into the URL box
7. You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session
Focus on what you are being asked:
8. Cover what the requirements mention, we will explore details in a later project
Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements
9. Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
10. In this project, again, avoid going in details if not asked

## Learning Objectives
## **General**
1. You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
2. You must be able to explain what each component is doing
3. You must be able to explain system redundancy
4. Know all the mentioned acronyms: LAMP, SPOF, QPS

## Task 1

> *On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.*

### **Requirements:**

### **You must use:**
        1 server
        1 web server (Nginx)
        1 application server
        1 application files (your code base)
        1 database (MySQL)
        1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

[0-simple_web_stack](0-simple_web_stack)
![](www.imgur.com/a/6PLEZtX)


## Task 2
> On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com.

### **Requirements:**

### **You must add:**
        2 servers
        1 web server (Nginx)
        1 application server
        1 load-balancer (HAproxy)
        1 set of application files (your code base)
        1 database (MySQL)
[1-distributed_web_infrastructure](1-distributed_web_infrastructure)


## Task 3

> On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

### **Requirements:**

### **You must add:**
        3 firewalls
        1 SSL certificate to serve www.foobar.com over HTTPS
        3 monitoring clients (data collector for Sumologic or other monitoring services)

