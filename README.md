Ansible project for 'RabbitMQ' configurations.

Example:

ansible-playbook -i inventory.yml playbook.yml --ask-vault-pass --ask-pass 

* Install RabbitMQ service (latest available from RabbitMQ repository)
* Install RabbitMQ admin plugin
* Remove guest user
* Create a vhost and a user with read, write privileges on the created vhost
* Modify RabbitMQ openfiles limit to 100K

* Service user password should be stored in ansible vault
* RabbitMQ installation should be suitable for Debian operating system
* Yaml files should pass linter (for example: yamllint)

* Use firewall to:
  - open rabbitmq admin console to outside
  - open default rabbitmq port for localhost only

* Create a simple rabbitmq producer (publisher) script (use language of your choice) which should:
  - create test exchange
  - create test queue with TTL parameter (3600 seconds)
  - bind test exchange to test queue
  - produce sample messages to the created test exchange