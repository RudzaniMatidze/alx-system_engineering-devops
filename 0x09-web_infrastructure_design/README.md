# 0x09-web_infrastructure_design

## Description:
This repository contains the setup documentation for different configurations of web infrastructures, from a simple single-server setup to a more complex and secure three-server setup, all hosting the website www.foobar.com.

## Tasks:
| File | Description |
| ---- | ------------ |
| **0-simple_web_stack** | A simple web infrastructure that hosts a website that is reachable via www.foobar.com. There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server. |
| **1-distributed_web_infrastructure** | A distributed web infrastructure that atttempts to reduce the traffic to the primary server by distributing some of the load to a replica server with the aid of a server responsible for balancing the load between the two servers (primary and replica). |
| **2-secured_and_monitored_web_infrastructure** | A 3-server web infrastructure that is secured, monitored, and serves encrypted traffic. |
| **3-scale_up** | This web infrastructure is a scaled up version of the infrastructure described here. In this version, all SPOFs have been removed and each of the major components (web server, application server, and database servers) have been moved to separate GNU/Linux servers. The SSL protection isn't terminated at the load-balancer and each server's network is protected with a firewall and they're also monitored. |
