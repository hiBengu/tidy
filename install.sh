file_name=tidy.py
install_path=/usr/bin/
service_path=/etc/systemd/system/
service_file=tidy.service
example_config=example.config

sudo rm ${install_path}tidy.py
sudo cp ./${file_name} ${install_path}${file_name}
sudo cp ./${example_config} ${install_path}${example_config}


sudo rm ${service_path}tidy.service
sudo bash -c "cat <<EOF >${service_path}${service_file}
[Install]
WantedBy=multi-user.target

[Unit]
Description=A program to tidy your folders
After=network.target

[Service]
User=$USER
Group=$USER
Type=forking
ExecStart=/usr/bin/python /usr/bin/tidy.py
EOF"

sudo systemctl daemon-reload
sudo systemctl start tidy.service
sudo systemctl enable tidy.service
sudo systemctl status tidy.service
