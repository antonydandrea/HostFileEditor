import array
print "###############################################################"
print "Host File Editor for Ubunutu"
print "Version 0.2"
print "Created by Antony D'Andrea"
print "###############################################################"
print ""
ip_address = raw_input("Enter the IP address:")
domain_name = raw_input("Enter the domain name:")
print "Adding %s with the IP address of %s"%(domain_name,ip_address)
print "Reading in hosts file..."
f = open('/etc/hosts', 'r+')
lines = f.readlines()

print "Read complete."

linewritten = 0
i = 0
for line in lines:
    tmp = line.split("\t")
    if len(tmp) > 1:
        if  tmp[1].strip(' \t\n\r') == domain_name:
	    print "Entry with domain name already exists. Overwriting the IP address."
            lines[i] = ip_address + "\t" + domain_name + "\n"
            linewritten = 1
            break
    i += 1

if linewritten == 0:
   lines.append(ip_address + "\t" + domain_name + "\n")

print "Writing host file..."
f.seek(0)
for line in lines:
    f.write(line)
f.truncate()
f.close()
print "Write complete."
 


