# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.env.enable
	config.vm.box = "google/gce"
	#config.vm.box_check_update = false
	config.vm.network "forwarded_port", guest: 80, host: 8080
	#config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
	#config.vm.network "private_network", ip: "192.168.33.10"
	#config.vm.network "public_network"
	config.vm.synced_folder "../data", "/vagrant_data"
	config.vm.provider :google do |google, override|
		google.google_project_id = ENV["GCE_PROJECT_ID"]
		google.google_client_email = ENV["GCE_CLIENT_EMAIL"]
		google.google_json_key_location = ENV["GCE_JSON_KEY_PATH"]
		google.image_family = "ubuntu-1604-lts"
		override.ssh.username = ENV["GCE_SSH_USERNAME"]
		override.ssh.private_key_path = ENV["GCE_PRIVATE_KEY_PATH"]
	end
	config.vm.provision "shell", inline: <<-SHELL
	  apt-get -qq upgrade && apt-get -qq update
	SHELL
end
