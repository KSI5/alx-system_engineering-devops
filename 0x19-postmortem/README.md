# Postmortem Report - Service Outage on November 5, 2023

<p align="center"><a href="url"><img src="https://pbs.twimg.com/media/D71yyZAWkAAPRbb.jpg" width="480" height="360"></a></p>


## Issue Summary

**Duration:** The outage occurred on November 5, 2023, from 3:00 PM to 6:00 PM (UTC-5).

**Impact:** The primary service affected was our cloud storage platform. During the outage, users experienced complete downtime, leading to severe disruptions in their workflows. Approximately 75% of our users were affected, resulting in widespread frustration and negative business impact.

## Root Cause

The root cause of the outage was a critical infrastructure failure. A major network switch, part of the core data center infrastructure, experienced a hardware malfunction.

## Timeline

### Issue Detected

- **Time:** 3:00 PM (UTC-5)
- **Detection:** The issue was detected when our automated monitoring system generated alerts for network connectivity failures within the data center. Additionally, several users reported being unable to access their files.

### Actions Taken

- Our network operations team immediately initiated an investigation. Initially, we assumed that the issue might be related to misconfigured network settings.

### Misleading Investigation

- The first hour was spent examining network configurations, firewall settings, and possible security breaches. These investigations proved to be misleading as they did not reveal the root cause.

### Escalation

- At 4:15 PM, recognizing the severity of the issue and the lack of progress, the incident was escalated to the vendor support team, as the network switch was identified as the potential source of the problem.

### Issue Resolution

- After intensive cooperation with the vendor support team, it was determined that a hardware failure within the network switch was causing the complete network outage.
- A replacement switch was deployed and configured.
- Normal service was restored by 6:00 PM.

## Root Cause and Resolution

The root cause was a hardware malfunction in the network switch, which led to a complete network outage. To resolve the issue:

- The malfunctioning network switch was replaced with a new one.
- The network configuration was reestablished on the new switch.
- System checks were performed to ensure the integrity of data and network functionality.

## Corrective and Preventative Measures

To prevent future outages and improve our system, we will:

- Maintain a spare network switch as part of the core infrastructure for rapid hardware replacement in emergencies.
- Enhance monitoring and alerting systems to detect hardware failures more proactively.
- Develop a clear escalation plan to involve vendor support promptly in cases of suspected hardware issues.
- Conduct regular hardware maintenance and testing to identify potential issues before they lead to outages.

<a href="url">
    <img src="https://img.freepik.com/free-photo/curly-haired-girl-winter-yellow-sweater-dances-with-arms-spreading-air-enjoys-music-has-overjoyed-face-expression-poses-indoor_273609-32580.jpg?w=740&t=st=1699305240~exp=1699305840~hmac=3e54d23f6c74a9cdab7ef866baebf2a892dc7cb2fea510c537767d54948dfef7" width="120" height="140">
  </a>
<br>
By implementing these measures, we aim to ensure the stability and reliability of our cloud storage platform, minimize downtime, and provide a seamless experience for our users. We understand the critical importance of our service and are committed to preventing future disruptions.

In conclusion, while outages are disruptive, they also present an opportunity to strengthen our systems and processes. We value the trust our users place in our service and will continue to learn from incidents like this to prevent them from happening again.
