chmod +x *
python3 install.py
python3 insta.py
echo "eb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee -a /etc/apt/sources.list
apt update
apt upgrade
apt dist-upgrade
apt autoremove
python3 installing.py
