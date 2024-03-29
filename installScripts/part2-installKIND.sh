sudo snap install go --classic
go install sigs.k8s.io/kind@v0.18.0
export PATH=$PATH:$(go env GOPATH)/bin
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl