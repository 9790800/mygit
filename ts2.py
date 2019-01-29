import paramiko
import getpass

user = raw_input("User: ")
secret = getpass.getpass("Password: ")
hostlbcore = raw_input("IP LBcore: ")
hostlbarcd = raw_input("IP LBarcd: ")
hostlbbd = raw_input("IP LBbd: ")
hostlbtest = raw_input("IP LBtest: ")
port = 22


def sshsess(comand, host):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=host, username=user, password=secret, port=port)
	stdin, stdout, stderr = client.exec_command(comand)
	data = stdout.read() + stderr.read()
	client.close()
	return data


#LBcore
host = hostlbcore

comand = """sudo rpm -qa | egrep -i 'lbcore-2|lbtv-2|lbphone-2' | awk -F ".git" '{print "find /opt/backup -name " $1 "*"}' """

outsshlbcore = sshsess(comand, host)
print '\033[91m' + '\n rpm LBcore ' + host +'\n' + '\033[0m'
print '\033[96m' + outsshlbcore + '\033[0m'

########

#LBarcd
host = hostlbarcd

comand = """sudo rpm -qa | egrep -i 'lbarcd-2' | awk -F ".git" '{print "find /opt/backup -name " $1 "*"}' """
outsshlbarcd = sshsess(comand, host)
print '\033[91m' + '\n rpm LBarcd ' + host +'\n' + '\033[0m' 
print '\033[96m' + outsshlbarcd + '\033[0m'

########

#LBbd
host = hostlbbd

comand = "sudo find /opt/backup -name '*.bz2' "

outsshlbbd = sshsess(comand, host)
print '\033[91m' + '\n BD LBbd ' + host +'\n' + '\033[0m' 
print '\033[96m' + outsshlbbd + '\033[0m'

########
key = 'no'
key =raw_input("Download? (yes/no): ")
if ( key == 'yes' ): print 'Download...'

