from scapy.all import *
dd = rdpcap("C:\\Users\二筒\Desktop\\jaja.pcap")
for i in dd:
  #  try:
        print(i.getlayer('Raw').fields['load'].decode().strip())
  #  except:
      #  pass
