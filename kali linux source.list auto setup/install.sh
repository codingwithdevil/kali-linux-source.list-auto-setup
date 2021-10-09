chmod +x *
python3 install.py
python3 insta.py
echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee /etc/apt/sources.list
echo "deb http://http.kali.org/kali kali-last-snapshot main non-free contrib" | sudo tee /etc/apt/sources.list
echo "deb http://http.kali.org/kali kali-experimental main non-free contrib" | sudo tee /etc/apt/sources.list
 echo "deb-src http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list
apt update
apt upgrade
apt dist-upgrade
apt autoremove
python3 installing.py