import subprocess
result = subprocess.run(['kubectl','get','pods','-n',sys.argv[1]], stdout=subprocess.PIPE)
result.stdout