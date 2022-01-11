# sh shell/ssh.sh
ssh -o ProxyCommand='connect -H proxy.anan-nct.ac.jp:8080 %h %p' orikami@10.40.3.171
