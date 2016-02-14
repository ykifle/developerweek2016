# file: .profile.d/ssh-setup.sh

#!/bin/bash
echo $0: creating private key files

# Create the .ssh directory
mkdir -p ${HOME}/.ssh
chmod 700 ${HOME}/.ssh

eval `ssh-agent -s`

# Create the public and private key files from the environment variables.
echo "${OREGON_PRIVATE_KEY}" > ${HOME}/.ssh/oregon.pem
chmod 600 ${HOME}/.ssh/oregon.pem
ssh-add ${HOME}/.ssh/oregon.pem

# Note use of double quotes, required to preserve newlines
echo "${DEVWEEK_PRIVATE_KEY}" > ${HOME}/.ssh/devweek2016.pem
chmod 600 ${HOME}/.ssh/devweek2016.pem
ssh-add ${HOME}/.ssh/devweek2016.pem

