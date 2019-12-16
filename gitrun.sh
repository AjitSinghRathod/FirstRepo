cd ~/pcc/
sudo rm -rf EliteCSM
git clone git@gitlab.sterlitetech-software.com:EliteCSM/Development/EliteCSM.git
sed -i s/pcc-docker-repo:5043[/]//g /home/sterlite/pcc/EliteCSM/Applications/nvsmx/docker/Dockerfile
cd EliteCSM/Applications/netvertex/docker
chmod +x build-nvsmx-image.sh
./build-nvsmx-image.sh 7.1.0.1
