# könyv példája
egyik = int(input('Mi legyen az egyik szám? '))
másik = int(input('Mi legyen a másik szám? '))
# mindig a nagyobb szám legyen az osztandó
if egyik >= másik:
 osztandó = egyik
 osztó = másik
else:
 osztandó = másik
 osztó = egyik
hányados = osztandó / osztó
if hányados == int(hányados):
 print(osztó, ' osztója ', osztandó, '-nek.', sep='')
else:
 print(osztó, ' nem osztója ', osztandó, '-nek.', sep='')