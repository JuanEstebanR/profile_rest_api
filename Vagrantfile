Vagrant.configure("2") do |config|
  # Use the Ubuntu 20.04 (Focal Fossa) box
  config.vm.box = "ubuntu/focal64"

  # Forward port 8000 from the guest to the host
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    # Disable daily apt tasks to avoid conflicts
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer

    # Update package list and install prerequisites
    sudo apt-get update
    sudo apt-get install -y software-properties-common

    # Add Deadsnakes PPA for newer Python versions
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update

    # Install Python 3.9 and related packages
    sudo apt-get install -y python3.9 python3.9-venv python3.9-dev python3-pip

    # Ensure alias is set in .bash_aliases
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
        echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
        echo "alias python='python3.9'" >> /home/vagrant/.bash_aliases
    fi

    # Update pip for the newly installed Python version
    python3.9 -m pip install --upgrade pip || echo "Python 3.9 pip upgrade failed."
  SHELL
end
