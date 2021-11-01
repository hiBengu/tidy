sudo rm -rf /opt/tidy
sudo cp -R ./app/tidy /opt/tidy/
sudo rm /etc/systemd/system/tidy.service
sudo rm /usr/lib/systemd/tidy.service
sudo rm /etc/systemd/system/multi-user.target.wants/tidy.service
sudo cp ./tidy.service /usr/lib/systemd/system/
sudo ln  -sf /usr/lib/systemd/system/tidy.service /etc/systemd/system/multi-user.target.wants/tidy.service

sudo cp ./example.config /opt/tidy/

sudo systemctl daemon-reload
sudo systemctl start tidy.service
sudo systemctl enable tidy.service
sudo systemctl status tidy.service
