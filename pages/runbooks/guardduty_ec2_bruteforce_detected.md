# Guardduty EC2 bruteforce detected

This guide will cover the process to follow when you have been made aware (Eg by AWS Guardduty) of a brute force attack against one of your instances.

Runbook will cover action points below but the summary should be considered to be:

1. Validate the alert (Is it correct)
2. Isolate the instance
3. Assess damage
4. Longer term remediations

Another important note is to ensure that you take lots of notes of actions taken at each stage so a timeline can be built for later analysis and review.

table_md="| Action | Details | Owner |\n\
| --- | ----- | ----- |\n\
| Gather information |  Collect details of the instance (Location, function, source IP of the attack) | Incident engineer       |\n\
| Validate alarm | Is the concern valid? Is there an external actor acting maliciously against your instance or is someone trying to clone a git repository from the instance with their wrong ssh key (it happens!) | Incident engineer       |\n\
| Block Access | If the threat is malicious, block access to the instance imediately. There should be no reason for port 22 to be exposed to 0.0.0.0/0. If the attack is coming from an allowed IP, remove the rule allowing access. | Incident engineer  |\n\
| Assessing Compromise | Finally, review the instance logs to determine if the attacker had successfully compromised the instance. Read separate runbook on this topic | Incident engineer  |\n\
| Complete report | Write up all notes using template and submit an incident report (following your incident management procedure). | Incident engineer |\n\"

Longer term solutions:
* Investigate using AWS Config to mark Security Groups as non-compliant if they contain port 22 exposed to the internet.
* Suggest training to the team about why port 22 should not be exposed to the internet
