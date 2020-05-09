import lirc

sockid = lirc.init("myprogram", "mylircrc")
lirc.load_config_file("~/airconditionor.lircd.conf")
