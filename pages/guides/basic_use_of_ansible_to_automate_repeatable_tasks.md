# Basic use of Ansible to automate repeatable Tasks

When running ansible-playbooks it is a good idea to use a centrally managed  “hosts” file in your Git repo. An easy way to ensure you always do this is by adding an alias into your bashrc file as below:

alias ansible-playbook="ansible-playbook -i /git/ansible/hosts"

## Writing Playbooks:
Ansible Playbooks should be written for any task that can be automated or will be repeated (Eg System installation / Package installation + configuration).

To write an ansible Playbook, the Ansible website is very helpful for finding what commands to use for specific tasks. Eg searching in Google “ansible apt” will result in the below page which will show the usage of the apt command in Ansible with various examples:

https://docs.ansible.com/ansible/latest/modules/apt_module.html

When you have finished writing your Playbook, before commiting to Gitlab you should use Ansible to check the syntax of the script by using the –check flag as follows:

```
ansible-playbook example.yml --check
```

If the result is OK you should commit the Playbook to Gitlab after removing any target hosts on the “hosts” line.

## Running Playbooks:
Ansible Playbooks should be stored within the ansible Repository with no “host” specified so they cannot accidentally be run on all hosts.

When you wish to run a Playbook, ensure your local git repo is up to date with master, update the yaml with the hostname for the server you wish to run the script against (line #2) and execute the playbook.

Eg if you wish to deploy Logwatch to server “ubuntu”:

```
cd ansible && git pull
```

Update line #2 in playbooks/monitoring/check_mk/deploy-logwatch-ubuntu.yml with:

```
- hosts: ubuntu
```

## Execute the playbook:

```
ansible-playbook playbooks/monitoring/check_mk/deploy-logwatch-ubuntu.yml
```